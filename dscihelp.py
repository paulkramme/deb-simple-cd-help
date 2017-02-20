#!/usr/bin/python3

# ARGS:  path_to_apikey

import sys

def main():
	print("DEB-SIMPLE CI HELPER")
	
	apipath = sys.argv[2]
	apitoken = ""
	with open(path, "r") as f:
		apitoken = f.read()
	apitoken = apitoken.rstrip()

	url = sys.argv[1]
	url.replace("API_PLACEHOLDER", apitoken)
	os.system(url)

if __name__ == "__main__":
	main()

