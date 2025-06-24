#   https://www.google.com/search?q=You+are+given+a+set+of+random+numbers.+Write+a+code+to+shift+all+the+zeros+to+the+left.&authuser=0&aep=21&udm=50&utm_source=google&utm_campaign=aim_aware&utm_content=oo-seaport-10128&mstk=AUtExfBBAsUT-Tut-YWe2oRfBREA3nk9on8AvH_NoNBG7uSFftfrwkBp4-uDTxG7zNNEbmbzH8u1cMpbimXjEI1h8Y8T63AZ2WdE6n5OCrSXoDoYS9xcschTIGkfba8zp5BfvUXOu0Bg2A4fSzGH0dmsiWyJM-l5youFQHpgjPQ3KIUzQDQ3aXnGXv707XswyNkIoS1GIaK2OrdAK-UUqkwngxSnwPxsaa8y0tFuPN3T0vjcn2ObyHohaPj74ahMDbjcdTm_4Dg5JOvg0AjQ83aC2DoGdsyAdUdmIfKD1D3SIIyVGVdC73uGa358x1-zC7JrzTBggYcgTw1bOA&csuir=1

def Shift_Nums_Left_Zero(nums):
    n = len(nums)
    index = n - 1 
    for i in range(n-1, -1, -1 ):
        if nums[i] != 0:
            nums[index] = nums[i]
            index -=1
    for a in range(index+1):
        nums[a] = 0 
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12, 0, 5]
    shift_nums = Shift_Nums_Left_Zero(nums)
    print (shift_nums)