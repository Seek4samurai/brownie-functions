from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpingScript import get_account, deployMocks


def deployFundMe():
    account = get_account()
    if network.show_active() != "development":
        priceFeedAddress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deployMocks()
        priceFeedAddress = MockV3Aggregator[-1].address

    fundMe = FundMe.deploy(
        priceFeedAddress,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fundMe.address}")


def main():
    deployFundMe()
