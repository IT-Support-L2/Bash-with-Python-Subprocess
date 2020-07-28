> oldFiles.txt
files=`grep jane* ~/learning/text.txt`
for i in $files; do
 if [ -f ~/learning/$i ]; then
     echo $i >> oldFiles.txt
fi
done