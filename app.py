from flask import Flask, render_template, url_for, request, redirect
from random import random
from time import sleep
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

timer_date = (datetime.utcnow()).strftime("%d %b %Y, %H:%M:%S")

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
    timer_date = (datetime.utcnow()).strftime("%d %b %Y, %H:%M:%S")
    return redirect(url_for("timer"))

@app.route("/api/latestreset")
def get_latestreset():
    global timer_date
    return timer_date

@app.route("/api/settime", methods=["POST"])
def post_settime():
    global timer_date
    timer_date = request.json["time"]

    # datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    # "20 Oct 2020, 06:18:12"
    # datetime_object = datetime.strptime(request.json["time"], '%d %b %Y, %H:%M:%S')

    return f"Set time to: {timer_date}"


if __name__ == '__main__':
    app.run()