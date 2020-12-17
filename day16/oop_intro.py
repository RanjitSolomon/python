# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/labs/lab01/colors
# https://pypi.org/


from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# go to pypi.prg and search for "prettytable" and install the pakage.
# File - settings - project folder - interpreter - click the "+" to add "install"

from prettytable import PrettyTable
# to see the source code, right click on "prettytable" and Go to implementation
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikcachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
print(table)

table2 = PrettyTable()
table2.add_column("Pokemon Name", ["Pikcachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])
table2.align = "l"
print(table2)