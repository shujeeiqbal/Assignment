"""
Shujee Iqbal
BCSF14M541
System Programming
Task 4: Enter PID of a process to see its details.
"""

import psutil
import sys
import datetime

def processInfo(pid):
	if psutil.pid_exists(pid):
		p = psutil.Process(pid)
		print("Process ID: {0}".format(pid))
		print("Process name: {0}".format(p.name()))
		print("Process status: {0}".format(p.status()))
		print("Process parent ID: {0}".format(p.ppid()))
		print("Process parent name: {0}".format(p.parent()))
		print("Process creation time: {0}".format(datetime.datetime.fromtimestamp(p.create_time())))
		print("Files opened by the process: info {0}".format(p.open_files()))
		print("Memory info (bytes): {0}".format(p.memory_info()))
	else:
		print("PID {0} doesn't exist.".format(pid))
		
		
def main():
	for pid in (sys.argv[1:]):
		processInfo(int(pid))
		print("******************")

if __name__ == "__main__":
    main()
