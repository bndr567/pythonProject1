ages = [1,2,3,4,5,66,7]
adults = []


def filtered_ages(ages):
 for age in ages:
  if age >= 1:
   adults.append(age)

print(filtered_ages(ages))