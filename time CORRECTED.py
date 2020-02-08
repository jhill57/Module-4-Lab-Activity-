#this code was edited by Jordan on 2/8/2020
#this code is like an alarm clock

currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)
