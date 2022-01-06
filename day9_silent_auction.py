import os
from auction_art import logo

flag=True
people={}
while flag:
  print(logo)
  name=input("What is your name?: ")
  bid=int(input("What is your bid?: $"))
  people[name]=bid
  choice=input("Are there any other bidders? Type 'yes' or 'no': ")
  if choice=="no":
    flag=False
  os.system('cls')

max=0
name=""
for key in people:
  if max<people[key]:
    max=people[key]
    name=key
print(f"The winner is {name} with a bid of ${max}")


#Excercise

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades={}
# for key in student_scores:
#   marks=student_scores[key]
#   if marks>90:
#     student_grades[key]="Outstanding"
#   elif marks>80:
#     student_grades[key]="Exceeds Expectations"
#   elif marks>70:
#     student_grades[key]="Acceptable"
#   else:
#     student_grades[key]="Fail"
# print(student_grades)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country,visit,cities):
#   dict1={}
#   dict1["country"]=country
#   dict1["visits"]=visit
#   dict1["cities"]=cities
#   travel_log.append(dict1)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)





