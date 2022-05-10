from brownie import interface, network, config
from web3 import Web3

def get_lending_pool():
    lending_pool_addr_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )

    lending_pool_addr = lending_pool_addr_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_addr)

    return lending_pool

def deposit(account, amount, lending_pool, weth_token_addr):
    tx = lending_pool.deposit(
            weth_token_addr, amount, account.address, 0
            ,{"from": account, "gas_limit": config["settings"]["gas_limit"], 'allow_revert': True})
    tx.wait(1)

def approve_weth(account, amount, lending_pool_addr, weth_token_addr):
    weth = interface.IERC20(weth_token_addr)
    tx = weth.approve(lending_pool_addr, amount, {"from": account})
    tx.wait(1)

def get_user_data(account, lending_pool):
    (totalCollateralETH,totalDebtETH,
      availableBorrowsETH,currentLiquidationThreshold,
      ltv, healthFactor
    ) = lending_pool.getUserAccountData(account.address)

    print(f"{Web3.fromWei(totalCollateralETH, 'ether')} eth collateral")
    print(f"{Web3.fromWei(totalDebtETH, 'ether')} eth debt")
    print(f"{Web3.fromWei(availableBorrowsETH, 'ether')} eth is there to borrow")


def borrow(lending_pool, amount_dai_borrow, account, dai_addr):
    # TODO
    
    
    
