from collections import defaultdict

MAX_ALERTS_PER_HOUR = 2
ignored_count = {"service": 3}

def rate_limit(notifications):
    user_count = defaultdict(int)
    filtered = []

    for n in notifications:
        if user_count[n.user_id] < MAX_ALERTS_PER_HOUR:
            filtered.append(n)
            user_count[n.user_id] += 1
        else:
            print(f"Rate limited: {n.notification_id}")

    return filtered


def adaptive_suppression(notification):
    return ignored_count.get(notification.type, 0) > 2
