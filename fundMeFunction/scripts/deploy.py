from brownie import FundMe, network, config
from scripts.helpingScript import get_account


def deployFundMe():
    account = get_account()
    if network.show_active != "development":
        priceFeedAddress = config["networks"][network.show_active()]["ethUsdPriceFeed"]
    
    fundMe = FundMe.deploy(priceFeedAddress, {"from": account}, publish_source=True)
    print(f"Contract deployed to {fundMe.address}")


def main():
    deployFundMe()
