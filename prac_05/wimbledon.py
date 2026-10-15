filename = "wimbledon.csv"
champion_wins = {}
countries = []

print("Wimbledon Champions: ")
with open(filename, "r", encoding="utf-8-sig") as in_file:
    lines = in_file.readlines()
    for line in lines[1:]:
        parts = line.split(",")
        champion_names = parts[2]
        champion_wins[champion_names] = champion_wins.get(champion_names, 0) + 1

        country = parts[1]
        if country not in countries:
            countries.append(country)

longest_name = max(len(name) for name in champion_wins.keys())
for name, count in champion_wins.items():
    print(f"{name:<{longest_name}} {count}")

print(f"\nThese {len(countries)} are Wimbledon Champions:")
print(", ".join(sorted(countries)))
