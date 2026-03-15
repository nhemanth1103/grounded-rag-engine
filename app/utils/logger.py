import logging

def setup_logger():
    logger = logging.getLogger("rag_system")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger