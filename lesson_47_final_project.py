from flask import Flask
import json
import os
import logging
import print_colors as colors 
import subprocess


global KNOWN_NAMES  
KNOWN_NAMES = None

logging.basicConfig(
    level = logging.INFO, 
    format = '%(asctime)s|%(funcName)s|%(levelname)s|%(name)s|%(message)s|%(process)d|%(lineno)d' ,
    handlers = [
        logging.FileHandler("apps.log"), # Log to a file
        logging.StreamHandler() # Also log to console
                ]     
            )
app = Flask(__name__)


def run_local_command(command):
    try:
        # Run the command
        result = subprocess.run(command, shell = True, check = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
        if result.stdout:
            logging.info(result.stdout)
            return result.stdout.strip()
        else:
            logging.error(result.stderr)
            logging.error("the command isn't executed good")
            return f'error is:{result.stderr.strip()}'

    except subprocess.CalledProcessError as e:
        logging.critical(f"{command} return non-zero exit status {e.returncode} and error output {e.stderr}")
        print(f"Command '{command}' returned non-zero exit status {e.returncode}")
        print(f"Error output: {e.stderr}")
        return f"Error: {e.stderr.strip()}"


def load_names():
    try:
        with open("config.json") as json_file:
            KNOWN_NAMES = set(json.load(json_file))
            logging.info("all supported names are " + str(KNOWN_NAMES))
            return KNOWN_NAMES
    except(json.JSONDecodeError):
        logging.warning("json decode error maybe empty set, or not valid return type")
    except(FileNotFoundError):
        logging.critical("Error: Config file missing")
    return set()


@app.route("/")
def hello():
    logging.info("user has accessed the path")
    returned_value = colors.printBlack("Welcome to my system, Please login.")
    return returned_value


@app.route("/login/<name>")
def newpath(name):
    logging.info("all supported names are " + str(KNOWN_NAMES))
    logging.info(f"the user accessed the login with name {name}")
    if name in KNOWN_NAMES:
        logging.info(f"name {name} is in list - access granted")
        returned_value = colors.printGreen("Access Granted")
        return returned_value
    else:
        logging.warning(f"the name {name} is not in list - access denied")
        returned_value = colors.printRed("Access Denied")
        return returned_value   


@app.route("/addname/<name>")
def addname(name):
    KNOWN_NAMES.add(name)
    with open("config.json", "w") as json_file:    
        json.dump(list(KNOWN_NAMES), json_file)
    returned_value =  colors.printGreen(f"name {name} added successfully")
    return returned_value

if __name__ == "__main__":
    KNOWN_NAMES = load_names()
    app.run(host = os.environ.get("HOST_IP"), port = 80)
   



