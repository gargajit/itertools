def main():

    countries = ('India', 'USA', 'England', 'France', 'Italy', 'Germany')     #tuple

    country_iter = iter(countries)      #iter function gives iterator over a sequence

    print(countries)
    print(countries[5])
    print(next(country_iter))          #next function: by calling next on the iterator, it prints the next item in the sequence
    print(next(country_iter))
    print(next(country_iter))
    print(next(country_iter))
    print(next(country_iter))


if __name__ == "__main__":
    main()
