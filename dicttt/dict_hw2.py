school = {'1а': 20, '1б': 25, '2б': 22, '6а': 18, '7в': 15}

school['1а'] = 22

school['3в'] = 19

school.pop('2б')

total = sum(school.values())

print(school)
print("Всего учеников:", total)