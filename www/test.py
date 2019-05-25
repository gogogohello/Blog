#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import orm
from models import User, Blog, Comment
import asyncio


async def init(loop):
	await orm.create_pool(loop=loop, host='localhost', port=3306, 
			user='root', password='Xmima624!', db='test')
	u = User(name='admin', email='admin@qq.com', passwd='123456', amdmin=True, image='about:blank')
	await u.save()
	r = await User.findAll()
	print(r)


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(init(loop))
	loop.run_forever()
