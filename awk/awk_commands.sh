#!/bin/bash

# AWK: Alfred Aho, Peter Weinberg and Brian Kernighan (has associative arrays)

### AWK PATTERN ###
awk 'if(PATTERN1){...print something..} if(PATTERN2){...print something..} ...'
# Basic read
awk '{print "First column item: " $1 " Second column item: " $2 }' temps.csv
# NR>1 So the number record starts from 1, the NR==1; prints the first line
awk 'NR==1; NR>1{print ($2=="F" ? ($1-32) / 1.8 : $1)" C"}' temps.csv
# With the formatting print function
awk 'NR==1; NR>1{printf("%.1f %c\n",($2=="F" ? ($1-32) / 1.8 : $1),"C")}' temps.csv
# Specifying the field separator -F',' (space is by default)
awk -F' ' '{print "First column item: " $1 " Second column item: " $2 }' temps.csv
# Matching pattern example
awk 'NR==1{print} NR==2{print} {print}' temps.csv

# Regex in awk $0 refers to the entire line
awk '($0 ~ /e$/){print $0}' animals.txt
# Parenthesis are optional
awk '$0 ~ /e$/{print $0}' animals.txt
# The entire line is the default input
awk '/e$/{print $0}' animals.txt
# The regex action is the default output (grep like)
awk '/e$/' animals.txt
# Replaces also the sed command
awk '{ gsub(/e$/, "zzzzz");print}' animals.txt

# Comparing awk with cut
 cut -d -f1,5 grades.csv
 awk -F, '{ print $1, $5 }' grades.csv

 cut -d: -f2 studentlist | xargs printf "%s@example.edu"
 awk -F: '{ print $2 "@example.edu" }' studentlist

# Comparing awk with bash
 while IFS=, read user p1 p2 p3 p4; do
   (( p1 + p2 + p3 + p4 < 70 )) && echo $user;
 done < grades.csv
 awk -F, '$2 + $3 + $4 + $5 < 70' grades.csv

# Splitting input into multiple files:
fwadm list -p -o uuid,owner_uuid,rule | \
  awk -F: '$2 != "-" { print >> "rules/"$2 }'

# Quick method to sum everything in a column
ls -l /tmp/*-log-* | awk '{ size += $5; } END { print size; }'
# or based on column:
awk '{ sums[$1] += $2 } END { for (usr in sums) print usr, sums[usr] }'
# Cross-POSIX system method to get Unix Epoch:
awk 'BEGIN { srand(); t = srand(); print t; }'

 # transform csv of events on a xml file
 # awk
 # BEGIN { print "<staff-calendar><schedule>" }
 # END { print "</schedule></staff-calendar>" }
 # {
 #   print "<event>"
 #   print "<day>" substr($1, 0, 3) "</day>"
 #   print "<date>" $2 "</date>"
 #   print "<time>" $3 "</time>"
 #   print "<location>" $4 "</location>"
 #   print "<name>" $5 "</name"
 #   print "</event>"
 # }

 # gawk
 # Writen by Paul Rubin, David Trueman & Arnold Robbins
 # Implementation of new AWK
 # Time functions like strftime()
 # Arbitrary-precision arithmetic (-M flag)
 # Bit manipulation functions like lshift(), rshift(), and(), or(), and xor()
 # nextfile keyword (added to POSIX in 2012)
