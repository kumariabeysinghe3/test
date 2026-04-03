#create a random joke generator that will print a random joke from a list of jokes
import random
jokes = ["Why did the chicken cross the road? To get to the other side!",
         "Why is my Dad's name 'Father'? Because he is my Father!", 
         "Why did the dog get scared? Because he saw a ghost!" ]
print(random.choice(jokes))
