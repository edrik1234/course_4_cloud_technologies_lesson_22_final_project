
FILE_NAME=$1
TIME_VALUE=$2


for second in $(seq 1 $TIME_VALUE)
do
  if [ -e "$FILE_NAME" ]
  then
      echo "file $FILE_NAME arrived in server after $second seconds"
      sleep 1
      exit 0
  elif [  $second -eq $TIME_VALUE  ]
  then
      echo "time out"
      sleep 1
      exit 0
  fi
  sleep 1
done

~                   