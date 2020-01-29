from flask import Flask
from flask_cors import CORS
from .functions.tennis import get_tennis_data
import atexit
import json


from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

cron = BackgroundScheduler(daemon=True)
# Explicitly kick off the background thread
cron.add_job(get_tennis_data,'interval',minutes=60)
cron.start()

# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

@app.route("/tennisData")
def getTennisData():
    with open('cache/availabilities.json', 'r')  as file:
        tennis_data = json.load(file)

    response = app.response_class(
        response=json.dumps(tennis_data),
        status=200,
        mimetype='application/json'
    )
    return response
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
