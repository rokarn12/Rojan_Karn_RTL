#!/usr/bin/env python3
import os
import sys
import subprocess

def run_command(command, cwd="."):
	ret = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
	return ret.returncode, ret.stdout, ret.stderr

def grade():
	### Compiling RTL/testbench
	command = f"iverilog -o sim-op ./tb/uart_rx.v ./rtl/*.v"
	rc, out, err = run_command(command)
	if rc != 0:
		# compile failed, end
		print("Compile failed with err:", err)
		return 0

	### Run sim
    sim_cmd = f"vvp sim-op"
	rc, out, err = run_command(sim_cmd)
	if rc > 0:
		## sim failed, end
		print("Simulation failed with err:", err)
		return 0
	else:
		## sim passed, print output
		print("Sim Output:")
		print(out)

	# search for "PASS" in output
	if "PASS" in out:
		print("Grade: Passed")
		return 1
	else:
		print("Grade: Failed")
		return 0

if __name__ == "__main__":
	passed = grade()
	sys.exit(0 if passed else 1)
