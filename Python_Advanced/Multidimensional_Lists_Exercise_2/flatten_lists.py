line = input().split('|')

sub_list = []

for substr in line[::-1]:
    sub_list.extend(substr.split())

print(*sub_list)