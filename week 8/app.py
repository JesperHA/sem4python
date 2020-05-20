import re
from flask import Flask, jsonify, abort, request, flash, request, redirect, url_for,render_template
import exercise1 as backend

# Lav en flask server, hvor du åbner minimum 2 endpoints:
# - GET : returner data omkring antallet af crimes i en given periode 
# (giv to datoer med som query-param i URL'en)
# - POST : returner den totale mængde af "burglaries" i januar, men returner kun data, 
# hvis request.body indeholder et json objekt med key-value {"key":"secret"}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_crimes():
    if request.method == 'GET':
        day1 = request.args.get('day1')
        day2 = request.args.get('day2')
        print(day1)
        print(day2)
        if day1 != None:

            crime_dict = backend.data_finder(day1, day2)

            return render_template("crimes.html", crimes=crime_dict)
        

    
    return render_template("crimes.html",)


app.run(threaded=False)