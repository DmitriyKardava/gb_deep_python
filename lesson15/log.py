import logging
log_file = "dir_traversal.log"
FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.INFO, filemode='a', style='{',
                    format=FORMAT)
logger = logging.getLogger(__name__)
