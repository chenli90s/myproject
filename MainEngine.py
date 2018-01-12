# coding: utf-8
from EventEngine import EventEngine, Event
from EventManage import EventManage
from algoInstanceManage import AlgoInstanceManage
from wrapper import Params


class MainEngine:

    def __init__(self):
        self.algoInstanceManage = AlgoInstanceManage()
        self._event_engine = EventEngine(self.algoInstanceManage)
        self._event_manage = EventManage(self._event_engine)

    def start(self):
        self._event_engine.start()
        self._event_manage.start()

    def stop(self):
        self._event_engine.stop()
        self._event_manage.stop()

    def create_algo_instance(self, event_type, param_dict):
        self._event_engine.put(event=Event(event_type, params=param_dict))

    def add_algo(self, algo):
        """
        加载算法程序
        :param algo:
        :return:
        """
        self._event_engine.register(algo)
        if algo.config.launch_type == 'unactive':
            self._event_manage.add_Config(algo.config)

    def remove_algo(self, algo):
        """
        移除算法程序
        :param algo:
        :return:
        """
        self._event_engine.unregister(algo)
        if algo.config.launch_type == 'unactive':
            self._event_manage.remove_Config(algo.config)

    def deploy_algo(self):
        pass

if __name__ == '__main__':
    from BaseConfig import BaseConfig
    from BaseAlgo import BaseAlgo
    from algo import Algo
    mainengin = MainEngine()
    mainengin.start()
    algo = Algo(BaseAlgo, BaseConfig)
    mainengin.add_algo(algo)
    mainengin.create_algo_instance('test_event', {'id':5,'hello': 'world', 'haha': 'heihei'})

    for i in xrange(100):
        mainengin.create_algo_instance('test_event', {'id':5, i*5: i, i*2: 'saa'})

    # mainengin.stop()


