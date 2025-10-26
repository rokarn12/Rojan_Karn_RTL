import os
import subprocess

def start_test():
	## Just run the given test Python script
	cmd = f"python3 tb/test_uart_rx.py"
	try:
		ret = subprocess.run(cmd, cwd="/workspace", shell=True, text=True, capture_output=True)
		## Print output of run command
		print("Test Output:")
		print(ret.stdout)
		
		## Trying to invoke AssertionError -> FAIL
		if "AssertionError" in ret.stderr:
			print("Grade: Failed")
		elif "Traceback" in ret.stderr:
			print("Grade: Failed")
		else:
			print("Grade: Passed")		

	### If test couldn't be run properly
	except subprocess.CalledProcessError as err:
		print("Error:", err)

if __name__ == "__main__":
	start_test()
