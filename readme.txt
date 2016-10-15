### Checkpoint 1 ###

1. the program should be able to run by type "./(filename) -o (output_filename.txt/jpg/etc.) (http to download)"
2. Sometimes the website is not portocol, so we have to find the PORT of the website by using "parse"
3. We want to seperate header from the data, so we will know the content-length (to check that we do not lose any data)
4. Once we got the content-length we could write file and keep track where we are.
5. if no. of byte of the received file equal to the content-length, we did not leave any data behind.
6. DONE


### CHECKPOINT 2 ###

1. I rearranged my code to be in 'Class' and put many methods inside the function.
2. First of all, the code must check wheather it needs to resume by checking if the output filename and the file 'information.txt' exist. 
	2.1 If the output filename and the file 'information.txt' does not exist.
		- Connect the socket and send the request.
		- Find the header first by receive the data until the '\r\n\r\n' has found. There maybe a case that the header we have received conclude some data remaining, so the text file will be firstly wrote here. 
		- Find the "ETag", "Last-Modified", and "Content-Length"
		- Find the content length to make sure that the data has downloaded completely. By using .split()
		- Create the file called 'information.txt' to save the "ETag", "LastModified", and "Content-Length"
		- Start to write file using 'try....except'. In case there is no except, the file 'information.txt' will be removed.
		- Done
	2.2 If the output filename and the file 'information.txt' exist.
		- Send the request by using RANGE.
		- Find the header by using the same logic like the previous one.
		- Find the "ETag", "Last-Modified", and "Content-Length" and compare with the information in the file 'information.txt'
		- Continue writing the data until finish
		- Done
