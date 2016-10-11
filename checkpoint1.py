
#!/usr/bin/env python

import socket as skt
import sys
from urlparse import urlparse
import time

servName = sys.argv[-1]
filename = sys.argv[-2]
# servName = url.netloc+url.path
serv  = urlparse(servName).hostname
p = urlparse(servName).path
port = urlparse(servName)
print port

servPort = 8080

def make_http_request(host, obj):
	NL = "\r\n"
	return ("GET {o} HTTP/1.1" + NL + "Host: {s}" + NL + NL).format(o=obj, s=host)

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
clientSocket.connect((serv, servPort))
request_str = make_http_request(serv, p)

clientSocket.send(request_str)
print "SERVER IS READY..."

f = open(filename , 'wb')



def findContentLength(info):
	a = info.split()
	if "Content-Length:" in a:
		b = a.index("Content-Length:") + 1
		return a[b]
	else:
		writeFileWithoutContent();
		f.close()
		clientSocket.close()

# start1 = time.time()

# count = 0
while True:

	data_received = clientSocket.recv(1024)
	loading = ""
	loading += data_received

	if "\r\n\r\n" in loading:
		header, remaining_data = loading.split("\r\n\r\n")
		f.write(remaining_data)
		findLength = findContentLength(header)
		break
# end1 = time.time()

# time_taken1 = end1 - start1
# print total, "<<<<"
# print "total_count",total_count

# start2 = time.time()

def writeFileWithoutContent():
	data_received3 = clientSocket.recv(8192)
	while data_received3:
		f.write(data_received3)
		data_received3 = clientSocket.recv(8192)


def writeFileWithContent(remaining_data1, findLength1):
	total = 0
	total = len(remaining_data)
	while total<int(findLength):
		data_received2 = clientSocket.recv(8192)
		f.write(data_received2)
		total += len(data_received2)
		# print int(findLength) - total
	f.close()
	clientSocket.close()

writeFileWithContent(remaining_data, findLength)

# end2 = time.time()

# time_taken2 = end2 - start2

# print "time_taken1:", time_taken1
# print "time_taken2:", time_taken2




print "DONE"

