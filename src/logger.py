import logging
import os
from datetime import datetime

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up one level to the project root
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory in project root if not exists
logs_path = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path of log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode='a'),  # File handler
        logging.StreamHandler()  # Console handler
    ]
)

# Create a logger instance
logger = logging.getLogger(__name__)

def log_info(message):
    """Log info message"""
    logger.info(message)

def log_error(message):
    """Log error message"""
    logger.error(message)

def log_warning(message):
    """Log warning message"""
    logger.warning(message)

def log_debug(message):
    """Log debug message"""
    logger.debug(message)

if __name__ == "__main__":
    logger.info("Logging is started")
    print(f"Log file created at: {LOG_FILE_PATH}")