import numpy as np
def main():
	i = 0
	x = 119.0
	for i in range(120):        
		if ((i%2)==0):       #if i is even
			x += 3 
		else:
			x -= 5.0
	s = "%3.2e" % x
	        			#make a string that shows x with scientific notation, the 3.2 says that you want three numbers in total with 2 after the decimal place and the 'e' says to put the number in scientific notation
	print(s)
	
# now the rest of the program
if __name__ == "__main__":         #something that makes the program run
	main()                         # if the main() fxn exists, run it
	