import requests
import os
from flask import Flask, jsonify, render_template, request, url_for, redirect, flash

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>testing</h1>"

