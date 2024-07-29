#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create versions directory if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')
    
    # Define the archive name with the current date and time
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    # Create the archive
    result = local(f"tar -cvzf {archive_name} web_static")

    # Check if the archive was created successfully
    if result.failed:
        return None
    return archive_name
