"""Restaurant rating lister.

Read restaurnat name and rating from scores.txt
Store in a dictionary
Show ratings in alphabetical order

"""
#define function for rating restaurants
def rate_restaurants():
    ratings = open("scores.txt")

    restaurant_scores = {}
    
    for rating in ratings:
        restaurant_name, score = rating.rstrip().split(":")
        #dict_name[key] = value
        restaurant_scores[restaurant_name] = int(score)
    for restaurant_name, score in sorted(restaurant_scores.items()):
        print(f"{restaurant_name} has a score of {score}")



