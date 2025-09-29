Final Docker Project:

  This project demonstrates building and deploying a Dockerized Python web application on AWS EC2.

Workflow:

  1)Build & Save Image.

  2)Build a Docker image with docker build.

  3)Save it as a .tar file and transfer to EC2 via scp.

  4)Deploy on EC2.

  5)Load the image with docker load.

  6)Runs a container exposing a Flask web server.

API Functionality

  / → Displays a welcome message.

  /login/<name> → Validates user against config.json (grants/denies access).

  /addname/<name> → Adds a user to config.json persistently.

Lessons Learned:

  Initially, I tried syncing config.json with the local Windows filesystem using Docker volumes, Docker Compose, PowerShell, shell scripts, SCP/SFTP, etc., but these approaches failed. Eventually, I learned to      simplify by handling persistence within the container itself.

Tech Stack:

  Used: Flask, Docker, AWS EC2, Python, Logging, SCP.
  Explored (unsuccessfully): Docker Compose, PowerShell, Bash scripts, SCP, SFTP.

If you have any questions you can also contact me in linked in☺️:
  https://www.linkedin.com/in/edrian-netyosov-9b412b282/
