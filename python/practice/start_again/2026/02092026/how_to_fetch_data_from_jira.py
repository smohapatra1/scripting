#   https://www.geeksforgeeks.org/python/how-to-fetch-data-from-jira-in-python/

from jira import JIRA

jiraOptions = {'server': "https://jira.test.com/"}
jira = JIRA(options=jiraOptions, basic_auth=("sam@t.com", "your_api_token"))
for singleIssue in jira.search_issues(jql_str='project=test'):
    print('{}: {}: {}'.format(singleIssue.key, singleIssue.fields.summary,
                              singleIssue.fields.reporter.displayName))