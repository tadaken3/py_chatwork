#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse
import requests
import logging

def main():
    logger = get_logger()
    logger.info('start')
    psr = argparse.ArgumentParser()
    psr.add_argument('-a', '--apikey', default='#Your Chatwork API KEY')
    psr.add_argument('-r', '--roomid', default='Your Room ID')
    psr.add_argument('-m', '--message', default='貧弱！ 貧弱ゥ！')
    psr.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = psr.parse_args()
    
    ENDPOINT = 'https://api.chatwork.com/v2'
    
    post_message_url = '{}/rooms/{}/messages'.format(ENDPOINT, args.roomid)

    headers = { 'X-ChatWorkToken': args.apikey}
    params = { 'body': args.message }
    r = requests.post(post_message_url,
                        headers=headers,
                        params=params)
    if r.status_code != 200:
        logger.warning(r.text)
    logger.info('end')

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel('INFO')
    
    fh = logging.FileHandler('chatwork.log')
    logger.addHandler(fh)
    
    sh = logging.StreamHandler()
    logger.addHandler(sh)
    
    formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    return logger

if __name__ == '__main__':
    main()
