import sys

s = "a"
p_index = []
for i in range(len(s)):
    p_index.append([i, i])

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        p_index.append([i, i + 1])

answer = ""
while len(p_index) != 0 :
    current_index = p_index[0]
    answer = s[current_index[0]:current_index[1] + 1]
    p_index.pop(0)
    if current_index[1] + 1 < len(s) and current_index[0] - 1 >= 0 and (s[current_index[0] - 1] == s[current_index[1] + 1]):
        p_index.append([current_index[0] - 1, current_index[1] + 1])
        if len(s[current_index[0] - 1:current_index[1] + 1]) > len(answer):
            answer = s[current_index[0] - 1:current_index[1] + 2]

print(answer)