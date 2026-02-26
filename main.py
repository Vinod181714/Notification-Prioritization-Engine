from datetime import datetime
from models.notification import Notification
from models.user_context import UserContext
from services.deduplication import deduplicate_notifications
from services.priority_engine import calculate_priority
from services.fatigue_control import adaptive_suppression
from services.ml_predictor import predict_response_probability
from config.settings import DECISION_THRESHOLDS

users = {
    "U1": UserContext("U1", "sales", 0.8, (9,18))
}

notifications = [
    Notification("N1", "U1", "lead", "CRM", 3, 5, datetime.now(), "New hot lead"),
    Notification("N2", "U1", "lead", "CRM", 3, 5, datetime.now(), "New hot lead")
]

notifications = deduplicate_notifications(notifications)

for n in notifications:
    user = users[n.user_id]

    if adaptive_suppression(n):
        decision = "NEVER"
    else:
        score = calculate_priority(n, user) + predict_response_probability(n, user)
        if score >= DECISION_THRESHOLDS["NOW"]:
            decision = "NOW"
        elif score >= DECISION_THRESHOLDS["LATER"]:
            decision = "LATER"
        else:
            decision = "NEVER"

    print(f"{n.notification_id} → {decision}")
