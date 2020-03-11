from flask import Flask, request, jsonify, make_response
import calculus as calc
import base64
import logging
app = Flask(__name__)


success_message = {"error": False, "result": ""}
fail_message = {"error": True, "message": "bad input"}


@app.route('/calculus', methods=['GET'])
def calculus():
    logging.error("WE HIT THIS")
    if 'query' not in request.args:
        print('this?')
        fail_message['message'] = "no query was supplied"
        return make_response(jsonify(fail_message), 400)
    arg = request.args.get("query")
    data_bytes = base64.urlsafe_b64decode(str(arg))
    calculation = data_bytes.decode("utf-8")
    print("SEE ME HERE YES NOW")
    print(calculation)
    try:
        print('here?')
        success_message["result"] = calc.compute(calculation)
    except:
        print('we get here')
        return make_response(jsonify(fail_message, 400))
    return make_response(jsonify(success_message), 200)


if __name__ == '__main__':
    app.run('0.0.0.0', port=80)
