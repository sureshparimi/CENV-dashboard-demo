import json
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Function to generate fake test data in JSON format
def generate_test_data(num_records):
    data = []
    oracle_modules = {
        'Finance': ['Billing', 'AP', 'AR'],
        'HR': ['Recruitment', 'Payroll', 'Employee Management'],
        'Supply Chain': ['Inventory', 'Procurement', 'Order Management'],
        # Add more modules and their respective products as needed
    }
    nested_environments = {
        'Dev': ['SD1', 'DEV', 'DEV4'],
        'Test': ['TST1', 'TST2'],
        'Staging': ['ACC'],
        'Production': ['PROD']
    }
    test_suites = ['Regression', 'E2E', 'Sanity']

    for _ in range(num_records):
        module = random.choice(list(oracle_modules.keys()))
        product = random.choice(oracle_modules[module])
        primary_env = random.choice(list(nested_environments.keys()))
        nested_env = random.choice(nested_environments[primary_env])
        data.append({
            'Test Case ID': fake.uuid4(),
            'Status': random.choice(['Passed', 'Failed', 'Skipped']),
            'Test Suite': random.choice(test_suites),
            'Failed Reason': fake.sentence() if random.random() < 0.3 else None,
            'Oracle Module': module,
            'Product': product,
            'Primary Environment': primary_env,
            'Nested Environment': nested_env,
            'Execution Date': fake.date_time_between(start_date='-30d', end_date='now').isoformat()
        })

    # Write generated data to a JSON file
    with open('test_execution_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Generate sample test data in JSON format
generate_test_data(1000)  # Adjust the number of records as needed