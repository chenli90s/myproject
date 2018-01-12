# encoding: utf-8


# class CycleParam:
#
#     def __init__(self, startTime, interval, endTime):
#         # 开始时间
#         startTime = None
#         # 指定运行的周期 年:Y 月:m 日:d 小时:H 分钟: M 秒:S 毫秒:MS
#         interval = ''
#         # 结束时间
#         endTime = None

class BaseConfig:


    # 触发类型
    launch_type = 'active'

    # 设定事件类型
    event_type = 'test_event'
    # 定时任务触发时间
    timer = '2018-01-10 18:04:34'
    # 运行周期
    """
    Minute 每个小时的第几分钟执行该任务
    Hour 每天的第几个小时执行该任务
    Day 每月的第几天执行该任务
    Month 每年的第几个月执行该任务
    DayOfWeek 每周的第几天执行该任务，0表示周日
    """
    cycleParam = '*/1 * * * *'
    endTime = '2018-01-11 18:04:34'


    def is_active(self):
        """
        被动触发的条件，如果满足执行的条件，返回一组算法需要的参数
        :return:
        """
        pass

    def get_data(self):
        """
        当算法程序运行之前会被调用，返回的值传入算法运行方法里
        :return:
        """
        print('get_data', self.event_type)
        return 'data'

    def process_result(self, result):
        """
        处理算法程序产生的结果
        :param result:
        :return:
        """
        print('process_result',result)


