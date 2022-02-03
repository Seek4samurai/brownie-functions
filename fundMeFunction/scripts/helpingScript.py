from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deployMocks():
    print(f"Active network is {network.show_active()}")
    ("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": get_account()})
    print("Mock Deployed!")
