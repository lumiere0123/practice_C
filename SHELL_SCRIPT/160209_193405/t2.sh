# check if num of args is 3
if [ $# -eq 3 ];then
  # if true, print the biggest number.


  # 1 >  2
    # true, 1 > 3
      # true, 1
      # not true, 3
    # not true, 2 > 3
      # true, 2
      # not true 3

  big=$1

  if [ $1 -gt $2 ];then
    big=$1
  else
    big=$2
  fi

  if [ $big -gt $3 ];then
    echo $big
  else
    echo $3


# else, print error
