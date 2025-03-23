from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network


def my_deploy_favorites() -> VyperContract:
    my_favorites_contract: VyperContract = favorites.deploy()
    my_starting_number: int = my_favorites_contract.retrieve()
    print(f"Starting number is {my_starting_number}!")

    # store new number
    my_favorites_contract.store(69)
    my_ending_number: int = my_favorites_contract.retrieve()
    print(f"The ending number is {my_ending_number}!")

    return my_favorites_contract


def moccasin_main() -> VyperContract:
    return my_deploy_favorites()
