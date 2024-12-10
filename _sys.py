#  Copyright (c) 2024.
# 所有if True均为折叠点,并无实际作用
import socket

from _sys_message import *

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
    if message in r_message.keys():
        if type(r_message[message]).__name__ == 'str':
            logging.info(f'>>> message:{r_message[message]},ip:{_ip}')
            _udp.sendto(r_message[message].encode('utf-8'), _ip)
        else:
            logging.info(f'执行方法:{message}')
            _udp.sendto(r_message[message]().encode('utf-8'), _ip)
    else:
        _udp.sendto('未知指令'.encode('utf-8'), _ip)
        logging.info(f'未知指令:{message}')

# 主体
while True:
    try:
        _message = _udp.recvfrom(10240)
        print(_message)
        logging.info(f"<<< {_message}")
        udp_message(_message[0].decode("utf-8"), _message[1])
    except BlockingIOError:
        pass
    except Exception as e:
        logging.error(f'\n{e}\n')
        print(e)
