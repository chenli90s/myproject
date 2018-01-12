# encoding: UTF-8
from Queue import Queue, Empty
from threading import Thread
from collections import defaultdict

class Event:

    def __init__(self, type, *args, **kwargs):
        self.type = type
        self.args = args
        self.kwargs = kwargs


    def __getattr__(self, item):
        return self.kwargs[item]



class EventEngine:

    def __init__(self, algo_Instance_manage):
        # 事件队列
        self.__queue = Queue()
        # 事件轮询器开关
        self.__active = False
        # 事件引擎线程
        self.__thread = Thread(target=self.__run)
        # 处理器字典
        self.__handlers = defaultdict(list)
        # 算法实例管理
        self._algo_Instance_manage = algo_Instance_manage


    def __run(self):
        """
        运行引擎
        :return:
        """
        while self.__active:
            try:
                event = self.__queue.get(block=True, timeout=1)
                self.__process(event)
            except Empty:
                pass

    def __process(self, event):
        """
        处理事件
        :param event:
        :return:
        """
        if event.type in self.__handlers:
            # [handler(event) for handler in self.__handlers[event.type]]
            for handler in self.__handlers[event.type]:
                self._algo_Instance_manage.add_algo_instance(handler, event)

    def start(self):
        """
        引擎启动
        :return:
        """
        self.__active = True
        self.__thread.start()

    def stop(self):
        """
        停止引擎
        :return:
        """
        self.__active = False
        self.__thread.join()

    def register(self, algo):
        """
        注册事件处理函数
        :param algo:
        :return:
        """
        handlerList = self.__handlers[algo.type]

        if algo not in handlerList:
            handlerList.append(algo)

    def unregister(self, algo):
        """
        注销事件处理监听
        :param algo:
        :return:
        """
        handlerList = self.__handlers[algo.type]

        if algo in handlerList:
            handlerList.remove(algo)

        if not handlerList:
            del self.__handlers[algo]

    def put(self, event):
        """
        添加事件
        :param event:
        :return:
        """
        self.__queue.put(event)


def test1(event):
    print('开始执行', event.type)
    for i in range(10,1000000):
        for j in range(1,10000000):
            x = i**j
            # print(x)

def test2(event):
    print('开始执行', event.type)
    c = 10000000
    i = 0
    while i < c:
        m = c*i
        i += 1
        print(m)



if __name__ == '__main__':
    ee = EventEngine()
    ee.start()
    ee.register('test1', test1)
    ee.register('test2', test2)
    # while True:
    #     # print('-')
    #     ee.put(Event('test1'))
    #     ee.put(Event('test2'))
    ee.put(Event('test1'))
    ee.put(Event('test2'))


