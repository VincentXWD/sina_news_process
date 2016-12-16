# -*- coding: utf-8 -*-
import sys
import time
import datetime
import re
import os

RESULT_PATH = '/home/kirai/workspace/sina_news_process/result/'
CATALOG_PATH = '/home/kirai/workspace/sina_news_process/catalog/'
DISWORDED_NEWS_PATH = '/home/kirai/workspace/sina_news_process/disworded_news.txt'
SUB_PATH = ['biz_tech/', 'china/', 'culture/', 'ent/', 'sports/', 'world/']
PATH_FILE_NAME = 'path.snp'
TIME_REGEXP = re.compile('([\d]+)-([\d]+)-([\d]+) ([\d]+):([\d]+):([\d]+) GMT')
DISWORDED_NEWS = []

def get_time(raw):
	global TIME_REGEXP
	return map(int, TIME_REGEXP.findall(raw)[0])

def read_file(path):
	if not os.path.exists(path):
		print 'path : \''+ path + '\' not find.'
		return []
	content = ''
	try:
		with open(path, 'r') as fp:
			content += reduce(lambda x,y:x+y, fp)
	finally:
		fp.close()
	return content.split('\n')

def get_full_path():
	global CATALOG_PATH, SUB_PATH, PATH_FILE_NAME
	# 展开所有的path
	expand_path = map(lambda path:read_file(path),
									map(lambda path:CATALOG_PATH+path+PATH_FILE_NAME, SUB_PATH))
	# 去重，过滤空。expand_path[i]]表示第i个special coverage下的j个文件
	expand_path = map(lambda path:list(set(
		filter(lambda each:each!='', path))), expand_path)
	# 在文件里标注过subject了，所以直接zip下，降一维
	expand_path = reduce(lambda x, y: x+y, expand_path)
	return expand_path

def fmt_output(each):
	# subject
	# topic
	# time yy-mm-dd hh:mm:ss
	# content(不在此)
	return str(each[2][0])+'-'+str(each[2][1])+'-'+str(each[2][2])+' '+str(each[2][3])+':'+str(each[2][4])+':'+str(each[2][5]) + \
				 ' #### ' + each[0] + \
				 ' #### ' + each[1] + \
				 ' #### '

def process_all_file():
	file_path = get_full_path()
	# file_content[i][j]代表第i个文件第j行，每一个文件都是5行，分别是subject topic date content（最后一行是个空白）
	file_content = filter(lambda each:each!=[], map(read_file, file_path))
	# 处理时间，并按时间排序
	file_content = sorted(map(lambda each:[each[0],each[1],get_time(each[2]),each[3]], file_content),
												key=lambda each:each[2])
	file_content = map(fmt_output, file_content)
	DISWORDED_NEWS = read_file(DISWORDED_NEWS_PATH)
	final = zip(file_content, DISWORDED_NEWS)
	# redirect
	print len(final)
	for each in final:
		print each[0], each[1]

def write_file():
	fp = open(path, 'w')
	fp.write()
	fp.close()


def __main__(argv):
	process_all_file()

if __name__ == '__main__':
	__main__(sys.argv)
