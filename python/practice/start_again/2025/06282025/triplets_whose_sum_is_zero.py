#   https://www.google.com/search?q=Can+you+find+the+triplets+whose+sum+is+zero%3F+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifM2rRtB49GXZHkKXqU-Nr9Nt_rrNw%3A1751147938980&ei=omVgaMG9O5KIwbkPmLmn6AU&ved=0ahUKEwjBlui2jpWOAxUSRDABHZjcCV0Q4dUDCBE&uact=5&oq=Can+you+find+the+triplets+whose+sum+is+zero%3F+using+python%C2%A0&gs_lp=Egxnd3Mtd2l6LXNlcnAiO0NhbiB5b3UgZmluZCB0aGUgdHJpcGxldHMgd2hvc2Ugc3VtIGlzIHplcm8_IHVzaW5nIHB5dGhvbsKgMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigATIFECEYqwJIoSNQAFipIXAAeACQAQCYAZIBoAGtD6oBBDAuMTW4AQPIAQD4AQL4AQGYAg-gApkQwgIGEAAYFhgewgILEAAYgAQYhgMYigXCAggQABiABBiiBJgDAJIHBDAuMTWgB4tLsgcEMC4xNbgHmRDCBwowLjIuMTEuMS4xyAdM&sclient=gws-wiz-serp


def find_triplets_with_zero_sum(nums):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1 
        right = n - 1
    while left < right:
        current_sum = nums[i] + nums[left] + nums[right] 
        if current_sum == 0:
            result.append([nums[i], nums[left], nums[right]])
            while left < right and nums[left] == nums[left +1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -=1
            left += 1
            right -=1
        elif current_sum < 0:
            left +=1 
        else:
            right -=1
    return result

nums1 = [-1, 0, 1, 2, -1, -4]
print(f"Triplets with zero sum in {nums1}: {find_triplets_with_zero_sum(nums1)}")

nums2 = [0, 0, 0]
print(f"Triplets with zero sum in {nums2}: {find_triplets_with_zero_sum(nums2)}")

nums3 = [1, 2, 3]
print(f"Triplets with zero sum in {nums3}: {find_triplets_with_zero_sum(nums3)}")