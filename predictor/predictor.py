import random

class Predictor:

    def predict_age(min_age, max_age):
        age = random.randint(int(min_age), int(max_age))
        print("Your age is.. " + str(age) + "!")
        return age