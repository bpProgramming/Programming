bhishan tips to build and run c file with fitsio header
-------------------------------------------------------
1. first go the directory:

2. to build the program:
gcc -o output_name  fileName.c -O2 -lcfitsio -lm -pthread   (or) 
gcc 				fileName.c -02 -lcfitsio -lm

e.g1:  gcc -o a a.c -O2 -lcfitsio -lm -pthread 
e.g2:  gcc 		a.c -O2 -lcfitsio -lm

2. to run the program

eg1:  ./a 		in.fits
eg2:  ./a.out 	in.fits
