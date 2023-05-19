bitcoin_value = 10000
bitcoin_increase = 10
total_bitcoin_value = bitcoin_value + (bitcoin_value * (bitcoin_increase / 100))

print(f"The total increase is  {total_bitcoin_value}")
print(f"The amount it increased by is " + str((total_bitcoin_value - bitcoin_value)))