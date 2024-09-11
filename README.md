# SERVER_startup
Simple server that simulates multiple ssh - type connections on the same PC and allows multiple users to get and upload files, run commands, etc

Each client is handled by a different thread on the main server which allows less clients but fast parallel communications, file transffer, etc

So far configured on local host for testing, allows 4 maximum connections

Only messaging implementd so far
