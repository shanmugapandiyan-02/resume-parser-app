from flask import Flask, request

mock_app = Flask(__name__)

@mock_app.route('/api/profile', methods=['POST'])
def receive_profile():
    profile = request.json
    print("Received Profile:", profile)
    return {"status": "success"}, 200

if __name__ == '__main__':
    mock_app.run(port=5001)
