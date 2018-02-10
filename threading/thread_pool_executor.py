#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 2/10/18.

import concurrent
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor

import requests


def get_content():
    resp = requests.get('http://whatthecommit.com/index.txt')
    return resp.content.decode()


def main():
    with ThreadPoolExecutor(max_workers = 10) as pool:
        futures = {pool.submit(get_content): i for i in range(1000)}
        for future in concurrent.futures.as_completed(futures):
            n = futures[future]
            try:
                data = future.result()
            except Exception as exc:
                print("task: {} exception: {}".format(n, exc))
            else:
                print("task: {} data: {}".format(n, data))


if __name__ == '__main__':
    main()
