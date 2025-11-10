#   https://www.geeksforgeeks.org/python/python-projects-beginner-to-advanced/
#   https://www.geeksforgeeks.org/python/convert-emoji-into-text-in-python/

import demoji
demoji.download_codes()

text="""I will be your 🎅🎅"""

demoji.findall(text)