from src import favorites, favorites_factory, five_more
from moccasin.boa_tools import VyperContract


def deploy_favorites():
    favorites_contract: VyperContract = favorites.deploy()
    return favorites_contract


def deploy_factory(favorites_contract: VyperContract):
    factory_contract = favorites_factory.deploy(favorites_contract.address)
    factory_contract.create_favorites_contract()

    new_favorites_address: str = factory_contract.list_of_favorite_contracts(0)
    new_favorites_contract: VyperContract = favorites.at(new_favorites_address)
    new_favorites_contract.store(77)
    print(f"Stored favorite value is {new_favorites_contract.retrieve()}")

    factory_contract.store_from_factory(0, 88)
    print(f"new contract stored value is {new_favorites_contract.retrieve()}")
    print(f"Original contract stored value is {favorites_contract.retrieve()}")


def deploy_five_more():
    five_more_contract: VyperContract = five_more.deploy()
    five_more_contract.store(89)
    # five_more_contract.store_new_color("red")
    print(five_more_contract.retrieve())
    print(five_more_contract.get_color())


def moccasin_main():
    favorites_contract = deploy_favorites()
    deploy_factory(favorites_contract)
    deploy_five_more()
