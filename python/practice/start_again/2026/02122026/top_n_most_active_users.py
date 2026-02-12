# return the top N active users in the last hour

from collections import defaultdict
from datetime import datetime, timedelta

def top_n_active_users(logs, n, current_time):
    one_hour_ago = current_time - timedelta(hours=1)
    user_counts = defaultdict(int)
    for timestamp, user_id, action in logs:
        if timestamp >= one_hour_ago:
            user_counts[user_id] += 1
    sorted_user = sorted(user_counts.items(), key = lambda x:x[1], reverse=True)
    return [user for user, count in sorted_user[:n]]