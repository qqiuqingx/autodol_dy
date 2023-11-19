from flask_restful import  Resource, reqparse

from .common.threadUtil import add_dict,get_all_dict,get_dict,remove_dict
from flask import jsonify
import argparse
from .douyin import Douyin
from .common.models import jobdetailed
import logging
import re

logger = logging.getLogger('biliup')
def check_positive(value):
    #if not re.match(r'^\d+$', value):
    if not (isinstance(value, str) and value.isdigit()and len(value) > 0):
        raise argparse.ArgumentTypeError(f"{value} is not a valid room_id (a string containing only digits)")
    return value
# 使用 reqparse 定义参数解析器
parser = reqparse.RequestParser()
parser.add_argument('room_id', type=check_positive, required=True, help='房间号错误')

class JobResource(Resource):
    #添加
    def post(self):
        args = parser.parse_args()
        room_id = args['room_id']
        if room_id is None:
            return {'data': None}
        url = f"live.douyin.com/{room_id}"
        logger.info(f'添加任务:{url}')
        #return "add_dict(room_id, my_function, url)"
        rest=add_dict(room_id, my_function, url)
        return {'data': rest}

    #获取所有
    def get(self):
        jobs = []
        global_executor_dict = get_all_dict()
        for key in global_executor_dict.keys():
            threadtt = global_executor_dict.get(key)
            job = jobdetailed(key, threadtt.nickname, threadtt.isFinish)
            jobs.append(job.to_dict())

        return {'data': jobs}

class SingleJobResource(Resource):
    #获取单个任务
    def get(self, roomid):
        threadtt = get_dict(roomid)
        if threadtt is None:
            return {'data': None}
        job = jobdetailed(roomid, threadtt.nickname, threadtt.isFinish)
        return {'data': job.to_dict()}
    #删除
    def delete(self, roomid):
        threadtt = get_dict(roomid)
        if threadtt:
            threadtt.setFinish()
            return {'Finish': threadtt.isFinish}
        return {'Finish': False}

class TestResource(Resource):
    def get(self):
        return {'data': 'success'}

def add_restful_routes(api):
 api.add_resource(JobResource, '/jobs')
 api.add_resource(SingleJobResource, '/jobs/<roomid>')
 api.add_resource(TestResource, '/test2')




def my_function(url):
    try:
      
      child_instance = Douyin('fname',url=url).start()  # 创建子类对象
    finally:
         success=remove_dict(child_instance.roomid)
         logger.info(f'删除任务:{url}---{success}')