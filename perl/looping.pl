use strict;
use warnings;
use diagnostics;

# say prints a line followed by a newline
use feature 'say';

# Use a Perl version of switch called given when
use feature "switch";

# use v5.36;  # (does not support given())
use v5.16;  

# ---------- LOOPING ----------
 
# For loop
for(my $i = 0; $i < 10; $i++){
  say $i;
}
 
# Print odds with the While loop
my $i = 1;
 
while ($i < 10){
  if($i % 2 == 0){
    $i++;
 
    # next skips back to the beginning of the loop (like "continue" in Python)
    next;
  }
 
  # Last exits out of the loop
  if($i == 7){ last; }  # like "break" in Python
 
  say $i;
  $i++;
}
 
# The Do while loop is used when you must loop once
# my $lucky_num = 7;
# my $guess;
# do {
#   say "Guess a Number Between 1 and 10";
#  
#   # This is how you get user input
#   $guess = <STDIN>;
# } while $guess != $lucky_num;
#  
# say "You guessed 7";
#
# Given When Perl Switch statement
my $age_old = 18;
given ($age_old) {
  when($_ > 16) {
    say "Drive";
 
    # Will continue with the next cases
    continue;
  }
  when($_ > 17) {say "Go Vote";}
  default {say "Nothing Special";}
} 
