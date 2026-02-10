#   https://www.geeksforgeeks.org/python/how-to-fetch-data-from-jira-in-python/

from jira import JIRA

jiraOptions = {'server': "https://yourdomain.atlassian.net/"}
jira = JIRA(options=jiraOptions, basic_auth=("youremail@gmail.com", "your_api_token"))

singleIssue = jira.issue('TEST-1')
print('{}: {}: {}'.format(singleIssue.key, singleIssue.fields.summary, singleIssue.fields.reporter.displayName))