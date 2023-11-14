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

    app.add_url_rule('/addjob/<room_id>', view_func=add_job)
    app.add_url_rule('/getAlljob', view_func=getAlljob)
    app.add_url_rule('/getjob/<roomid>', view_func=getjob)
    app.add_url_rule('/stopjob/<roomid>', view_func=stopjob)
    app.add_url_rule('/test', view_func=test)


def my_function(url):
    try:
      suffix = "mp4"  # 指定文件后缀
      child_instance = Douyin('fname', url, suffix=suffix)  # 创建子类对象
      download_instance = child_instance  # 将子类对象赋值给父类变量
    # download_instance = DownloadBase(fname, url, suffix=suffix, opt_args=download_args)
    # 开始下载

      success = download_instance.start()
    finally:
        
         logger.info('删除任务:',url,remove_dict(download_instance.roomid))
        # download_instance.rename(f'{download_instance.file_name}.{download_instance.suffix}')
     
