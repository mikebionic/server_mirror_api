from . import api


@api.route("/hello")
def hello():
	return "world"