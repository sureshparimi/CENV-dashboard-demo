from jira import JIRA

# Jira server URL and API token
JIRA_SERVER = 'https://parimiams.atlassian.net/'
API_TOKEN = 'ATATT3xFfGF0FndjNxaiMugAqiEpOdiyNS7xbxNUbhDR2EYVeLdTHtC9yAjaB8UgLpobrgYilV-PA3SizohDPqh12mbgwFry2cwJsQ_yD0gRb7RycioefpmqQt9TtNoSTze-G6DMByRZptMYN-ULRSlFncsCz52lJin5JwZFUAu3bVGmZISvSR4=DCC79E2D'

# Connect to Jira using API token
options = {
    'server': JIRA_SERVER
}
jira = JIRA(options=options, api_token=API_TOKEN)

# Fetch issues using JQL (Jira Query Language)
jql = 'project = BOOK'  # Change 'YOUR_PROJECT_NAME' to your actual project name or key
issues = jira.search_issues(jql)

# Create a list to store issue data
issue_data = []

# Extract data from each issue and store it in a list
for issue in issues:
    issue_dict = {
        'Key': issue.key,
        'Summary': issue.fields.summary,
        'Status': issue.fields.status.name,
        # Add more fields as needed
    }
    issue_data.append(issue_dict)

# Save issue data to a JSON file
import json

with open('issue_data.json', 'w') as json_file:
    json.dump(issue_data, json_file, indent=4)

print(f"Issue data saved to 'issue_data.json'")
