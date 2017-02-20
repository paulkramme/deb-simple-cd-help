#!/usr/bin/python3

import sys

def main():
	print("DEB-SIMPLE CI HELPER")
	path = sys.argv[1]
	with open(path, "r") as f:
		apitoken = f.read()
		apitoken = apitoken.rstrip()
		print(apitoken)

if __name__ == "__main__":
	main()

