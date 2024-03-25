def main():
    
    with open('places_to_visit.txt') as file:
        for line in iter(file.readline, ""):      #iter function with a function and sentinel value i.e. end of the file
            print(line, end="")


if __name__ == "__main__":
    main()
