#!usr/bin/python
#coding: utf-8

import sys
sys.path.append('/Users/Paul/Applications/git/losemytime')
from ytsearch import RandomVideoBuilder


file_to_inspect = "resources/yt_eminem_search_result.html"

def page():
	with open(file_to_inspect,'r') as f:
		data = str(f.read())
		f.close()
		return data
	return None

def rvb():
	return RandomVideoBuilder([])	

def testSearchFirstElement():
	data = page()
	obj = rvb()

	expectedResult = ['ab9176Srb5Y', 'ZDXXi19_7iE', 'j5-yKhDd64s', 'S7cQ3b0iqLo', 'NlmezywdxPI', 'YVkUvmDQ3HY', '359na4NeaVA', 
	'ltg5dx4TpjU', 'wVZJkPefwf0', 'R9CY1l8Bc-c', 'eJO5HU_7_1w', 'fySaWH6qIVg', 
	'1wYNFfgrXTI', 'RSdKmX2BH7o', 'Kt_96bFMLAQ', 'tK9jX91XuT8']

	assert type(data) is str
	result = obj.parsePage(str(data))
	assert result == expectedResult

#<a href="/watch?v=359-a4NeaVA" class="ux-thumb-wrap yt-uix-sessionlink yt-uix-contextlink contains-addto "  data-sessionlink="ei=7N6PUrf8MKfD0QWo2IAY&amp;ved=CFIQwBs">    <span class="video-thumb  yt-thumb yt-thumb-185"
testSearchFirstElement()

