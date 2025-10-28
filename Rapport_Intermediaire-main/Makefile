.PHONY: all clean

FILE = main
PARAM = param

all: build

build:
	@echo "Building the project..."
	lualatex -interection=nonstopmode $(FILE).tex
	# Run twice to resolve references
	lualatex -interection=nonstopmode $(FILE).tex

clean:
	@echo "Cleaning up..."
	rm -rf ${FILE}*.aux
	rm -rf ${FILE}*.bcf
	rm -rf ${FILE}*.lof
	rm -rf ${FILE}*.log
	rm -rf ${FILE}*.out
	rm -rf ${FILE}*.run.xml
	rm -rf ${FILE}*.synctex.gz
	rm -rf ${FILE}*.toc
	rm -rf ${PARAM}*.aux
	rm -rf include/*.aux
