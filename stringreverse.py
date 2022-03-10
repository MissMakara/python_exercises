#"Given an input string, reverse the string word by word."
string = "Give food to the fox"

x = string.split()
x.reverse()
print(x)
final_string =" "
# final_string =" ".join(map(str, x))
out = final_string.join(x)
print(out)