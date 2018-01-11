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
        pass