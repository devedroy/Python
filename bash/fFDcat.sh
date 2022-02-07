Ser() {
    cat $1 | grep "help"
}
Dir() {
    ls -l $1
}

if [ -d $1 ]
then
    Dir $1
elif [ -f $1 ]
then
    Ser $1
else
    echo "Invalid file or directory"
fi