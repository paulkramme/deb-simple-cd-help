#!/usr/bin/python3

# ARGS:  path_to_apikey

import sys
import os

def main():	
	if len(sys.argv) < 3:
		print("""USAGE: url path-to-api-file
	Add a file to a secure location on your CD system.
	In this file there should only be the api token, NOTHING ELSE.
	Replace the API token in the URL with API_TOKEN.
	This program will replace the API token with the real one.""")
		sys.exit()

	apipath = sys.argv[2]
	apitoken = ""
	with open(path, "r") as f:
		apitoken = f.read()
	apitoken = apitoken.rstrip()

	url = sys.argv[1]
	url.replace("API_TOKEN", apitoken)
	os.system(url)

if __name__ == "__main__":
	main()

