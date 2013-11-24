
#!/usr/bin/python
# coding: utf-8

import sys
sys.path.append('/Users/Paul/Applications/git/losemytime')
from timer_decorator import timer

@timer(True)
def myFunction():
	print "a"

if __name__ == '__main__':
	print myFunction()