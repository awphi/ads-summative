import sys

def read_input(filename):
    A = []
    
    try:
        myfile = open(filename, 'r')
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
    for line in myfile:
        A = A + [int(line.strip())]
    myfile.close()
    return A


def insertionsort(A):
    for j in range(1, len(A)):
        x = A[j]
        i = j - 1
        while (i >= 0) and (A[i] > x):
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = x
    return A
  
def partition(A, k):
    n = len(A)
    pivots = insertionsort(A[n - k:n])
    seqs = []

    for pivot in pivots:
        seqs.append([])
        seqs.append([pivot])
    seqs.append([])

    for a in A:
        if(a in pivots):
            continue

        for i in range(0, len(pivots)):
            pivot = pivots[i]
            if(a < pivot):
                seqs[2 * i].append(a)
                break
        else:
            seqs[2 * i + 2].append(a)
    return seqs
    

def quicksort(A, k):
    parts = partition(A, k)
    for i in range(0, len(parts)):
        n = len(parts[i])

        if(n <= 1):
            continue;
        elif(n < 2 * k):
            parts[i] = insertionsort(parts[i])
        else:
            parts[i] = quicksort(parts[i], k)

    return sum(parts, [])
    

def main():
    k = int(sys.argv[1])
    filename = sys.argv[2]
    A = read_input(filename)
    print(quicksort(A,k))
    
if __name__ == "__main__":
    main()