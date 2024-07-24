#!/usr/bin/python3
"""Switches to the FileStorage engine"""
from models import storage
from models.engine.file_storage import FileStorage

if __name__ == "__main__":
    storage.__class__ = FileStorage
    storage.reload()
