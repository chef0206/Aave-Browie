// SPDX-Licence-Identifier: MIT
pragma solidity 0.6.12;

interface ILendingPoolAddressesProvider {
    function getLendingPool() external view returns(address);
}

