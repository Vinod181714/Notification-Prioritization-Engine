import hashlib
from datetime import datetime

class Notification:
    def __init__(self, notification_id, user_id, n_type, source,
                 urgency, business_impact, timestamp, content):
        self.notification_id = notification_id
        self.user_id = user_id
        self.type = n_type
        self.source = source
        self.urgency = urgency
        self.business_impact = business_impact
        self.timestamp = timestamp
        self.content = content
        self.content_hash = self._generate_hash()

    def _generate_hash(self):
        return hashlib.md5(self.content.encode()).hexdigest()