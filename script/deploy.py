from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network


def deploy_favorites() -> VyperContract:
    favorites_contract = favorites.deploy()
    print("YAY Cyfrin")
    print(type(favorites_contract))
    starting_number: int = favorites_contract.retrieve()
    print(f"Starting number is {starting_number}")

    favorites_contract.store(77)
    ending_number: int = favorites_contract.retrieve()
    print(f"Ending number is {ending_number}")

    active_network = get_active_network()
    print(active_network)
    print(type(favorites_contract))
    if active_network.has_explorer():
        print("Verifying contract")
        result = active_network.moccasin_verify(favorites_contract)
        print(result)
        result.wait_for_verification()
    else:
        print("No explorer available")
    return favorites_contract


def moccasin_main() -> VyperContract:
    return deploy_favorites()
