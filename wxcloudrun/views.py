from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/message', methods=['POST'])
def handle_message():
    # 获取请求体中的message
    data = request.get_json()

    if 'message' not in data:
        return jsonify({'error': 'Missing message parameter'}), 400

    message = data['message']

    # 返回相同的message
    return jsonify({'message': message}), 200


if __name__ == '__main__':
    app.run(debug=True)
