import datetime

def calculate_priority(notification, user):
    age_minutes = (datetime.datetime.now() - notification.timestamp).seconds / 60
    recency_score = max(0, 1 - age_minutes / 60)

    priority_score = (
        0.4 * notification.urgency +
        0.3 * notification.business_impact +
        0.2 * recency_score +
        0.1 * user.response_rate
    )

    return round(priority_score, 2)
