from flask import Flask, request
from flask import json
import issueHandler
import planCreator
import config

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """
    A Flask route handler for the '/webhook' endpoint that handles incoming POST requests.
    
    Parameters:
        None
        
    Returns:
        - If the payload action is 'get_github_repos', it returns a JSON response with data from issueHandler.get_github_repos.
        - If the payload action is 'create_issue', it returns a JSON response with data from issueHandler.create_issue.
        - If the payload action is 'get_all_issues', it returns a JSON response with data from issueHandler.get_all_issues.
        - If the payload action is 'get_possible_labels', it returns a JSON response with data from issueHandler.get_possible_labels.
        - If the payload action is 'get_existing_labels', it returns a JSON response with data from issueHandler.get_existing_labels.
        - If the payload action is 'add_label_to_issue', it returns a JSON response with data from issueHandler.add_label_to_issue.
        - If the payload action is 'leave_comment_on_issue', it returns a JSON response with data from issueHandler.leave_comment_on_issue.
        - If the payload action is 'get_all_pull_requests', it returns a JSON response with data from issueHandler.get_all_pull_requests.
        - If the payload action is 'merge_pull_request', it returns a JSON response with data from issueHandler.merge_pull_request.
        - If the payload action is 'issues', it calls issueHandler.handle_issue.
        - If the payload action is 'issue_comment', it calls issueHandler.handle_comment.
        - If the payload action is 'pull_request', it calls issueHandler.handle_pull_request.
        - If the payload action is unknown, it prints a message to the console.

    Note: This function is a Flask route handler and is intended to be used with the @app.route decorator.
    """
    print('Hello World!')
    payload = request.get_json()
    # Check the event type
    if payload['action'] == 'get_github_repos':
        data = issueHandler.get_github_repos(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'create_issue':
        data = issueHandler.create_issue(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'get_all_issues':
        data = issueHandler.get_all_issues(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'get_possible_labels':
        data = issueHandler.get_possible_labels(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'get_existing_labels':
        data = issueHandler.get_existing_labels(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'add_label_to_issue':
        data = issueHandler.add_label_to_issue(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'leave_comment_on_issue':
        data = issueHandler.leave_comment_on_issue(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'get_all_pull_requests':
        data = issueHandler.get_all_pull_requests(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'merge_pull_request':
        data = issueHandler.merge_pull_request(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'issues':
        data = issueHandler.handle_issue(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'issue_comment':
        data = issueHandler.handle_comment(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif payload['action'] == 'pull_request':
        data = issueHandler.handle_pull_request(payload)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        print(f"Received unknown action type: {payload['action']}")

    return '', 200

if __name__ == '__main__':
    app.run(port=3000)
