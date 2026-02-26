class UserContext:
    def __init__(self, user_id, role, response_rate, working_hours):
        self.user_id = user_id
        self.role = role
        self.response_rate = response_rate
        self.working_hours = working_hours  # (start_hour, end_hour)
