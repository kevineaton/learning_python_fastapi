# src/app.py
import utils.logger

extra = { "test" : "data" }
utils.logger.log("DEBUG", "this is a sample debug", module="Main", extra=extra)
utils.logger.log("INFO", "this is a sample info", module="Main", extra=extra)
utils.logger.log("WARNING", "this is a sample warning", module="Main", extra=extra)
utils.logger.log("ERROR", "this is a sample error", module="Main", extra=extra)
utils.logger.log("CRITICAL", "this is a sample critical", module="Main", extra=extra)