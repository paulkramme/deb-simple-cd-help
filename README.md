# deb-simple-ci-help
Helper script for deb-simples API token

## Usage
`dscdhelp.py <url> <path to api token file>`  

Replace the token in the URL with API_TOKEN. The program
will replace API_TOKEN with the token specified in the api file.
This tool is necessary if you want to Continuous Deliver your build 
packages to deb-simple server, without having to expose your API token, 
as the token will lie at a not accessible place at your build server.  

I recommend including the file into any CD project.

