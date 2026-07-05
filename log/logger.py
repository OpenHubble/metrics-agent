# # Logging
# import logging
# from logging.handlers import RotatingFileHandler
#
# # Config
# import api.config.config as config
#
# # Set up logging
# log_file = config.LOG_APP_DESTINATION
#
# # Create a file handler and set up log formatting
# handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
#
# # Create a logger and add the handler
# logger = logging.getLogger("app")
# logger.addHandler(handler)
# logger.setLevel(logging.INFO)
#
# # Log an initial message when the logger is configured
# logger.info("Logger initialized successfully!")
#
# # Return the logger so it can be used elsewhere
# def get_logger():
#     return logger
