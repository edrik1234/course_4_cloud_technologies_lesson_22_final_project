from flask import Flask
import json
import os
import logging
import print_colors as colors 

global KNOWS_NAMES
KNOWS_NAMES = None


logging.basicConfig(
    level = logging.INFO, 
    format = '%(asctime)s|%(funcName)s|%(levelname)s|%(name)s|%(message)s|%(process)d|%(lineno)d' ,
    handlers = [
        logging.FileHandler("apps.log"), # Log to a file
        logging.StreamHandler() # Also log to console
                ]     
            )

app = Flask(__name__)


def load_names():
    try:
        with open("config.json") as json_file:
            KNOWS_NAMES = set(json.load(json_file))
            logging.info("all supported names are " + str(KNOWS_NAMES))
            return KNOWS_NAMES
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
    logging.info("all supported names are " + str(KNOWS_NAMES))
    logging.info(f"the user accessed the login with name {name}")
    if name in my_set:
        logging.info(f"name {name} is in list - access granted")
        returned_value = colors.printGreen("Access Granted")
        return returned_value
    else:
        logging.warning(f"the name {name} is not in list - access denied")
        returned_value = colors.printRed("Access Denied")
        return returned_value   


@app.route("/addname/<name>")
def addname(name):
    my_set.add(name)
    with open("config.json", "w") as json_file:    
        json.dump(list(KNOWS_NAMES), json_file)
    returned_value =  colors.printGreen(f"name {name} added successfully")
    return returned_value


if __name__ == "__main__":
    global KNOWS_NAMES
    KNOWS_NAMES = load_names()
    app.run(host = os.environ.get("HOST_IP"), port = 80)
   



