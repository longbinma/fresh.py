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
def refresh(device_type,*arg):
	print arg
def walk_device(device,device_file,url_file,*arg):
	if not arg:
		device_type=filter(str.isalpha,device)
		device_ip=filter(lambda ch: ch in '0123456789.',device)
		refresh(device_type,device_ip,url_file)
	else:
		device_ip=device
walk_device(top_device,device_file,url_file,"ignore")

