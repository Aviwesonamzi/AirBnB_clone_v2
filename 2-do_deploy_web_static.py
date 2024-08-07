#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, put, run
import os

env.hosts = ['54.237.32.102', '54.87.237.86']

def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the file name without the directory path
        file_name = os.path.basename(archive_path)
        # Extract the name without the extension
        name_no_ext = file_name.split('.')[0]
        release_dir = f"/data/web_static/releases/{name_no_ext}/"
        tmp_path = f"/tmp/{file_name}"

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, tmp_path)

        # Uncompress the archive to the folder
        run(f"mkdir -p {release_dir}")
        run(f"tar -xzf {tmp_path} -C {release_dir}")

        # Delete the archive from the web server
        run(f"rm {tmp_path}")

        # Move files out of the sub-directory
        run(f"mv {release_dir}web_static/* {release_dir}")
        run(f"rm -rf {release_dir}web_static")

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current linked to the new version
        run(f"ln -s {release_dir} /data/web_static/current")

        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
