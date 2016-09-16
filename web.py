from flask import Flask, render_template, request
import weather
import om_yelp
import os
app = Flask(__name__)


@app.route("/")
def index():
	address = request.values.get('address')
	forecast = None
	top = None
	if address:
		forecast = weather.get_weather(address)
		top = om_yelp.top_spots(address)
	return render_template('index.html', forecast=forecast, top=top)


@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == "__main__":
	# app.run()
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)