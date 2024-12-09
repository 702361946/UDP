#  Copyright (c)

import logging
import os

# 获取当前用户的AppData路径
appdata_path = os.path.expanduser('~\\AppData')

# 检查操作系统，Windows，拼接LocalLow路径
if os.name == 'nt':
    user_log_path = os.path.join(appdata_path, 'LocalLow\\702361946\\UDP\\user.log')
    sys_log_path = os.path.join(appdata_path, 'LocalLow\\702361946\\UDP\\sys.log')
    global_log_path = os.path.join(appdata_path, 'LocalLow\\702361946\\UDP\\global.log')
else:
    # 对于其他系统，可能没有LocalLow，自定义路径
    user_log_path = '.\\.log'
    sys_log_path = '.\\.log'
    global_log_path = '.\\.log'

# 目录补全
os.makedirs(os.path.dirname(user_log_path), exist_ok=True)
os.makedirs(os.path.dirname(sys_log_path), exist_ok=True)
os.makedirs(os.path.dirname(global_log_path), exist_ok=True)

if True:
    sys_log = logging.getLogger('sys_log')
    sys_log.setLevel(logging.DEBUG)
    sys_handler = logging.FileHandler(sys_log_path, mode='w', encoding='UTF-8')
    sys_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    sys_handler.setFormatter(sys_formatter)
    sys_log.addHandler(sys_handler)

if True:
    user_log = logging.getLogger('user_log')
    user_log.setLevel(logging.DEBUG)
    user_handler = logging.FileHandler(user_log_path, mode='w', encoding='UTF-8')
    user_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    user_handler.setFormatter(user_formatter)
    user_log.addHandler(user_handler)

if True:
    global_log = logging.getLogger('global_log')
    global_log.setLevel(logging.DEBUG)
    global_handler = logging.FileHandler(global_log_path, mode='w', encoding='UTF-8')
    global_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    global_handler.setFormatter(global_formatter)
    global_log.addHandler(global_handler)

sys_log.info('path ok and exit\n')
user_log.info('path ok and exit\n')
global_log.info('path ok and exit\n')
