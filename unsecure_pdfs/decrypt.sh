## Decryptes all pdfs in the folder, where the script is executed
## Needs qpdf

var="_dec.pdf"
password="rating"

for file in *.pdf
do
		echo "Processing $file ...";
    	qpdf --password="$password" --decrypt "$file" "$file$var";
    	rm "$file";
done