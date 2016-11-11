#!/bin/bash
## DESCRIPTION:	Decryptes all pdfs in the folder, where the script is executed. All files need to be encrypted with the same key!
## AUTHOR: Remo Röthlisberger
## DATE: 11.11.2016

var="_dec.pdf"
password="rating"

for file in *.pdf
do
		echo "Processing $file ...";
    	qpdf --password="$password" --decrypt "$file" "$file$var";
    	rm "$file";
done
