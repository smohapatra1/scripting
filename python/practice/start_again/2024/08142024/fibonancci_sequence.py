#   Print the Fibonacci sequence up to a given number of terms.

def fibonancci_seq(n):
    fibo_seq = [0, 1 ]
    while len(fibo_seq) < n:
        fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
    return fibo_seq
if __name__ == "__main__":
    num_terms = int(input("Enter the number of terms: "))
    result = fibonancci_seq(num_terms)
    print ("Fibonancci sequence is {}: ".format(result))
