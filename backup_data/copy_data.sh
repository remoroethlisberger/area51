# Keeps daily copies of files and folders in a SOURCE folder copied to the PATH specified
readonly TARGET="/mypath/folder/"$(date +%Y%m%d)
readonly SOURCE="/mypath/folder/source"
mkdir "$TARGET"
cp -r "$SOURCE" "$PATH"
