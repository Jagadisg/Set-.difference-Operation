Students of District College have a subscription to English and French newspapers.
Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to only English newspapers.
# Enter your code here. Read input from STDIN. Print output to STDOUT
total_eng = int(input())
std_no_eng = set([int(i) for i in input().split()])
total_frn = int(input())
std_no_frn = set([int(i) for i in input().split()])
print(len(std_no_eng.difference(std_no_frn)))

