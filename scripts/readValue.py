from brownie import SimpleStorage, accounts, config


def readContract():
    simpleStorage = SimpleStorage[-1]
    print(simpleStorage.retrieve())


def main():
    readContract()
