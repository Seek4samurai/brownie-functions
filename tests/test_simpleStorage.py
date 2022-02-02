from brownie import SimpleStorage, accounts
import time


def testDeploy():
    # Arrange
    account = accounts[0]
    simpleDeploy = SimpleStorage.deploy({"from": account})

    # Act
    startingValue = simpleDeploy.retrieve()
    expectedValue = 0

    # Assert
    assert startingValue == expectedValue

    time.sleep(1)


def testUpdating():
    # Arrange
    account = accounts[0]
    simpleDeploy = SimpleStorage.deploy({"from": account})

    # Act
    expected = 15
    simpleDeploy.store(expected, {"from": account})

    # Assert
    assert expected == simpleDeploy.retrieve()

    time.sleep(1)
