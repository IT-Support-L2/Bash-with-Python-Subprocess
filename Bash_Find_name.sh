> matched_pattern.txt  
files=`grep jane* ~/directory/log.txt`
for i in $files; do
 if [ -f ~/directory/$i ]; then
     echo $i >> matched_pattern.txt
fi
done

<<COMMENTS
This script grep 'jane' username using regex from a log file and append the matched pattern to matched_pattern.txt
COMMENTS
