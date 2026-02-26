import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Training data (sample)
data = pd.DataFrame({
    "urgency": [1,2,3,3,2,1],
    "impact": [1,3,5,4,2,1],
    "response_rate": [0.2,0.5,0.9,0.8,0.6,0.3],
    "responded": [0,1,1,1,0,0]
})

X = data[["urgency", "impact", "response_rate"]]
y = data["responded"]

model = LogisticRegression()
model.fit(X, y)

def predict_response_probability(notification, user):
    try:
        features = np.array([[notification.urgency,
                               notification.business_impact,
                               user.response_rate]])
        return model.predict_proba(features)[0][1]
    except Exception:
        return user.response_rate  # fallback
