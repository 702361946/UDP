#  Copyright (c)
import json
import os

from _path import global_log as logging

os.makedirs('.\\json', exist_ok=True)

if True:
    logging.name = 'jsons'
    logging.info("Initialize Module:jsons")

def w_json(a, name: str, encoding: str = 'utf-8'):
    logging.info(f'w_json\\name:{name}\n{a}')
    try:
        with open(f'.\\json\\{name}.json', 'w+', encoding=encoding) as f:
            json.dump(a, f, indent=4, ensure_ascii=False)
            return True

    except Exception as e:
        logging.error(e)
        # print(e)
        return False


def r_json(name: str, encoding: str = 'utf-8'):
    logging.info(f'r_json\\name:{name}')
    try:
        with open(f'.\\json\\{name}.json', 'r+', encoding=encoding) as f:
            a = json.load(f)
            return a

    except Exception as e:
        logging.error(e)
        # print(e)
        return None

logging.info('json ok and exit\n')
