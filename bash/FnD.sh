pwd

f=0
d=0
w=0
for i in *
do
    if [ -d $i ]
    then
        d=$((d+1))
    elif [ -f $i ]
    then
        f=$((f+1))
    elif [ -w $i ]
    then
        w=$((w+1))
    fi
done
echo "Total no. of files: $f"
echo "Total no. of directories: $d"
echo "Total no. of writable files: $w"