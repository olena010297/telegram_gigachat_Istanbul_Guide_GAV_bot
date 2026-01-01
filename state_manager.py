from collections import defaultdict

class StateManager:
    def __init__(self):
        self._users = defaultdict(dict)

    def get_state(self, user_id: int) -> dict:
        return self._users[user_id]

    def update_state(self, user_id: int, **kwargs):
        self._users[user_id].update(kwargs)

    def set_mode(self, user_id: int, mode: str):
        self.update_state(user_id, mode=mode)
