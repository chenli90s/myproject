# coding: utf-8
from alogEngine import EventEngine,Event
from EventManage import EventManage


class MainEngine:

    def __init__(self):
        self._event_engine = EventEngine()
        self._event_manage = EventManage(self._event_engine)

    def start(self):
        self._event_engine.start()
        self._event_manage.start()


    def add_algo(self, algo):
        """
        添加算法程序
        :param algo:
        :return:
        """
        self._event_engine.register(algo)
        self._event_manage.add_Config(algo.config)


    def remove_algo(self, algo):
        """
        移除算法程序
        :param algo:
        :return:
        """
        self._event_engine.unregister(algo)
        self._event_manage.remove_Config(algo.config)

