from flask import Flask , render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/api/v1/<station>/<date>')
def about(station, date):
    temperature = 23
    return {'Station': station, 
            'Date': date,
            'temperature': temperature}

app.run(debug=True)