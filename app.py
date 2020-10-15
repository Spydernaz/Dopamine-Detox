from flask import Flask, render_template, url_for, copy_current_request_context, redirect
from random import random
from time import sleep
from datetime import datetime
from threading import Thread, Event


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

timer_date = (datetime.datetime.utcnow() + datetime.timedelta(hours=11)).strftime("%m %b %Y, %H:%M:%S")


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return redirect(url_for("timer"))

@app.route("/timer")
def timer():
    global timer_date
    return render_template("cover.html", date=timer_date)

@app.route("/reset-timer")
def reset_timer():
    global timer_date
    timer_date = (datetime.datetime.utcnow() + datetime.timedelta(hours=11)).strftime("%m %b %Y, %H:%M:%S")
    return redirect(url_for("timer"))

@app.route("/api/latestreset")
def get_latestreset():
    global timer_date
    return timer_date

if __name__ == '__main__':
    app.run()