from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load JSON data from file
with open('static/test_execution_data.json', 'r') as f:
    json_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    test_suite = request.form.get('test_suite')
    product = request.form.get('product')
    subproduct = request.form.get('subproduct')
    primary_environment = request.form.get('primary_environment')
    nested_environment = request.form.get('nested_environment')
    execution_date = request.form.get('execution_date')

    filtered_data = json_data

    if test_suite:
        filtered_data = [item for item in filtered_data if item['Test Suite'] == test_suite]

    if product == 'All':
        filtered_data = json_data  # Return all data for "All" option
    elif product:
        filtered_data = [item for item in filtered_data if item['Product'] == product]

    if subproduct:
        filtered_data = [item for item in filtered_data if item['Subproduct'] == subproduct]

    if primary_environment:
        filtered_data = [item for item in filtered_data if item['Primary Environment'] == primary_environment]

    if nested_environment:
        filtered_data = [item for item in filtered_data if item['Nested Environment'] == nested_environment]

    if execution_date:
        filtered_data = [item for item in filtered_data if item['Execution Date'].split('T')[0] == execution_date]

    # Prepare the data to send back to the frontend
    response_data = [{
        'Test Case ID': item['Test Case ID'],
        'Status': item['Status'],
        'Failed Reason': item['Failed Reason'],
        'Oracle Module': item['Oracle Module'],
        'Product': item['Product'],
        'Primary Environment': item['Primary Environment'],
        'Nested Environment': item['Nested Environment'],
        'Execution Date': item['Execution Date']
    } for item in filtered_data]

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
