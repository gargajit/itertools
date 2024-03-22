from itertools import permutations

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    S, K = input().split(" ")
    K = int(K)
    my_list = list(permutations(S, K))
    joined_values = [''.join(p) for p in my_list]
    joined_values.sort()
    for value in joined_values:
        print(value)
    

    return 0

if __name__ == '__main__':
    main()
