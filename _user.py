#  Copyright (c) 2024.
# 所有if True均为折叠点,并无实际作用
import socket
import time

from _path import user_log as logging
from jsons import r_json, w_json

if True:
    logging.name = 'user'
    logging.info("Initialize Module:user")

# 读取配置文件
if True:
    default_configure = {
        'setblocking': False,
        'IPv4': ('192.168.10.1', 8080),
        'user input': False,
    }
    logging.info('configure up')
    configure = r_json('user_configure')
    if not configure:
        logging.info('no configure,Use default configure')
        w_json(default_configure, 'user_configure')
        configure = default_configure
    else:
        for k in default_configure:
            if k not in configure.keys():
                logging.info('Incomplete configure,Use default configure')
                w_json(default_configure, 'user_configure')
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
        configure['IPv4'] = (_t0, _t1)
        logging.info(f'sys ip:{configure['IPv4']}')
    else:
        logging.info('configure ip&port')

    while True:
        try:
            logging.info('尝试握手')
            _udp.sendto('handshake'.encode('utf-8'), configure['IPv4'])
            print('已发送连接信息,请等待')
            time.sleep(3)
            _message = _udp.recvfrom(1024)[0].decode("utf-8")
            if _message == 'handshake':
                logging.info('握手成功')
                print('握手成功')
                break
            else:
                logging.error(f'服务器返回了错误的消息\\{_message}')
                print(f'服务器返回了如下消息\n{_message}')
        except BlockingIOError:
            logging.info('握手失败')
            if input('无法连接到服务器,输入exit退出,或直接敲击回车重试') == 'exit':
                logging.info('exit')
                exit(0)
        except Exception as e:
            logging.error(e)
    logging.info('configure:UDP\\ok')

# 宣布模块配置完成
logging.info('sys ok and Enter the main body of UDP communication')


# 主体
while True:
    try:
        _message = input('按下回车发送')
        logging.info(f'>>> message:{_message}')
        _udp.sendto(_message.encode('utf-8'), configure['IPv4'])
        time.sleep(1)
        _message = _udp.recvfrom(10240)
        logging.info(f'<<< message:{_message}')
        print(_message[0].decode("utf-8"))
    except BlockingIOError:
        logging.info('未收到&超时')
        print('或许超时了?')
    except Exception as e:
        logging.error(f'\n{e}\n')
        print(e)
