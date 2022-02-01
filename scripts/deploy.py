from brownie import accounts, config, SimpleStorage
import os, time


def deploySimpleStorage():
    # four methods to use sensitive variables using these techniques
    account = accounts[0]
    # account = accounts.load("myAccount")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    # deploying contract
    simpleDeploy = SimpleStorage.deploy({"from": account})

    # initializing retrieve and getting 0 since we initialized it with 0
    storedValue = simpleDeploy.retrieve()
    print(storedValue)

    # updating the store function and getting 1
    transaction = simpleDeploy.store(1, {"from": account})
    storedValue = simpleDeploy.retrieve()
    print(storedValue)

    # waiting for all transactions to finish
    # time.sleep(1)
    transaction.wait(1)


def main():
    deploySimpleStorage()
