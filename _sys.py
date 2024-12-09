#  Copyright (c) 2024.
# 所有if True均为折叠点,并无实际作用
import socket

from jsons import r_json, w_json
from _path import sys_log as logging

# 配置日志
if True:
    logging.name = 'sys'
    logging.info("Initialize Module:sys")

# 读取配置文件
if True:
    if True: # configure
        default_configure = {
            'setblocking': False,
            'IPv4': ('192.168.10.1', 8080),
            'user input': False
        }
        logging.info('configure up')
        configure = r_json('sys_configure')
        if not configure:
            logging.info('no configure,Use default configure')
            w_json(default_configure, 'sys_configure')
            configure = default_configure
        else:
            for k in default_configure:
                if k not in configure.keys():
                    logging.info('Incomplete configure,Use default configure')
                    w_json(default_configure, 'sys_configure')
                    configure = default_configure
                    break
        # 将ipv4变为数组避免报错
        configure['IPv4'] = tuple(configure['IPv4'])

    # 消息应对策略
    if True:
        logging.info('读取消息应对策略')
        default_r_message = {
            'handshake': 'handshake'
        }
        r_message = r_json('message')
        if not r_message:
            logging.info('未找到消息应对策略,启用默认')
            w_json(default_r_message, 'message')
            r_message = default_r_message
        else:
            for k in default_r_message.keys():
                if k not in r_message.keys():
                    logging.info('缺少默认键,启用默认配置,不覆盖文件')
                    print('请检查消息配置文件')
                    r_message = default_r_message
                    break
        logging.info('读取完毕')

    logging.info('configure ok')

# UDP配置
if True:
    logging.info('configure:UDP\\start')
    _udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    _udp.setblocking(configure['setblocking'])
    if configure['user input']:
        logging.info('user input ip&port')
        print('no try')
        _t0 = input('ip')
        _t1 = int(input('port'))
        _udp.bind((_t0, _t1))
        logging.info(f'bind:{(_t0, _t1)}')
    else:
        logging.info('configure ip&port')
        _udp.bind(configure['IPv4'])
    logging.info('configure:UDP\\ok')

# 宣布模块配置完成
logging.info('sys ok and Enter the main body of UDP communication\n')


def udp_message(message: str, _ip: tuple[str, int]):
    try:
        logging.info(f'message:{r_message[message]},ip:{_ip}')
        _udp.sendto(r_message[message].encode('utf-8'), _ip)
    except Exception as _e:
        _udp.sendto('未知指令'.encode('utf-8'), _ip)
        logging.error(_e)
        print(_e)

# 主体
while True:
    try:
        _message = _udp.recvfrom(10240)
        print(_message)
        logging.info(_message)
        udp_message(_message[0].decode("utf-8"), _message[1])
    except BlockingIOError:
        pass
    except Exception as e:
        logging.error(f'\n{e}\n')
        print(e)
