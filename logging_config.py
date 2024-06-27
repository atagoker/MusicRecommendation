import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('app.log'),
                              logging.StreamHandler()])

logger = logging.getLogger(__name__)

def main():
    logger.info("Application started")

if __name__ == "__main__":
    main()
