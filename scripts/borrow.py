from webbrowser import get
from brownie import accounts, interface, network, config
from web3 import Web3
from scripts._weth import get_weth, deposit_to_weth, get_weth_balance
from scripts._aave import get_lending_pool, deposit, approve_weth, get_user_data

WETH = None

def get_account():
    if (network.show_active() == "develpoment"):
        return accounts[0]
    else:   
        return accounts.add(config["wallets"]["from_key"])

def main():
    account = get_account()
    WETH = get_weth()

    # deposit_to_weth(WETH, account, Web3.fromWei(0.1, "ether"))
    # print(get_weth_balance(WETH, account))
    lending_pool = get_lending_pool()
    # approve_weth(account, Web3.fromWei(0.1, "ether"), lending_pool.address, config["networks"][network.show_active()]["weth_token"])
    # deposit(account, Web3.fromWei(0.1, "ether"), lending_pool, config["networks"][network.show_active()]["weth_token"])
    get_user_data(account, lending_pool)
