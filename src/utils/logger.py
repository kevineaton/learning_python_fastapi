# src/utils/logger.py
import logging
from datetime import datetime

# set up a basic config
logging.basicConfig(
    level=logging.DEBUG, # we will show everything while testing, and eventually take this from the environment
    filename="log.log", # write to log.log in the running dir
    filemode="w", # overwrite each time
    format="%(message)s", # format the data according to the template; since we create the line ourselves, this is fine
)

def log(level, message, **options):
    # normalize the level
    level = level.upper()
    if level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        level = "INFO"
    
    # for options, we care about module and extra for now
    module = "?"
    extra = {}

    if "module" in options:
        module = options["module"]
    if "extra" in options:
        extra = options["extra"]

    # set the time format
    # we will come back and improve this with our basic config
    time_format = "%Y-%m-%d %H:%M:%SZ"
    now = datetime.now()
    
    line = f"{now.strftime(time_format)}:{level}:Module {module}: {message}:: {extra}"

    # switch on the level
    match level:
        case "DEBUG":
            logging.debug(line)
        case "INFO":
            logging.info(line)
        case "WARNING":
            logging.warning(line)
        case "ERROR":
            logging.error(line)
        case "CRITICAL":
            logging.critical(line)