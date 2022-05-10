from web3 import Web3
from brownie import interface, network, config

def get_weth():
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    return weth

def get_weth_balance(weth, account):
    return weth.balanceOf(account)

def deposit_to_weth(weth, account, amount):
    tx = weth.deposit({"from": account, "value": amount})
    tx.wait(1)
