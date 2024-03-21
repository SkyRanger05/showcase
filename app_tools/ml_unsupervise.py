# -*- coding: "utf-8" -*-
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import sys


class UnSuper:

    def __init__(self):
        pass

    def blobs(self, samples: int, centers: int, random_state: int):
        X, y = make_blobs(n_samples=samples, centers=centers, random_state=random_state)
        print("From class UnSuper...Hawdeee!!!")

        return X, y

def main():
    
    print("From ML main...Hawdeee!!!")

fav = ["burrito", "nachos", "cervesas"]


if __name__ == "__main__":
    user_name = sys.argv[1]
    print("Directly run!")
    main()

else:
    print("Run via import.")
