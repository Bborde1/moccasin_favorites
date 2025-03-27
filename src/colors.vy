# pragma version 0.4.0
# @license MIT

# This contract stores a favorite color attribute to a Person struct

has_favorite_color: bool
my_favorite_color: public(String[100])
my_address: address

struct Person:
    favorite_color: String[100]
    name: String[100]

@deploy
def __init__():
    self.my_favorite_color = "Black"

@external
def store_color(new_color: String[100]):
    self.my_favorite_color = new_color

@external
@view
def get_color() -> String[100]:
    return self.my_favorite_color
    
