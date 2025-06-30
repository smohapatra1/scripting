#   How will you count all distinct pairs with differences equal to k?

#   https://www.google.com/search?q=How+will+you+count+all+distinct+pairs+with+differences+equal+to+k%3F+using+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifPprzMVZF1ZHlDJECoHlJM0mieM9w%3A1751259583001&ei=vhliaNvxPOnYptQP5aXzsQs&ved=0ahUKEwjbyOqqrpiOAxVprIkEHeXSPLYQ4dUDCBE&uact=5&oq=How+will+you+count+all+distinct+pairs+with+differences+equal+to+k%3F+using+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiT0hvdyB3aWxsIHlvdSBjb3VudCBhbGwgZGlzdGluY3QgcGFpcnMgd2l0aCBkaWZmZXJlbmNlcyBlcXVhbCB0byBrPyB1c2luZyBweXRob25IzAtQ3gRY3gRwAXgBkAEAmAGYA6ABmAOqAQM0LTG4AQPIAQD4AQL4AQGYAgGgAj_CAgoQABiwAxjWBBhHmAMAiAYBkAYIkgcBMaAHiwGyBwC4BwDCBwM1LTHIBy8&sclient=gws-wiz-serp

def count_distinct_pair_diff_k(nums, k ):
    unique_nums = set(nums)
    count = 0 
    if k == 0:
        from collections import Counter
        freq = Counter(nums)
        for num in freq:
            if freq[num] > 1:
                count +=1
    else:
        for num in unique_nums:
            if (num+k) in unique_nums:
                count +=1
    return count
arr = [1, 5, 3, 4, 2]
k = 2
result = count_distinct_pair_diff_k(arr, 2)
print (f"Number of distinct pairs with diff {k}: {result}")
