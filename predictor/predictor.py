import random
import os

class Predictor:

    def predict_age(min_age, max_age):
        age = random.randint(int(min_age), int(max_age))
        printf("Your age is.. " + str(age) + "!")
        return age