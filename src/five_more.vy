# pragma version 0.4.0
# @license MIT

import favorites
import colors

initializes: favorites
exports: (
    favorites.retrieve,
    favorites.add_person
)
initializes: colors
exports: (
    colors.store_color,
    colors.get_color
)

@deploy
def __init__():
    favorites.__init__()
    colors.__init__()
    # print(favorites.my_favorite_number)

@external
def store(new_number: uint256):
    favorites.my_favorite_number = new_number + 5

@external
def store_new_color(new_color: String[100]):
    colors.my_favorite_color = new_color
