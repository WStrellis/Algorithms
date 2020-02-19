#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients, batches=0) -> int:
    can_make = True
    for k in recipe:
        try:
            if recipe[k] <= ingredients[k]:
                ingredients[k] -= recipe[k]
            else:
                can_make = False
                break
        except:
            can_make = False
            break
    if can_make:
        return recipe_batches(recipe, ingredients, batches + 1)
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
