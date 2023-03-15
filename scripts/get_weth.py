from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    get_weth()

def get_weth():
    """
    Mints WETH by depositing ETH
    Check out already deployed goerli weth contract
    """
    # ABI - Get the weth interface from git hub 
    # Address - Add the token address in brownie-config

    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])

    # txn to get WETH for given ETH
    eth = 0.1
    tx = weth.deposit({"from": account, "value": eth * 10 ** 18})
    tx.wait(1)
    print("Recieved 0.1 WETH")
    # This is an ERC20 token which can be used to interact with Aave functions
    return tx
    