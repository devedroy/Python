add() {
    a=$(($1+$2))
    # echo $a
    # echo $@
    echo $a
    return $a
}
echo "cmdline args are $@"
# add $1 $3
# s=$?
s=$(add $1 $3)
echo "sum is $s"