#   Given is an array of positive integers. Can you find the smallest subarray's length whose sum of elements is greater than a given number k? 
#   https://www.google.com/search?q=Given+is+an+array+of+positive+integers.+Can+you+find+the+smallest+subarray%27s+length+whose+sum+of+elements+is+greater+than+a+given+number+k%3F+using+python&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifO6mtcKBt-wtsdZKPGyahNLL10QGA%3A1751300166859&ei=RrhiaJzQM7jIptQPopPx0A8&ved=2ahUKEwjZjNyBqZyOAxU4hu4BHTcbGiEQ0NsOegQIChAA&uact=5&sclient=gws-wiz-serp&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeiAkWG4OlBE2zyCTMjPbGmPzNVD9LjlghyJHnd1ZXeDdXVx4XE4fnKIrgG-eztKBa3XtqheD5mv_PGu_xz1oxsTBhDqma78rPHYeMtbJGhp_YBMowGlCYXdBe8BaAHMPR3C2iKJi45mGPs87_bYqOvAigi1A7HLWQDRaVR4RG5sC16x-2A&aep=10&ntc=1&mstk=AUtExfAqi1cNdvK0434Sp_SdPR_OrzQQsqZ63MWxkMFZwytyuJMxhQJNfpH9UyiTa5M5oB_HIdPthmJ2YKww15GmBKzjuwqpJ07uDBQpn-yPRW_peapalCE8MwgPP-G3mkWSIJe9lymjOmSqc-EpyKSDbOkjq2IjIGNnp_oqz28Uf4WxkDsUjuxl-DSw4T2L-QdDrUPT6EER1fjIoxqK-yjXgs51q_D-bHivVW0exscuB68NG_SIldpHN2d6CLlt8JYX-WodAninySTu4woke0lAyLF_Mm7o_TRqoRfnpmt87QBEsOH7DrCQIWlg39zTJlxQ0ExhviYBnyE8zr2CszbUlDJOUsXJ31_FatFf_yrN03pMmGGZK7tFfLQYtHPA5MKNxb-8MA3ebXaIf8Jv-b1cfppg3Y_Uchwqgz3ZWO_0ZkdNdFNR0JyoApDvF0fK5CEh5Z3mQ1uCdzY&csuir=1

def smallest_subarray_with_sum(target: int, nums: list[int]) -> int:
    n = len(nums)
    min_length = n + 1
    window_sum = 0
    left = 0

    for end in range(n):
        window_sum += nums[end]

        while window_sum >= target:
            min_length = min(min_length, end - left + 1)
            window_sum -= nums[left]
            left += 1

    return min_length if min_length <= n else 0

nums = [2, 3, 1, 2, 4, 3]
target = 7
result = smallest_subarray_with_sum(target, nums)
print (f"The minimum subarray length is : {result}")