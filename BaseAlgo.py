# coding: utf-8


class BaseAlgo:

    def init(self, param):
        self.param = param


    def run(self, data):
        n = 0
        for i in xrange(1000):
            if i/7 == 0:
                self.param.id = i
            for j in xrange(1000):
                n += i*j
        return n

    def destory(self,event):
        print('destory', self.param, event.instance_id)
