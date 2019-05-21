import requests
from random import randint

topic = input("Let me tell you a joke! Give me a topic: ")

# Request
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()


# Count quantity of jokes in chosen topic
jokes_quantity = len(res["results"])
result = res["results"]

if jokes_quantity > 1:
    print(f"I've got {jokes_quantity} jokes about {topic}, Here's one: ")
    # Print random joke
    print(result[randint(0, jokes_quantity)]["joke"])

elif jokes_quantity == 1:
    print(f"I've got one joke about {topic}, Here it is: ")
    # Print one joke
    print(result[0]["joke"])
else:
    print(f"Sorry I don't have any jokes about {topic}! Please try again.")



