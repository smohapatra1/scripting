# Per User Rate Limiter

from collections import defaultdict, deque
import time

class RateLimter:
    def __init__(self, max_request=100, window = 60):
        self.max_request = max_request
        self.window = window
        self.user_requests = defaultdict(deque)
    def allow_request(self, user_id):
        now = time.time()
        q = self.user_requests(user_id)
        while q and now -q[0] > self.window:
            q.popleft()
        if len(q) < self.max_request:
            q.append(now)
            return True
        else:
            return False
