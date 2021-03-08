SRC_FILES = $(wildcard *.tex)
BUILD_DIR=aux

all: $(SRC_FILES:.tex=.pdf)

%.pdf: %.tex
	latexmk -interaction=nonstopmode -shell-escape -pdf -use-make -outdir=$(BUILD_DIR) -cd $<

clean:
	@rm -rf aux
