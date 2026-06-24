#q1
#Zero-Shot Prompt
zero_shot= "Amit drives at 60 kmph for 9 hours. Aman drives at 90 kmph. Find Aman's time. "
print("Zero-Shot Answer: ",(60*9)/90, "hours ")
#One-Shot Prompt
one_shot = """
Ex:- Distanc=100km, Speed=50kmph,Time=2hours
Now solve:
Amit drives at 60 kmph for 9 hours.Aman drives at 90 kmph.
"""
print("One-Shot Answer: ",(60*9)/90, "hours")
#Few-Shot Prompt
Few_shot = """
Ex1:- 200 km, 50 kmph -> 4 hours
Ex2:- 300 km, 60 kmph -> 5 hours
Now solve:
Amit drives at 60 kmph for 9 hours.Aman drives at 90 kmph.
"""
print("Few-Shot Answer:",(60*9)/90, " hours ")
#Chain-Of-Thought
distance = 60*9
aman_time = distance /90
print("Chain-Of-Thought Answer: ",aman_time,"hours")