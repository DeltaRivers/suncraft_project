
this_thing = ["a", "b", "c"]

string1 = ""
for i in this_thing:
    string1 += "He "
print(string1)

def samething(input):
    string2 = ""
    for i in input:
        string2 += "Ho "
    return string2
print(samething(this_thing))