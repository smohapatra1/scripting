#   https://www.google.com/search?q=Here+is+a+list+of+daily+stock+prices.+Return+the+buy+and+sell+prices+to+maximize+the+profit+using+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNkiqz60BiQF380O-TlNm8LmbEoTA%3A1750867433492&ei=6R1caNHhHbzJkPIP4-KdoQE&ved=0ahUKEwiR-q-7-YyOAxW8JEQIHWNxJxQQ4dUDCBE&uact=5&oq=Here+is+a+list+of+daily+stock+prices.+Return+the+buy+and+sell+prices+to+maximize+the+profit+using+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiaEhlcmUgaXMgYSBsaXN0IG9mIGRhaWx5IHN0b2NrIHByaWNlcy4gUmV0dXJuIHRoZSBidXkgYW5kIHNlbGwgcHJpY2VzIHRvIG1heGltaXplIHRoZSBwcm9maXQgdXNpbmcgcHl0aG9uSNMqUABYxyhwAngBkAEAmAHOBKABqhCqAQswLjcuMC4xLjAuMbgBA8gBAPgBAvgBAZgCAaACzgHCAgUQABiABJgDAJIHAzItMaAHjQuyBwMyLTG4B84BwgcDNC0xyAcY&sclient=gws-wiz-serp

def max_profit(prices):
    max_profit = 0 
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
max_profit_result = max_profit(prices)
print (f"Maximum profit : {max_profit_result}")