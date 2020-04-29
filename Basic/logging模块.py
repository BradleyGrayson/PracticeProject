import logging
import logging.config

# 设置log级别、输出格式，及log文件的重定位
# log级别: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s - %(processName)s - %(message)s",
                    # 默认情况下log是不断追加到该文件中的
                    filename=".\\log_test_ThisCanBDeletet.txt")
# 也可以指定配置信息从指定的配置文件中读取
# logging.config.fileConfig("xxx.conf")

logger = logging.getLogger(__name__)

logger.debug("debug level")
logger.info("info level")
logger.warning("warning level")
logger.error("error level")
logger.critical("critical level")


def funlog():
    logger.info("Entering 'funlog' function")


logger.info("Calling 'funlog' function")
funlog()