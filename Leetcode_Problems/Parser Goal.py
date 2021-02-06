#https://leetcode.com/problems/goal-parser-interpretation/
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
def func(inp):
    word=""
    output=""
    for i in inp:
        word+=i
        if word=="G":
            output+="G"
            word=""
        elif word=="()":
            output+="o"
            word=""
        elif word=="(al)":
            output+="al"
    return output
print(func(inp="G()(al)"))
