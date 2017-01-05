import sys
import subprocess
import os 
import signal

if len(sys.argv) == 1:
	
	print("kill_process: Error - No arguments given")
	sys.exit()

elif len(sys.argv) > 2:
	
	print("kill_process: Error - Too many arguments given") 
	sys.exit() 

elif len(sys.argv) == 2:

	processToKill = sys.argv[1]

	try: 			
		processIDs = subprocess.check_output(["pgrep", processToKill])

	except subprocess.CalledProcessError:
		print("kill_process: Error - No processes running with given name")

	processIDs = processIDs.split()
		
	for processID in processIDs:	
		os.kill(int(processID), signal.SIGKILL)

	sys.exit()
