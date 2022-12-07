# Enter your code here. Read input from STDIN. Print output to STDOUT
total_eng = int(input())
std_no_eng = set([int(i) for i in input().split()])
total_frn = int(input())
std_no_frn = set([int(i) for i in input().split()])
print(len(std_no_eng.difference(std_no_frn)))

