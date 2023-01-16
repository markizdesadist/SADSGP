from loguru import logger
import os
import sys

info_path = os.path.abspath(os.path.join('..', 'logs', 'log_{time:DD_MM_YY}.log'))
warning_path = os.path.abspath(os.path.join('..', 'logs', 'warning', 'logs', 'log_{time:DD_MM_YY}.log'))
sys.path.append(info_path)
user = os.getlogin()

logger.add(
    info_path,
    level='INFO',
    format='[{time:DD-MM-YY HH:mm}] | {level}\t| {name}:<{module}>: (line: {line}) |-> : ' + user + ' : {message}',
    rotation='17:00',
    retention='7 days',
    compression='zip',
    enqueue=True,
    encoding='utf-8'
)
logger.add(
    warning_path,
    level='WARNING',
    format='[{time:DD-MM-YY HH:mm}] | {level}\t| {name}:<{module}>: (line: {line}) |-> : ' + user + ' : {message}',
    rotation='17:00',
    retention='20 days',
    compression='zip',
    enqueue=True,
    encoding='utf-8'
)
if __name__ == '__main__':
    # logger.warning('error')
    logger.info('info')
    print(info_path)
