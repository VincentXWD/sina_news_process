import sys
import os

ROOT_PATH = '/home/kirai/workspace/sina_news_process/result/'
SUB_PATH = ['biz_tech/', 'china/', 'culture/', 'ent/', 'sports/', 'world/']

def __main__(argv):
	global ROOT_PATH, SUB_PATH
	SUBJECT_PATH = [filter(lambda path:path!='suburls.usns', group)
									for group in map(lambda path:os.listdir(path),
										 map(lambda sub:ROOT_PATH+sub, SUB_PATH))]

	for i in range(0, len(SUB_PATH)):
		print SUB_PATH[i][:-1]
		for topic in SUBJECT_PATH[i]:
			print topic

if __name__ == '__main__':
	__main__(sys.argv)