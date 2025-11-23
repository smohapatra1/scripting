#   https://www.geeksforgeeks.org/python/desktop-notifier-python/

import time
import notify2
from topnews import topStories

ICON_PATH = "icon.png"
newsitems = topStories
notify2.init("News Notifier")
n = notify2.Notification(None, icon=ICON_PATH)
n.set.urgency(notify2.URGENCY_NORMAL)
n.set_timeout(10000)  # Notification timeout in milliseconds
for newsitem in newsitems:
    n.update(newsitem['title'], newsitem['description'])
    n.show()
    time.sleep(10)