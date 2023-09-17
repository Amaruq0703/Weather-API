from flask import Flask , render_template
import pandas as pd

#Creation of Flask web app

app = Flask(__name__)

#Reading of data and creating dataframe

stations = pd.read_csv('data small\stations.txt', skiprows=17)
stationdisplay = stations[['STAID','STANAME                                 ']]

#Homepage

@app.route('/')
def home():
    return render_template('home.html', data=stationdisplay.to_html())

#Return temperature value of specified station at specified date

@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = 'data small\TG_STAID'+ str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']== date]['   TG'].squeeze()/10
    return {'Station': station, 
            'Date': date,
            'temperature': temperature }

#Return all Temperature values of specified station

@app.route('/api/v1/<station>')
def alldata(station):
    filename = 'data small\TG_STAID'+ str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])

    #Made result look neater

    df['Temperature'] = df.loc[df['   TG'] != -9999]['   TG']/10
    df['Date'] = df['    DATE']
    df = df[['Date', 'Temperature']]
    listoftemps = df.to_dict(orient='records')
    return listoftemps

#Return all weather values of specified station for specified year

@app.route('/api/v1/yearly/<station>/<year>')
def yeardata(station, year):
    filename = 'data small\TG_STAID'+ str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))]
    result = df.to_dict(orient='records')
    return result





app.run(debug=True)