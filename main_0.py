#!/usr/bin/python3
"""Test script to create a State object"""
from models import storage
from models.state import State

if __name__ == "__main__":
    state = State(name="California")
    state.save()
    print(state.id)
