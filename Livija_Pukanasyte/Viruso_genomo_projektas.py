
import sys, os, re
import matplotlib.pyplot as plt
import numpy as np
import math
import re
import ctypes
from scipy.stats import entropy
from collections import Counter


with open("clx4rdrp.txt", "r") as file:
    valid = set("ACGT")
    s = file.read()
    for line in s:
        s = s.replace('\n', '')
    # print(s)


#sita vieta sutvarko teksta ir pavercia i substringus sekas

cleanstring = re.sub(r'[^ATGC>]', '', s)  #characters we want to replace, characters get raplaced to this, string
cleanstring = re.sub(r'[^ATGC>]', '>', s)
cleanstring = re.sub(r'>[A-Za-z]{1,3}>', '', cleanstring)  # \w reiskia bet kokia raidę 
cleanstring = re.sub(r'[^ATGC>]', '', cleanstring)  #characters we want to replace, characters get raplaced to this, string
cleanstring = re.sub(r'>+', '>', cleanstring)

substrings = cleanstring.split(">")
substrings = [x for x in substrings if x.strip()]
# print(substrings)

#sita vieta suteikia kintamuosius substringams

sequence_dictionary = {}

for i in range(len(substrings)):
    key = f"seq{i}"   # dynamic key name
    value = substrings[i]   # dynamic value from your list
    sequence_dictionary[key] = value

for name, seq in sequence_dictionary.items():
    # print(name, "=", seq)


#we will use this to access the sequence from the dictionary
    seq0 = sequence_dictionary["seq0"]
print(seq0)
