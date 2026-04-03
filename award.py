time_swimming=int(input("How long did it take you to complete the swimming portion of the triathlon in minutes? "))
time_cycling=int(input("How long did it take you to complete the cycling portion of the trialthon in minutes?"))
time_running=int(input("How long did it take you to complete the running portion of the triathlon in minutes? "))
time_total= time_swimming + time_cycling +time_running
print(f"Your total time for the trialthon is {time_total} minutes.")
#award participant based on qualifying times 
if time_total <=100:
    print("Award: Provincial colours")
elif time_total>101 and time_total<105:
    print("Award: Provincial half colours")
elif time_total>106 and time_total<110:
    print("Award: Provincial scroll")
elif time_total>=111:
    print("Award: No award")

