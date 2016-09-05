#!/usr/bin/env python3
# -*- coding : utf-8 -*-


__author__ = 'huqingsong'


"""
async web application.
"""


import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web


def index(request):
    return web.Response(body=bytes('<h1>代码如诗</h1>', encoding='utf-8'),
                        headers={'Content-Type': 'text/html;charset=utf-8'})


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8888)
    logging.info('服务启动：http://127.0.0.1:8888……')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
