# coding: utf-8
import uuid
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler
from wrapper import watch_instance_param

class Params:

    instance_id = '0000'

    def __init__(self, instance_id, param_dict):
        self.__param = param_dict
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
        return self.__param[item]

    @watch_instance_param
    def __setattr__(self, key, value, instance_id=instance_id):
        try:
            self.__param[key] = value
        except:
            pass


class AlgoInstanceManage:


    def __init__(self):
        # 运行实例容器
        self._instance_task = {}
        self._scheduler = BackgroundScheduler()

    def add_algo_instance(self, algo, event):
        """
        开启实例
        :param algo:
        :param event:
        :return:
        """
        alog_instance_id = str(uuid.uuid1())
        event.instance_id = alog_instance_id

        if algo.config.event_type == 'scheduler':
            cron_list = algo.config.cron.split('')
            self._scheduler.add_job(algo.run, args=event, trigger='cron', minute=cron_list[0],
                                          hour=cron_list[1],
                                          day=cron_list[2],
                                          month=cron_list[3],
                                          day_of_week=cron_list[4], misfire_grace_time=60, coalesce=True,
                                          id=alog_instance_id)
            self._instance_task[alog_instance_id] = event
        else:
            t = Thread(target=algo.run, args=(event, ))
            t.start()
            event.t = t
            self._instance_task[alog_instance_id] = event

    def remove_algo_instance(self, instance_id):
        """
        关停实例
        :param instance_id:
        :return:
        """
        event = self._instance_task[instance_id]
        if event.type == 'scheduler':
            self._scheduler.remove_job(instance_id)
        else:
            event.t.join()


if __name__ == '__main__':
    item = Params('123', {'a':3, 'b':5})
    # item2 = Params('125', {'a':3, 'b':5})
    # item.set_attr('a', 8)
    # item['a'] = 'ssssss'
    # item2['b'] = 'eeeee'
    item.abc = 'sss'
    # print(item['a'])