# from simhash import fnvhash
from hashlib import md5
import simhash
import re

"""
Splits the text in a list of k-grams
This is the first part of the simhash algorithm
Parameters:
s :The text that will be k-grammed
width (optional): The value of k
Returns:
list:The list with the k-grams
"""
def get_features(s,width=5):
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]
