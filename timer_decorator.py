#!/usr/bin/python
# coding: utf-8

import time
import math

def format(t):
	return math.floor(t*1000)/1000

def timer(format_value = False): 

	def timer_func(func):

		def execute(self = None, *args):
			startTime = time.time()
			if args:
				if self != None:
					func(self, args)
				else:
					func(args)
			else:
				if self != None:
					func(self)
				else:
					func()

			t = time.time() - startTime
			if format_value:
				return format(t)
			else:
				return t

		return execute

	return timer_func
