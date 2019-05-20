all: install run
    
install:
	pip install hovercraft

run:
	hovercraft ./slides.rst
