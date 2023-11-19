from .common.threadUtil import add_dict,get_all_dict,get_dict,remove_dict
from flask import jsonify
from .douyin import Douyin
from .common.models import jobdetailed
import logging
logger = logging.getLogger('biliup')
def add_job(room_id):
    url = f"live.douyin.com/{room_id}"
    logger.info(f'添加任务:{url}')
    return add_dict(room_id,my_function,url)

def getAlljob():
    jobs=[]
    global_executor_dict=get_all_dict()
    for key in global_executor_dict.keys():
        threadtt=global_executor_dict.get(key)
        print(key,threadtt.isFinish)
        job=jobdetailed(key,threadtt.nickname,threadtt.isFinish)
        jobs.append(job.to_dict())

    return jsonify({'data':jobs})

def getjob(roomid):
    threadtt=get_dict(roomid)
    if threadtt is None:
        return jsonify({'data':None})
    job=jobdetailed(roomid,threadtt.nickname,threadtt.isFinish)
    return jsonify({'data':job.to_dict()})

def stopjob(roomid):
    threadtt=get_dict(roomid)
    threadtt.setFinish()
    return jsonify({'Finish':threadtt.isFinish})

def test():
    return jsonify({'test':'success'})
def add_new_routes(app):

    app.add_url_rule('/add/<room_id>', view_func=add_job)
    app.add_url_rule('/jobs', view_func=getAlljob)
    app.add_url_rule('/getjob/<roomid>', view_func=getjob)
    app.add_url_rule('/stop/<roomid>', view_func=stopjob)
    app.add_url_rule('/test', view_func=test)


def my_function(url):
    try:
      
      child_instance = Douyin('fname',url=url).start()  # 创建子类对象
    finally:
         success=remove_dict(child_instance.roomid)
         logger.info(f'删除任务:{url}---{success}')

     
