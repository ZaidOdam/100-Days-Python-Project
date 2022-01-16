# import turtle
# timmy=turtle.Turtle()

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
temp = PrettyTable()
# temp.field_names=["Name", "Number"]
# temp.add_rows(
#     [
#         ["Zaid", '7744080417'],
#         ['Appe', '8999480460'],
#         ['Neha', '7447558259'],
#         ['Vinay', '9511874677']
#     ]
# )
# Or
temp.add_column("Name", ["Zaid", "Neha", "Vinay", "Appe"])
temp.add_column("Number", [7744080417, 7447558259, 9511874677, 8999480460])
temp.align = 'l'
print(temp)
