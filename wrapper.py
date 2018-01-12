# coding: utf-8
import functools
import json
from Queue import Queue

queue = Queue()
def watch_instance_param(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('jobid为: %s 的参数被修改了'%args[0].instance_id)
        # queue.put(args[0].instance_id)
        return func(*args, **kwargs)
    return wrapper

class Params:

    instance_id = '0000'

    def __init__(self, instance_id, param_dict):
        self.__dict__ = param_dict
        self.set_id(instance_id)

    @classmethod
    def set_id(cls, id):
        cls.instance_id = id
    # def __getitem__(self, item):
    #     return self.__param[item]
    #
    # @watch_instance_param
    # def __setitem__(self, key, value, instance_id=instance_id):
    #     self.__param[key] = value
    #

    def __getattr__(self, item):
        return self.__dict__[item]

    @watch_instance_param
    def __setattr__(self, key, value, instance_id=instance_id):
        self.__dict__[key] = value

    def __repr__(self):
        return json.dumps(self.__dict__)




if __name__ == '__main__':

    # @watch_instance_param(1234)
    # def main():
    #     print('hhaha')
    #
    # main()
    param = Params('1111', {'a': 'sss', 'v':'eee'})
    param.a = 3
    param.v = 'ssssssss'
    print(param.a)
    print(param.__dict__)
    print(param.v)
    # t = Test({'a': 'sss', 'v':'eee'})
    # print(t.dictp)