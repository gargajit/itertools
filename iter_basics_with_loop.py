def main():

    countries = ('India', 'USA', 'England', 'France', 'Italy', 'Germany')

    country_iter = iter(countries)

    while True:
        try:
            print(next(country_iter))
        except StopIteration:
            break

    
if __name__ == "__main__":
    main()
