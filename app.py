from flask import Flask, request, jsonify, make_response
import calculus as calc
import base64
import logging
app = Flask(__name__)


success_message = {"error": False, "result": ""}
fail_message = {"error": True, "message": "bad input"}


@app.route('/calculus', methods=['GET'])
def calculus():
    if 'query' not in request.args:
        fail_message['message'] = "no query was supplied"
        return make_response(jsonify(fail_message))
    try:
        arg = str(request.args.get("query"))
        if not arg.endswith('='):
            arg=arg+'='
        data_bytes = base64.urlsafe_b64decode(arg)
        calculation = data_bytes.decode("utf-8")

        success_message["result"] = calc.compute(calculation)
    except:
        return make_response(jsonify(fail_message))
    return make_response(jsonify(success_message))


if __name__ == '__main__':
    app.run('0.0.0.0', port=80)
