import logging
from logging.handlers import RotatingFileHandler
def setup_logging():
    log_formate_str = '%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
    """配置日志系统，使其追加日志到 app.log 文件。"""
    log_format = logging.Formatter(log_formate_str)
    # 文件日志处理器
    file_handler = RotatingFileHandler('app.log', maxBytes=1000, backupCount=0, encoding='utf-8')
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.INFO)
    # 控制台日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(logging.INFO)
    # 获取并配置根日志记录器
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    # 防止日志消息被重复处理
    root_logger.propagate = False