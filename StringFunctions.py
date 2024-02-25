str="i am a codder"
print(str.endswith("er"))
#this capitalize function does not change the original string value
print(str.capitalize())
print(str)
#if we wnat to change the original string
str=str.capitalize()
print(str)
"""if we want to replace any value with another value in a string then we use replace function
Syntax:str.replace("old value","new value")"""
print(str.replace("a","#"))
"""If we want to find any index value of a particular character or word then we use find function...
It basically returns the first ouucurance of teh char or word and returns -1 if not available"""
print(str.find("a"))
"""if we want to count any word or character then we use count function"""
print(str.count("d"))
