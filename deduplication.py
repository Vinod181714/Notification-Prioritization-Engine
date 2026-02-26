def deduplicate_notifications(notifications):
    seen = {}
    final_notifications = []

    for n in notifications:
        key = (n.user_id, n.content_hash)
        if key not in seen:
            seen[key] = n
            final_notifications.append(n)
        else:
            print(f"Duplicate suppressed for user {n.user_id}: {n.notification_id}")

    return final_notifications
