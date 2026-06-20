import logging 
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

def setuplogging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(name)s -> %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler(LOGS_DIR / 'app.log', encoding='utf-8'),
            logging.StreamHandler()
        ]

)


