#   What is the largest subset whose elements are Fibonacci numbers

#   https://www.google.com/search?q=What+is+the+largest+subset+whose+elements+are+Fibonacci+numbers+using+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifOr8QU19Mep7Pcuv-QtyL1Unhpozw%3A1751149000663&ei=yGlgaMeYKO2EwbkP8IDLsQM&ved=0ahUKEwjHnIixkpWOAxVtQjABHXDAMjYQ4dUDCBE&uact=5&oq=What+is+the+largest+subset+whose+elements+are+Fibonacci+numbers+using+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiTFdoYXQgaXMgdGhlIGxhcmdlc3Qgc3Vic2V0IHdob3NlIGVsZW1lbnRzIGFyZSBGaWJvbmFjY2kgbnVtYmVycyB1c2luZyBweXRob25ImwRQAFgAcAB4AZABAJgB0AGgAdABqgEDMi0xuAEDyAEA-AEC-AEBmAIAoAIAmAMAkgcAoAeIAbIHALgHAMIHAMgHAA&sclient=gws-wiz-serp


def find_largest_fibonancci_subset(arr):
    if not arr:
        return []
    max_val = max(arr)
    fib_set = set()
    a, b = 0, 1
    while a <= max_val:
        fib_set.add(a)
        a, b = b, a+b
    fib_subset = []
    for num in arr:
        if num in fib_set:
            fib_subset.append(num)
    return fib_subset
input_arr = [ 1, 4, 3, 9, 10, 13, 7, 21, 2]
result_subset = find_largest_fibonancci_subset(input_arr)
print (f"The largest Fibonacci subset is :  {result_subset}")