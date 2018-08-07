#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Rick'


'url handlers'


import re, time, json, logging, hashlib, base64, asyncio


from coroweb import get, post


from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
	summary = 'tree命令可以以树形结构显示文件目录结构，它非常适合于我们给别人介绍我们的文件目录的组成框架，同时该命令使用适当的参数也可以将命令结果输出到文本文件中。'	
	blogs = [
		Blog(id='1', name='编码', summary=summary, created_at=time.time()-120),
		Blog(id='1', name='读书', summary=summary, created_at=time.time()-360),
		Blog(id='1', name='机器学习', summary=summary, created_at=time.time()-720),
		Blog(id='1', name='Deep learning', summary=summary, created_at=time.time()-1020)
	]
	return {
		'__template__': 'blogs.html',
		'blogs': blogs
	}
