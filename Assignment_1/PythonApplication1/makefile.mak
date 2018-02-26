all:	assignment

assignment:	main.o ciphers.o
	python main.o ciphers.o -o main

main.o:	main.py
	python main.py 

ciphers.o:	ciphers.py
	python ciphers.py

clean:
	rm *.o assignment