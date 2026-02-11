#   https://www.geeksforgeeks.org/python/how-to-fetch-data-from-jira-in-python/

import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
url = "https://yourdomain.atlassian.net/rest/api/2/search"
auth = HTTPBasicAuth("youremail@gmail.com", "your_api_token")
headers = {"Accept": "application/json"}
query = {'jql': 'project = MedicineAppBugs'}

response = requests.get(url, headers=headers, auth=auth, params=query)
DictProjectIssue = response.json()
listAllIssues = []

def IterrateDictIsues (OIssues, listliner):
    for key, values in OIssues.items():
        if key == "fields":
            IterrateDictIsues(values, listliner)
        elif key == "reporter":
            IterrateDictIsues(values, listliner)
        elif key == "key":
            listliner.append(values)
        elif key == "summary":
            listliner.append(values)
        elif key == "displayName":
            listliner.append(values)
for key, value in DictProjectIssue.items():
    if key == "issues":
        for eachIssue in value:
            listliner = []
            IterrateDictIsues(eachIssue, listliner)
            listAllIssues.append(listliner)
dfIssues = pd.DataFrame(listAllIssues, columns=["KEY", "SUMMARY", "Reporter"])
print (dfIssues)