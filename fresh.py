#!/bin/env  python
import datetime
import sys
device_file=sys.argv[1]
url_file=sys.argv[2]
task_type=sys.argv[3]
task_id=sys.argv[4]
top_device=sys.argv[5]
url_type=sys.argv[6]
def log():
	f=open('/tmp/test','a')
	now=datetime.datetime.now()
	otherStyleTime=now.strftime("%Y-%m-%d %H:%M:%S")
	f.write(otherStyleTime + "\r\n")
	f.close()
def walk_device():
	if not ignore_current.strip():
		print 'ignore_current is null'
	print device
	print ignore_current
walk_device(top_device,device_file,url_file)
