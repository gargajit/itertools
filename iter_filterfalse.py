import itertools

def main():
    odd_num_list = list(itertools.filterfalse(lambda x: x%2 == 0, range(10,45)))
    print(odd_num_list)

if __name__ == "__main__":
    main()
