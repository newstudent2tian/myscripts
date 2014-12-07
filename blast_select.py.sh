#!/bin/bash
#!author: zf.wang

if [ $# -eq 0 ]; then
  echo "Please input file names."
  echo "e.g.: $0 name.blast" 
  exit 1 
fi

suffix=".ok"

for((i=1;i<=$#;i++));
do
  filename=$(eval echo \${${i}})
  echo $filename
  cat $filename | tr -t "\n" "%" | awk -F "#" ' 
  {
          for(i=1;i<=NF;i++)
          {
                  print $i |"grep found.*comp" 
          }
  }' | sed -r 's/^.*found%//' > out1

  filename=$(eval echo \${${i}})${suffix}
  
  while read line
  do
  echo $line | tr -t "%" "\n" > outtemp

  awk 'BEGIN { min=100000000000;first=0;second=0;} 
  {
    num=strtonum($15);
    if(num!=0 && num < min) {
      min=num;
      first=$1;
      second=$14;
    };
  }END {
    print first "\t" second "\t" min
  }' outtemp >> $filename

  rm -f outtemp

  done < out1

  rm -f out1
done

echo "all files process successfully!"