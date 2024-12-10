#  Copyright (c) 2024.
import sys

from _path import sys_log as logging
from jsons import r_json, w_json

if True:
    logging.name = 'sys_message'
    logging.info('Initialize Module:sys_message')

# 全局方法
def sys_exit(message: str = ''):
    logging.info(f'sys_exit message:{message}')
    sys.exit()


def r_help() -> str:
    logging.info('读取帮助文件')
    _d = '发送sys_exit关闭服务器'
    _r = r_json('sys_help')
    if not _r:
        logging.info('未找到帮助文件,启用默认帮助')
        _r = _d
        w_json(_d, 'sys_help')

    logging.info(f'读取完毕,内容如下\n{_r}')

    return _r


_m = {
    'sys_exit': lambda: sys_exit(),
    'r_help': lambda: r_help()
}

# 消息应对策略
if True:
    logging.info('读取消息应对策略')
    default_r_message = {
        'handshake': 'handshake',
        'help': r_help(),
        'sys_exit': 'm:sys_exit'
    }
    r_message = r_json('message')
    if not r_message:
        logging.info('未找到消息应对策略,启用默认')
        w_json(default_r_message, 'message')
        r_message = default_r_message
    else:
        for k in default_r_message.keys():
            if k not in r_message.keys():
                logging.info('缺少默认键,启用默认配置,覆盖文件')
                r_message = default_r_message
                w_json(default_r_message, 'message')
                break

    logging.info('开启方法转换')
    for k in r_message.keys():
        if r_message[k][0:2] == 'm:':
            if r_message[k][2:len(r_message[k])] in _m.keys():
                logging.info(f'方法{r_message[k][2:len(r_message[k])]}')
                r_message[k] = _m[r_message[k][2:len(r_message[k])]]
            else:
                logging.info(f'未知方法:{r_message[k][2:len(r_message[k])]}')
    logging.info('结束转换')

    logging.info('读取完毕')

logging.info('sys_message ok and exit\n')
