# path
SOURCES=$(wildcard *.md)
DEST_DIR=/root/nginx/html

# file format 
GEN_HTML=$(SOURCES:%.md=%)


all:$(GEN_HTML)

$(GEN_HTML):%:%.md
	marked -i $^ -o $(DEST_DIR)/$@.html



# marked -i $(wildcard *.md) -o $(DEST_DIR)/$<.html
