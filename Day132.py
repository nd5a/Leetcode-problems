# Find All Possible Recipes from Given Supplies

import collections

class Solution:
    def findAllRecipes(self, recipes, ingredients_list, supplies_list):
        dependencies = collections.defaultdict(list)
        supplies = set(supplies_list)
        for recipe, ingredients in zip(recipes, ingredients_list):
            dependencies[recipe] = ingredients

        WHITE = 0
        GRAY = 1
        BLACK = 2
        colours = collections.defaultdict(lambda: WHITE)
        cache = {}

        def can(recipe):
            if recipe in supplies:
                return True
            if colours[recipe] == BLACK:
                return cache[recipe]
            if recipe not in supplies and recipe not in dependencies:
                return False
            colours[recipe] = GRAY

            for ingredient in dependencies[recipe]:
                if colours[ingredient] == GRAY:
                    colours[recipe] = BLACK
                    cache[recipe] = False
                    return False
                if colours[ingredient] == BLACK and not cache[ingredient]:
                    colours[recipe] = BLACK
                    cache[recipe] = False
                    return False
                elif not can(ingredient):
                    colours[recipe] = BLACK
                    cache[recipe]= False
                    return False
            
            colours[recipe] = BLACK
            cache[recipe] = True
            return True
        
        ans = []
        for recipe in recipes:
            if can(recipe):
                ans.append(recipe)
        return ans