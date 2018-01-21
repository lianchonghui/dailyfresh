#!/usr/bin/env python
import os
import sys

'''
读取主app下的setting配置文件
获取命令行参数
'''
if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
