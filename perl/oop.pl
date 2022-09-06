use strict;
use warnings;
use diagnostics;

# say prints a line followed by a newline
use feature 'say';

# Use a Perl version of switch called given when
use feature "switch";

# use v5.36;  # (does not support given())
use v5.16;  

# ---------- OBJECT ORIENTED PERL ----------
# In Perl a class corresponds to a package which is a
# self contained unit of variables and subroutines
 
use lib 'lib';
 
use Animal::Cat;
 
# Create a Cat object
my $whiskers = new Animal::Cat("whiskers", "Derek");
 
# Call the subroutine that returns the name
say $whiskers->getName();
 
# Change the name
$whiskers->setName("Whiskers");
 
say $whiskers->getName();
 
say $whiskers->getSound();
 
# Inheriting object
use Animal::Lion;
 
# Create object that inherits from Cat
my $king = new Animal::Lion("King", "No Owner");
 
# Call overridden method
say $king->getSound();
