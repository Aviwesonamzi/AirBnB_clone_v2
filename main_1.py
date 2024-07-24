#!/usr/bin/python3
"""Test script to create a State object with FileStorage"""
from models import storage
from models.state import State

if __name__ == "__main__":
    storage.reload()  # Ensure storage is loaded
    state = State(name="California")
    state.save()
    print(state.id)
