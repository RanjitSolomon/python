# functions with outpus

# Docstrings must be in the first line after the function definition


def format_names(fname, lname):
    """ Take a first and last name and format it 
        to return the title case version of the name.
    """
    if fname == "" or lname == ""
        return
    else:
        return (fname.title() + " " + lname.title())

fname = input("Enter your first name \n")
lname = input("Enter your last name \n")

print(format_names(fname, lname))
