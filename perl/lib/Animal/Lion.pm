package Animal::Lion;

use Animal::Cat;
use strict;


# To inherit from a another object
our @ISA = qw(Animal::Cat);

# To overrride a subroutine
sub getSound {
  my ($self) = @_;
  return $self->{name}, " says Rowrrr";
}

1;
