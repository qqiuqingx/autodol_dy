import threading
from utils.config import config
from concurrent.futures import ThreadPoolExecutor
from .models import threadtt
        
global_executor_dict_lock = threading.Lock()
global_executor_dict = {}
thread_max=config.get('thread_max',5)
executor=ThreadPoolExecutor(thread_max)
def add_dict(key,task_function, *args, **kwargs):
    with global_executor_dict_lock:
        # print("add "+key)
        # print(len(global_executor_dict))
        if not checkCount():
            return "超过线程数量"
        executor_instance= global_executor_dict.get(key)
        if executor_instance is None : 
         future=executor.submit(task_function, *args, **kwargs)
         global_executor_dict[key] = threadtt(future,True)
         return "添加成功"
        else:
          return "存在相同任务"

# def checkCount():
#     with global_executor_dict_lock:
#         if len(global_executor_dict)>=thread_max:
#             for key, future in global_executor_dict.items():
#              if future.done():
#                  del global_executor_dict[key]
#                  return True
#             return False
#         else:
#          return True
def checkCount():

            if len(global_executor_dict) >= thread_max:
                 for key, threadtt in global_executor_dict.items():
                  if threadtt.future.done():
                   del global_executor_dict[key]
                   return True
                 return False
            else:
              return True
def get_dict(key):
   with global_executor_dict_lock:
        executor_instance= global_executor_dict.get(key)
        return executor_instance
def remove_dict(key):
    with global_executor_dict_lock:
        executor_instance= global_executor_dict.get(key)
        if executor_instance is not None:
            del global_executor_dict[key]
            return True
        else:
            return False
def get_all_dict():
    with global_executor_dict_lock:
        return global_executor_dict