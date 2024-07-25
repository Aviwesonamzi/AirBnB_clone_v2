#!/usr/bin/python3
"""
Starts a Flask web application that serves a dynamic web page
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays the HBNB filters page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    # Sort the data alphabetically by name
    sorted_states = sorted(states, key=lambda x: x.name)
    sorted_amenities = sorted(amenities, key=lambda x: x.name)
    sorted_places = sorted(places, key=lambda x: x.name)

    return render_template('100-hbnb.html',
                           states=sorted_states,
                           amenities=sorted_amenities,
                           places=sorted_places)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
