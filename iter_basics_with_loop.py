def main():

    countries = ('India', 'USA', 'England', 'France', 'Italy', 'Germany')

    country_iter = iter(countries)

    while True:
        try:
            country = next(country_iter)
        except StopIteration:
            break
        else:
            print(country)


    
if __name__ == "__main__":
    main()
