"""Restaurant rating lister.

Read restaurnat name and rating from scores.txt
Store in a dictionary
Show ratings in alphabetical order

"""
#define function for rating restaurants
def rate_restaurants(ratings):
    ratings = open("scores.txt")

    restaurants_scores = {}
    
    for rating in ratings:
        name, score = rating.rstrip().split(":")
        #dict_name[key] = value
        restaurants_scores[name] = score
    
    restaurants_scores = sorted(restaurants_scores)
    print(f"{name} has a score of {score}")
    # return sorted(restaurants_scores)



