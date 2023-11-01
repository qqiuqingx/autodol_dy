
from utils.config import config
from flask import Flask


import logging.config
import sys

def create_app():
    app = Flask(__name__)

    # 初始化数据
    config.load(None)
    logging.config.dictConfig(LOG_CONF)
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
            'level': logging.DEBUG,
            'class': 'common.log.SafeRotatingFileHandler',
            'when': 'W0',
            'interval': 1,
            'backupCount': 1,
            'filename': 'download2.log',
            'formatter': 'verbose'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': logging.INFO,
    },
    'loggers': {
        'biliup': {
            'handlers': ['file'],
            'level': logging.INFO,
        },
    }
}