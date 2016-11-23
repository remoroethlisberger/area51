#!/bin/bash
## DESCRIPTION:	Move files with the specified substring to the specified new folder!
## AUTHOR: Remo Röthlisberger
## DATE: 11.11.2016

echo "Please enter the substring, that is contained in all files"
read substring

echo "Please enter the new folders name"
read folder

mkdir "$folder";

for file in *
	do
			echo "Processing $file ...";
			if [[ $file == *"$substring"* ]] 
				then
				var="$folder/$file"
				mv "$file" "$var"; 
	    		fi
	done
