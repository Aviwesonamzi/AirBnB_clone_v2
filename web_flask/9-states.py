#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage session after each request"""
    storage.close()

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display a list of all States or a specific State with its cities"""
    states = storage.all(State)
    if id:
        state = states.get(f'State.{id}')
        if state:
            cities = sorted(state.cities, key=lambda city: city.name)
        else:
            state, cities = None, []
    else:
        state, cities = None, []
    
    return render_template('9-states.html', states=states, state=state, cities=cities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
