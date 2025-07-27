statistics = {"users": {}, "languages": {}}

while (command := input()) != "exam finished":
    parts = command.split("-")
    username = parts[0]

    if parts[1] == "banned":
        statistics["users"].pop(username)
    else:
        language = parts[1]
        points = int(parts[2])

        if (username not in statistics["users"]
                or statistics["users"][username] < points):
            statistics["users"][username] = points

        if language not in statistics["languages"]:
            statistics["languages"][language] = 0
        statistics["languages"][language] += 1

print(f"Results:")
for username in statistics["users"]:
    print(f"{username} | {statistics['users'][username]}")

print(f"Submissions:")
for language in statistics["languages"]:
    print(f"{language} - {statistics['languages'][language]}")