from flask import request, jsonify, make_response

from . import api
from .get_server_mirrors_data import get_server_mirrors_data

@api.route("/server-mirrors/")
def server_mirrors():
	MirrorAppName = request.args.get("app", "", str)
	
	data = get_server_mirrors_data(MirrorAppName)

	res = {
		"status": 1 if data else 0,
		"data": data,
		"message": f"Server Mirrors of {MirrorAppName}"
	}

	return res