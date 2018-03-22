#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import getopt
import string
from subprocess import check_output


def logo():
	print " ____  _     _____ _ _     _                _     "
	print "/ ___|| |_  |___ /| | |___| |__   ___   ___| | __  "
	print "\___ \| '_ \  |_ \| | / __| '_ \ / _ \ / __| |/ / "
	print " ___) | | | |___) | | \__ \ | | | (_) | (__|   <  "
	print "|____/|_| |_|____/|_|_|___/_| |_|\___/ \___|_|\_\  \n"
	print "           <<<<<<Coded by T3jv1l>>>>>>>>       "
	print "      <<<<<<Contact for bug t3jv1l@gmail.com>>>>>> \n  "
	print "            Usage:  [argument] [file] [argument]:" 
	print "      -f    --file     The ASM code filename"
	print "      -s    --show     Show shellcode"
	print "      -i    --intel    Syntax"




def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "f:si", ["file=", "show","intel"])

	except getopt.GetoptError as err:
		print(str(err))
		usage()
		sys.exit(2)
	objfile = None
	shellcode = None
	code = None
	syntax = "intel"
	format = None
	for o, a in opts:
		if o in ("-i", "--intel"):
			syntax = "intel"
		elif o in ("-f", "--file"):
			objfile = a
			if os.path.exists(objfile):
				shellcode, code = parse(objfile, syntax, format)
			else:
				print("[+] File dosen't existed")
				sys.exit(1)
		elif o in ("-s", "--show"):
			if objfile is not None:
				if format is  None:
					print("[+] Shellcode =")
					shellcode = re.sub(
								"(.{32})", "\\1 \n",
								shellcode, 0, re.DOTALL)
					
					print(shellcode[:-1])
					print("\n[+] We have a shellcode")
				else:
					shellcode = re.sub(
								"(.{32})", "\\1\n",
								shellcode, 0, re.DOTALL)
					print(shellcode[:-1])
		else:
			assert False, "unhandled option"

def parse(obj, syntax, format):
	objdump = ['objdump', '-d', '-M', syntax, obj]

	lines = check_output(objdump)
	lines = lines.split(b'Disassembly of section')[1]
	lines = lines.split(b'\n')[3:]

	shellcode = ""
	code = []

	for l in lines:
		l = l.strip()

		tabs = l.split(b'\t')
		if (len(tabs) < 2):
			continue
		bytes = tabs[1].strip()

		instruction = "."
		if (len(tabs) == 3):
			instruction = tabs[2].strip().decode("utf-8")

		bytes = bytes.split(b' ')
		sh3llshock = ""
		for byte in bytes:
			sh3llshock += "\\x" + byte.decode("utf-8")

		shellcode += sh3llshock
		if format is  None:
			show_shell =  (32, '"'+sh3llshock+'"', instruction)
		else:
			show_shell =  (32, '"'+sh3llshock+'"', instruction)
		code.append(show_shell)

	return shellcode, code


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		logo()
	else:
		 main()

	


	

