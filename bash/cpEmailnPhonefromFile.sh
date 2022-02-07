touch contact.txt
cat $1 | grep "^+91[6-9][0-9]{9}+" >> contact.txt
cat $1 | grep "^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+" >> contact.txt
grep -e "[6-9][0-9]{9}+\|[a-zA-Z0-9]+@[a-zA-Z0-9.]+" $1
cat contact.txt