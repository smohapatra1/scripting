#   Write a code to merge overlapping intervals.
#   https://www.google.com/search?q=Write+a+code+to+merge+overlapping+intervals.&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifOybx8t8GjU9ZPjO2NI4jSbYdg9Wg%3A1750784930201&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZud1z6kQpMfoEdCJxnpm_3W-pLdZZVzNY_L9_ftx08kwv-_tUbRt8pOUS8_MjaceHuSAD6YvWZ0rfFzwmtmaBgLepZn2IJkVH-w3cPU5sPVz9l1Pp06apNShUnFfpGUJOF8p91U6HxH3ukND0OVTTVy0CGuHNdViLZqynGb0mLSRGeGVO46qnJ_2yk3F0uV6R6BW9rQ&aep=1&ntc=1&sa=X&ved=2ahUKEwiN596OxoqOAxVTl-4BHU6VKLYQ2J8OegQIGRAC&biw=1729&bih=876&dpr=2&mstk=AUtExfB6XN-5diO5yrFeXQmVZ-yRQF3HUkqTiTDoSEK8B0-VIW4dapuE8UJA6xuEPSS1eLTZgenz8ZpBaMnYvXCWpFmUiIdVTFijLANwiYJbF6nMB-TFMJJVeepKOsiFQ-5ynBPiVST0Ty84iDGzBZLru6fOy_eRlKGg8CRejR--_DWvgGMh2OXKi5pLJXKcxKFBadYepO-O9vJarGXpZrE_jwqnMse6q58C6u8JcKy98ncHHmRUrN5BM0mWXGL-bZbmgCiR1xPdtl5ShnECli-3hd2R1IJTTtRlxVTEforvbfyP08YaKaLB68MEJbUi1avQ42SPENhcQ_W33A&csuir=1

def merge_interval(intervals):
    intervals.sort(key = lambda x:x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    merged_intervals = merge_interval(intervals)
    print (merged_intervals)
    intervals2 = [[1, 4], [4, 5]]
    merged_intervals2 = merge_interval(intervals2)
    print (merged_intervals2)