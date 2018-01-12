# coding: utf-8
from BaseConfig import BaseConfig
from threading import Thread
from EventEngine import Event
import pytz

tz = pytz.timezone("Asia/Shanghai")


class EventManage:

    def __init__(self, event_engine):
        self.__event_engine = event_engine
        # 主动触发事件容器
        self.__configs = {}
        # 定时器事件触发容器
        self.__timer = []
        # 是否开启轮询事件
        self.is_active = False
        # 主动触发轮询线程
        self._active_thread = Thread(target=self._active_run)
        # 定时任务触发线程
        # self._timer_thread = Thread(target=self._timer_run())

    def add_Config(self, algo_config):
        """
        添加配置类
        :param algo_config:
        :return:
        """
        # if algo_config.event_type == 'timer':
        #     self.__timer.append(algo_config)
        #     return

        if algo_config.event_type in self.__configs:
            self.__configs[algo_config.event_type].count += 1
        else:
            algo_config.count = 1
            self.__configs[algo_config.event_type] = algo_config

    def remove_Config(self, algo_config):
        """
        移除配置类
        :param algo_config:
        :return:
        """
        if algo_config.event_type in self.__configs:
            if algo_config.count > 1:
                algo_config.count -= 1
            else:
                del self.__configs[algo_config.event_type]

    def _active_run(self):
        """
        轮询事件是否触发
        :return:
        """
        while self.is_active:
            for _, config in self.__configs.iteritems():
                params = config.is_active()
                if params:
                    event = Event(type=config.event_type, params=params)
                    self.__event_engine.put(event)

    # def _timer_run(self):
    #     """
    #     轮询定时任务
    #     :return:
    #     """
    #     while self.is_active:
    #         for config in self.__timer:
    #             tm = time.strptime(config.timer, "%Y-%m-%d %H:%M:%S")
    #             if time.mktime(tm) < time.time():
    #                 self.__event_engine.put(Event(type=config.event_type, config=config))

    def start(self):
        self.is_active = True
        self._active_thread.start()
        # self._timer_thread.start()

    def stop(self):
        self.is_active = False
        self._active_thread.join()
        # self._timer_thread.join()


if __name__ == '__main__':
    pass
