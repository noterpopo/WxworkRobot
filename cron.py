#!/usr/bin/python
# -*- coding: UTF-8 -*-

from crontab import CronTab
cron_manager  = CronTab(user=True)
#替换自己的python文件路径
job = cron_manager.new(command='python3 路径 >> a.txt')
#这里填入定期的cron表达式
job.setall('0 8,12,13,17 * * *')
cron_manager.write()