import logging

from config import LoggerSetup
from server import HttpServer

log = logging.getLogger(__name__)

LoggerSetup.setup_logging()
log.info("初始化日志完成")
HttpServer.runHttpServer()
