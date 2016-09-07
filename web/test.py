#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# import asyncio
# import web.orm as orm
# from web.models import User, Blog, Comment
#
#
# async def test(loop):
#     await orm.create_pool(loop=loop, user='www-data', password='www-data',db='awesome')
#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#     await u.save()
#     await orm.close_pool()
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()

import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data',db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()
    await orm.close_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()