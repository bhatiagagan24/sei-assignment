from flask import Flask, jsonify, request
from core import get_compliance_analysis_results
from utils import validate_request_data
import json

app = Flask(__name__)

## /create-compliance-report creates a compliance report and returns 
## a report number that can be used to get the report.
## Error handling can be improved
@app.route('/create-compliance-report', methods=['POST', 'GET'])
def check_compliance():
    request_data = request.get_json()
    if not validate_request_data(request_data):
        ## Return error code
        return jsonify({'err': 'Incomplete Request Body'})
    return json.loads(get_compliance_analysis_results(request_data['url'], request_data['api_token']))

@app.route('/get-compliance_report', methods=['GET'])
def get_report():
    compliance_report = request.args.get('compliance_report')
    if not compliance_report:
        return jsonify({'err': 'Missing Compliance Report Number'})


if __name__ == '__main__':
    app.run(debug=True)