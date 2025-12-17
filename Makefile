##
## EPITECH PROJECT, 2025
## Makefile
## File description:
## Compiles the 103cipher
##

all:
	cp cypher.py ./103cipher
	chmod 777 103cipher

clean:
	find -type f \( -name '*~' -or -name '#*#' \) -delete

fclean:	clean
	rm -f 103cipher

re:	fclean	all	clean
