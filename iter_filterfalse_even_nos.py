import itertools

def main():
    even_num_list = list(itertools.filterfalse(lambda x: x%2 != 0, range(20)))
    print(even_num_list)
    for index, value in enumerate(even_num_list):
        if index == len(even_num_list) - 1:
            print(value)
        else:
            print(value, end=" - ")

if __name__ == "__main__":
    main()
