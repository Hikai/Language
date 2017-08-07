def coin_one_binary_search(coin_b, coin_a=0):
	mid = (coin_a + coin_b) / 2
	# send("{} {}".format(coin_a, mid))
	result = int(recv())
	if result % 10 == 0:
		return coin_one_binary_search(N, coin_a=mid)
	elif result % 10 != 0:
		return coin_one_binary_search(mid)
	else:
		return mid

