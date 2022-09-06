use strict;
use warnings;
use diagnostics;

# say prints a line followed by a newline
use feature 'say';

# Use a Perl version of switch called given when
use feature "switch";

use v5.36;

# ---------- SCALARS ----------
# There are 3 data types in Perl Scalars, Arrays and Hashes
 
# Use the my function to declare a variable
# The Sigil $ says we are defining a scalar or single value
# The variable must start with a letter or _ and then numbers
# there after
# A variable receives the default value of undef

my $name = 'Derek';

my ($age, $street) = (40, '123 Main St');

my $my_info = "$name lives on \"$street\"\n";
$my_info = qq{$name lives on "$street"\n};  # to avoid scaping double quotes

print $my_info;

my $bunch_on_info = <<"END";
This is a
bunch of information
on multiple lines
END

say $bunch_on_info;

my $big_int = 18446744073709551615;

# You can formatted strings by defining the data type after %
# %c : Character
# %s : string
# %d : Decimal
# %u : Unsigned integer
# %f : Floating Point (Decimal Notation)
# %e : Floating Point (Scientific Notation)

printf("%u \n", $big_int + 1);

# You can trust 16 digits of precision for floats on most machines
my $big_float = .1000000000000001;
# You can define the decimal precision amount
printf("%.16f \n", $big_float + .1000000000000001);

# Switch values of scalars
my $first = 1;
my $second = 2;
($first, $second) = ($second, $first);
say "$first $second";
