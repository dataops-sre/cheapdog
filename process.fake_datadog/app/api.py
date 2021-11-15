import json
import logging
import os
import sys
import zlib
from os import path

import monitoring
import pymongo
from flask import Flask, Response, jsonify, request, make_response

app = application = Flask("datadoghq")
monitoring.monitor_flask(app)
handler = logging.StreamHandler(sys.stderr)
app.logger.addHandler(handler)
app.logger.setLevel("INFO")

record_dir = path.join(path.dirname(path.abspath(__file__)), "recorded")

MONGODB_HOST = os.getenv("MONGODB_HOST", "127.0.0.1")

@app.route("/api/v1/container", methods=["POST"])
def container():
    # TODO
    output= '{"msg": "hihi"}'
    return make_response(jsonify(output), 200)

@app.before_request
def logging():
    # use only if you need to check headers
    # mind where the logs of this container go since headers contain an API key
    # app.logger.info(
    #     "path: %s, method: %s, content-type: %s, content-encoding: %s, content-length: %s, headers: %s",
    #     request.path, request.method, request.content_type, request.content_encoding, request.content_length, request.headers)
    app.logger.info(
        "path: %s, method: %s, content-type: %s, content-encoding: %s, content-length: %s",
        request.path,
        request.method,
        request.content_type,
        request.content_encoding,
        request.content_length,
    )

@application.errorhandler(404)
def not_found(_):
    app.logger.warning("404 %s %s", request.path, request.method)
    return Response("404", status=404, mimetype="text/plain")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
