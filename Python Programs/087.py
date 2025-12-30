#Write a function to merge three dictionaries into a single expression.
import collections as cln

def merge_three_dict(dict1, dict2, dict3):
    return dict(cln.ChainMap(dict1, dict2, dict3))
     
print(merge_three_dict({"name":"aniket", "age":22}, {"college":"PCCOE", "course":"MCA"}, {"location":"Pune"}))


