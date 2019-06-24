from .app import app
from flask import request, jsonify
from model.user import User

@app.route("/api/account_info/<api_key>",methods=['GET'])
def route(api_key):
	user = api_authenticate(api_key)
	print(api_key)
	if user is None:
		return(404)
	return jsonify({"username":user.username, "realname":user.realname, "balance":user.balance})




