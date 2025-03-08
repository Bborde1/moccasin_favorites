from src import favorites


def deploy():
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Starting number is {starting_number}")


def moccasin_main():
    deploy()
