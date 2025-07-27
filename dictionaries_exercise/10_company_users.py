company_dict = {}

while (command := input()) != "End":
    company, employee = command.split(" -> ")

    if company not in company_dict.keys():
        company_dict[company] = []
    if employee in company_dict[company]:
        continue

    company_dict[company].append(employee)

for company,employees in company_dict.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")