1. the program should be able to run by type "./(filename) -o (output_filename.txt/jpg/etc.) (http to download)"
2. Sometimes the website is not portocol, so we have to find the PORT of the website by using "parse"
3. We want to seperate header from the data, so we will know the content-length (to check that we do not lose any data)
4. Once we got the content-length we could write file and keep track where we are.
5. if no. of byte of the received file equal to the content-length, we did not leave any data behind.

