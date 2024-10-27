import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

# hier steuern wir den redis-Service an
redis_cache = Redis(host=os.getenv('REDIS_HOST', 'localhost'),
              port=os.getenv('REDIS_PORT', 6379))

@app.route('/')
def hello_world():
     return f'<h1>Hi, hier sehen wir Redis und Flask in Kubernetes!</h1>'

@app.route('/visits')
def visitor():
     redis_cache.incr('num_visits')
     counter = redis_cache.get('num_visits').decode("utf-8")
     return f'<h2>Anzahl der Besucher auf dieser Seite: {counter}</h2>'

@app.route('/visits/reset')
def reset_visits_counter():
    redis_cache.set('num_visits', 0)
    counter = redis_cache.get('num_visits').decode("utf-8")
    return f'<h2>Anzahl der Besucher wurde zurückgesetzt auf: {counter}</h2>'