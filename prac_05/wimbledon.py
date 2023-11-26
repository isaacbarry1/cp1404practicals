"""
CP1404/CP5632 Practical
Wimbledon
"""

FILENAME = "wimbledon.csv"


def main():
    """Read data from wimbledon.csv and print details about it"""

    data = get_data(FILENAME)
    champions, countries = process_data(data)
    display_wimbledon_results(champions, countries)


def display_wimbledon_results(champions, countries):
    """Display champions and countries"""

    print('Wimbledon Champions: ')

    for champion, count in champions.items():
        print(champion, count)

    print(f'\nCountries with Wimbledon victories ({len(countries)} in total):')
    print(', '.join(sorted(countries)))


def process_data(data):
    """Process the data and record the champions and countries from the data"""

    champions = {}
    countries = set()

    for entry in data:

        country = entry[2]
        countries.add(country)
        champions[country] = champions.get(country, 0) + 1

    return champions, countries


def get_data(filename):
    """Get data from file"""

    data = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:

        in_file.readline()
        for line in in_file:

            parts = line.strip().split(",")
            data.append(parts)

    return data


main()
