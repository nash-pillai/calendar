from flask import Flask, render_template, request, send_from_directory, Markup
from datetime import datetime
from utils import colorize, events
import os, logging

app = Flask(__name__)
logging.getLogger('werkzeug').disabled = True


@app.before_first_request
def logs_request_info():
  print(colorize("90", "First request"))

@app.before_request
def log_request_info():
  print(
    colorize("92", request.method), "request", 
    "at", colorize("95", datetime.now()), 
    "from", colorize("93", request.headers.get("X-Forwarded-For").split(",")[0]), 
    "for", colorize("96", request.script_root + request.path)
  )

@app.route('/')
def index(): 
  return render_template('index.html', events=Markup(events))

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(
    os.path.join(app.root_path, "static", "images"), 
    "favicon.ico", 
    mimetype='image/vnd.microsoft.icon'
  )


app.run('0.0.0.0', 8080, debug=True, use_reloader=True)