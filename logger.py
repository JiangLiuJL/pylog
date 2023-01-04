import logging
import colorlog
import os

# 创建一个 logger 对象
logger = logging.getLogger("logger")

# 设置日志输出颜色
log_colors_config = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

# 设置日志级别
logger.setLevel(logging.DEBUG)

# 判断日志目录是否存在
exist = os.path.exists('../log')
if not exist:
    os.mkdir('../log')

# 创建一个 handler，用于写入日志文件
file_handler = logging.FileHandler('../log/log.txt', encoding='utf-8')

# 再创建一个 handler，用于输出到控制台
console_handler = logging.StreamHandler()

# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 设置日志控制台输出格式
consoleFormatter = colorlog.ColoredFormatter(
    fmt='%(log_color)s[%(asctime)s - %(name)s - %(levelname)s] : %(message)s',
    log_colors=log_colors_config
)
console_handler.setFormatter(consoleFormatter)

# 将 handler 添加到 logger 对象中
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def INFO(message):
    logger.info(message)


def ERROR(message):
    logger.error(message)


def WARNING(message):
    logger.warning(message)


def CRITICAL(message):
    logger.critical(message)


def DEBUG(message):
    logger.debug(message)
