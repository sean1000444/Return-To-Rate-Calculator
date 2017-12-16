ETH_price = 624.78
initialDollar = 1000
initialMANA = 100000
percentReturn = 500.0
endDollar = initialDollar * (percentReturn/100)
endManaDollarPrice = endDollar / initialMANA
print("To get", percentReturn/100.0, "times or $", endDollar)
print("Which valuates a plot to $", endManaDollarPrice*1000, "and MANA at $", endManaDollarPrice)

desiredETH = endDollar / ETH_price
desiredEthToMANA = desiredETH / initialMANA
test = 0

print(desiredEthToMANA)
