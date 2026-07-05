# Logging
import logging
from logging.handlers import RotatingFileHandler

# Cluster
import multiprocessing # Multi processor
import uvicorn # Uvicorn

# API
from api.main import app # API
import api.config.config as config # Config

# Setup logging
log_file = config.LOG_API_DESTINATION

# File handler for logging
handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Get the root logger and set its level to INFO
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

# Capture logs for uvicorn error and access logs
uvicorn_error_logger = logging.getLogger("uvicorn.error")
uvicorn_error_logger.addHandler(handler)
uvicorn_error_logger.setLevel(logging.INFO)

uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.addHandler(handler)
uvicorn_access_logger.setLevel(logging.INFO)

# Log some initial information
logger = logging.getLogger("uvicorn")
logger.info("Agent application started!")
logger.info(f"Agent Version: {config.AGENT_VERSION}")
logger.info("OpenHubble By Amirhossein Mohammadi - 2025")

# Run the ASGI server
if __name__ == "__main__":
    num_workers = multiprocessing.cpu_count()  # Number of processors
    uvicorn.run("asgi:app", host=config.BIND_IP, port=int(config.PORT), workers=num_workers)