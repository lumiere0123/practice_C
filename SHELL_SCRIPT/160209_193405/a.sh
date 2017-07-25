
# check if the number of arguments is 2
if [ $# -eq 2 ];then
  # if 2, don't do anything
  echo 
  # if not, print error and usage
else
  echo "ERROR: usage $0 [arg] [arg]"
fi
