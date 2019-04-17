from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
				return "Hello, world!"
	if request.method == 'POST':
		return "method not supported", 405

@app.route('/test', methods=['GET', 'POST'])
def test():
			if request.method== 'GET':
				return "GET Message Received"
			if request.method== 'POST':
				message =request.args.get('msg')
				if message is None:
					return "method not supported", 405
				else:

					return "POST message received: "+ message

if __name__ == "__main__":
	app.debug = True;
	app.run(host = "0.0.0.0", port = 8081)
