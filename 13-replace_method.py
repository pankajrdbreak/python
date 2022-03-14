name = input("Enter Your Name : ") 
date = input("Enter Date : ")
later = '''Conrats <|name|> you are selceted date <|date|>'''
later = later.replace("<|name|>",name)
later = later.replace("<|date|>",date)
print(later)