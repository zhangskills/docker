# coding=utf-8
import os
import hanlp

from flask import Flask, request
from gevent.pywsgi import WSGIServer

HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH,
                   tasks=['ner/pku'])

# init flask
app = Flask(__name__)

PASSWORD = '1245679'
UNA_UTHORIZED_CODE = 401
UNA_UTHORIZED_MSG = "认证失败"
BAD_REQUEST_CODE = 400
BAD_REQUEST_MSG = "参数错误"
NOT_FOUND_CODE = 404
NOT_FOUND_MSG = "请求的资源不存在，或者没有这个请求方法"


# 单个样本输入，输入为Unicode编码的字符串
# seg 普通分词
@app.route('/hanlp', methods=['POST'])
def hanlp():
    text = request.form['text']
    password = request.form['password']
    # auth error
    if password != PASSWORD:
        return create_error_respose(UNA_UTHORIZED_CODE, UNA_UTHORIZED_MSG)
    if text and password:
        return lac_common(text)
    # bad request
    else:
        return create_error_respose(BAD_REQUEST_CODE, BAD_REQUEST_MSG)


# error page relink
@app.errorhandler(400)
def errorhandler(error):
    return create_error_respose(BAD_REQUEST_CODE, BAD_REQUEST_MSG)


@app.errorhandler(404)
def request_not_found(error):
    return create_error_respose(NOT_FOUND_CODE, NOT_FOUND_MSG)


def lac_common(text):
    if not text:
        return {"data": []}
    seg_result = HanLP([text])
    return {"data": seg_result}


def create_error_respose(error_code, error_msg):
    return {
               "error_code": error_code,
               "error_msg": error_msg,
               "data": [],
           }, error_code


if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.config["DEBUG"] = False
    # app.run(host='127.0.0.1', port='8080')
    host_name = os.environ.get('ADDRESS')
    port = os.environ.get('PORT')
    password = os.environ.get('PASSWORD')

    if not host_name:
        host_name = ''

    if not port:
        port = 8080
    else:
        port = int(port)

    if password:
        PASSWORD = password

    http_server = WSGIServer((host_name, port), app)
    http_server.serve_forever()
