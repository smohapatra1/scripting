#   https://www.geeksforgeeks.org/find-count-number-given-string-present-2d-character-array/

def computeLPSArray(pat, M, lps):
    # length of the previous longest prefix suffix
    len = 0

    lps[0] = 0  # lps[0] is always 0

    # the loop calculates lps[i] for i = 1 to M-1
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:  # (pat[i] != pat[len])
            if len != 0:
                len = lps[len - 1]
                # Also, note that we do not increment i here
            else:  # if (len == 0)
                lps[i] = 0
                i += 1

# Prints occurrences of pat in txt


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0]*M

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
    i = 0  # index for txt
    j = 0  # index for pat
    cnt = 0  # to store no of occurence.
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            j += 1
            i += 1

        if j == M:
            cnt += 1
            j = lps[j - 1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i = i + 1
    return cnt

if __name__ == "__main__":
    str = "MAGIC"
    input = ["BBABBM", "CBMBBA", "IBABBG", "GOZBBI", "ABBBBC", "MCIGAM"]
    n = len(input)
    m = len(input[0])
    ans = 0
    # row wise
    for i in range(n):
        text = input[i]
        # left to right match
        ans += KMPSearch(str, text)
        # right to left match
        text = text[::-1]
        ans += KMPSearch(str, text)

    # column wise;
    for i in range(m):
        text = ""
        for j in range(n):
            text += input[j][i]
        # top to down;
        ans += KMPSearch(str, text)
        # down to top;
        text = text[::-1]
        ans += KMPSearch(str, text)

    print("Count : ", ans)