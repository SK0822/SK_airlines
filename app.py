from flask import Flask, render_template

from flights import generate_random_flight_data as g

app = Flask(__name__,template_folder='app/templates')


@app.route('/')
def index():
    flight_data = g()
    return render_template('index.html', flight_data=flight_data)


if __name__ == '__main__':
    app.run(debug=True)
