#!/bin/bash
# List all logged-in users and gives the system uptime
# and saves the output in a logfile

LOG_FILE="$PWD/current_users_log.txt"
ROOT_UID=0    # Only users with $UID 0 have root privileges
LINES=50      # Default numbers of lines saved
E_NOTROOT=87  # Non-root exit error

# Run as root, of course.
if [ "$UID" -ne $ROOT_UID ]
then
  echo "Must be root to run this script."
  exit $E_NOTROOT
fi

if [ -n "$1" ]
# Test whether command-line argument is present (non-empty).
then
  lines=$1
else
  lines=$LINES # Default, if not specified on command-line.
fi

current_date=$(date)
current_users=$(who)
system_uptime=$(uptime)

if [ -f "$LOG_FILE" ]; then
  echo $current_date >> $LOG_FILE
  echo "$current_users" >> $LOG_FILE
  echo $system_uptime >> $LOG_FILE
  echo "" >> $LOG_FILE
else
  echo "log file doesn't exists creating one ..."
  touch $LOG_FILE
  echo $current_date > $LOG_FILE
  echo "$current_users" >> $LOG_FILE
  echo $system_uptime >> $LOG_FILE
  echo "" >> $LOG_FILE
fi

exit 0
