first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

""" 
The f letter stands for format, these are Format Strings because python replaces the 
variable in the braces with their value 

==========================


you can also use format strings to compose complete messages
"""
print(f"hello, {full_name.title()}!")



"""
You can also assign the format string to a new variable to make the final print 
call much simpler
"""

message = f"hello, {full_name.title()}!"
print(message)