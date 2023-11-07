
from utils.config import config
from flask import Flask


import logging.config
import sys
class infoFilter(logging.Filter):
    def filter(self, record):
        # 自定义过滤条件
        return record.levelno == logging.INFO
def create_app():
    app = Flask(__name__)
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
            'class': 'common.log.SafeRotatingFileHandler',
            'when': 'W0',
            'interval': 1,
            'backupCount': 1,
            'filename': 'download.log',
            'formatter': 'verbose',
            'filters': ['custom_filter']  # 过滤器'
        },
        'error': {
            'level': logging.ERROR,
            'class': 'common.log.SafeRotatingFileHandler',
            'when': 'W0',
            'interval': 1,
            'backupCount': 1,
            'filename': 'error.log',
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
            'handlers': ['file','error'],
            'level': logging.INFO,
        },
    }
}