from flask import Flask, request, jsonify, render_template, redirect
import flask
import os

app = Flask(__name__)

def getGames():
	games = os.listdir("builds")
	return games

def getURL(game):
	return f"unity/{game}/index.html"

@app.route('/')
def homepage():
	return render_template("home.html", getGames=getGames, getURL=getURL)

@app.route('/makecode')
def makecodeRedirect():
	return redirect("http://arcade.makecode.com/", code=302)

@app.route('/unity/<path:path>')
def catch_all(path):
	path = "builds/"+path
	isFile = os.path.isfile(path)
	if isFile: return flask.send_file(path)
	else: return "null"


@app.route('/favicon')
def favicon():
	return flask.send_file("favicon.png")

app.run(host="0.0.0.0", port=5000)
