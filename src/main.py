
from .utils.config import config
from flask import Flask
from .common.log import SafeRotatingFileHandler




import logging.config
import sys
class infoFilter(logging.Filter):
    def filter(self, record):
        # 自定义过滤条件
        return record.levelno == logging.INFO
def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    logging.config.dictConfig(LOG_CONF)
    # 初始化数据
    config.load(None)
 
    # 添加其他配置
    # app.config['DEBUG'] = True

    # 添加路由和视图函数
    # ...
    
    return app     

LOG_CONF = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': "%(asctime)s %(filename)s[line:%(lineno)d](Pid:%(process)d "
                      "Tname:%(threadName)s) %(levelname)s %(message)s",
            # 'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(filename)s%(lineno)d[%(levelname)s]Tname:%(threadName)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': logging.DEBUG,
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'simple'
        },
        'file': {
            'level': logging.INFO,
             'class': 'logging.handlers.TimedRotatingFileHandler',
            #'class': 'logging.FileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'filename': 'download.log',
            'formatter': 'verbose',
            'encoding': 'utf-8',
            # 'suffix': '%Y-%m-%d',  # 自定义时间戳格式
            'filters': ['custom_filter']  # 过滤器'
        },
        'error_log': {
            'level': logging.ERROR,
            #'class': 'common.log.SafeRotatingFileHandler',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'filename': 'error.log',
            'encoding': 'utf-8',
            'formatter': 'verbose'
        }        
    },
    'root': {
        'handlers': ['console'],
        'level': logging.DEBUG,
    },
    'filters': {
        'custom_filter': {
            '()': infoFilter,
        },
    },
    'loggers': {
        'biliup': {
            'handlers': ['error_log','file'],
            'level': logging.INFO,
        },
    }
}