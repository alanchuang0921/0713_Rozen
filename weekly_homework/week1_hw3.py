input_string =input("input string:")
# reversed_string=input_string[::-1]
# print("Reversed string:", reversed_string)
reversed= []
for i in input_string:
    reversed.insert(0,i)
reversed_string="".join(reversed)
print(reversed_string)