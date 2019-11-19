from . import routes
from .. import Config
from werkzeug.exceptions import abort
from flask import request

# Access to app
@routes.before_request
def limit_remote_addr():
    if Config.LIMIT_ACCESS:
        if not request.remote_addr in Config.WHITE_LIST_IPS:
            abort(404)  # Not Found

