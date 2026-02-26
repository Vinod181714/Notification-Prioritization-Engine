def ingest_notification(payload):
    """
    POST /notifications/ingest
    """
    required_fields = ["notification_id", "user_id", "type", "urgency", "business_impact", "content"]

    for field in required_fields:
        if field not in payload:
            raise ValueError(f"Missing field: {field}")

    return payload
