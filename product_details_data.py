# import pandas as pd
# from faker import Faker
# import random
# from datetime import datetime, timedelta

# fake = Faker()

# # Function to generate fake test data
# def generate_test_data(num_records):
#     data = []
#     oracle_modules = {
#         'Finance': ['Billing', 'AP', 'AR'],
#         'HR': ['Recruitment', 'Payroll', 'Employee Management'],
#         'Supply Chain': ['Inventory', 'Procurement', 'Order Management'],
#         'CRM': ['Contact Management', 'Communication Tracking', 'Opportunity Tracking'],
#         'HCM': ['Employee Records', 'Benefits Management', 'Recruitment Automation'],
#         'Project Management': ['Budget Tracking', 'Resource Allocation', 'Project Visualization'],
#         'ERP Analytics': ['Profitability Analysis', 'Expense Tracking', 'Working Capital Improvement']
#         # Add more modules and their respective products as needed
#     }
#     nested_environments = {
#         'Dev': ['SD1', 'DEV', 'DEV4'],
#         'Test': ['TST1', 'TST2'],
#         'Staging': ['ACC'],
#         'Production': ['PROD']
#     }
#     test_suites = ['Regression', 'E2E', 'Sanity']

#     for _ in range(num_records):
#         module = random.choice(list(oracle_modules.keys()))
#         product = random.choice(oracle_modules[module])
#         primary_env = random.choice(list(nested_environments.keys()))
#         nested_env = random.choice(nested_environments[primary_env])
#         data.append({
#             'Test Case ID': fake.uuid4(),
#             'Status': random.choice(['Passed', 'Failed', 'Skipped']),
#             'Test Suite': random.choice(test_suites),
#             'Failed Reason': fake.sentence() if random.random() < 0.3 else None,
#             'Oracle Module': module,
#             'Product': product,
#             'Primary Environment': primary_env,
#             'Nested Environment': nested_env,
#             'Execution Date': fake.date_time_between(start_date='-30d', end_date='now')
#         })

#     return pd.DataFrame(data)

# # Generate sample test data
# test_data = generate_test_data(1000)  # Adjust the number of records as needed

# # Save generated data to a JSON file for loading into your dashboard
# test_data.to_json('product_details.json', orient='records', date_format='iso')
