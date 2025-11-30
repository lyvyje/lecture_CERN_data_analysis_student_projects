import re
with open("clx4rdrp.txt", "r") as file:
    # valid = set("ACGT")
    s = file.read()
    # for line in s:
    s = s.replace('\n', '')


# >\w\w>
# # [] means match any character from this list, ^ means NOT and r' means do not treat / as special characters, take them literally
cleanstring = re.sub(r'[^ATGC>]', '>', s)
cleanstring = re.sub(r'>[A-Za-z]{1,3}>', '', cleanstring)  # \w reiskia bet kokia raidę 
cleanstring = re.sub(r'[^ATGC>]', '', cleanstring)  #characters we want to replace, characters get raplaced to this, string
cleanstring = re.sub(r'>+', '>', cleanstring)  #characters we want to replace, characters get raplaced to this, string
# print(cleanstring)
# Substringing a string (knowing when to slice)

x = cleanstring.split(">")

for i, v in enumerate(x):
    print(x)
    if (v == "" or v == "\n"): # if checks kad nebūtų nuancų dėl tuščių chars ar naujų eilučių simbolių \n
        continue
    # print('\n')
    # print(v)
    

