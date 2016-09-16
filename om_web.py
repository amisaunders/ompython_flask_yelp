# om_web.py

from flask import Flask, render_template
import weather
import os
app = Flask(__name__)

@app.route("/")

def index():
	return render_template('index.html')

@app.route("/about")

def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="127.0.0.1", port=port)

