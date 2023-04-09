

# # function to calculate the cost of a recipe
# def calculate_recipe_cost(recipe):
#     total_cost = 0
#     for ingredient, amount in recipe.items():
#         c.execute("SELECT cost FROM ingredients WHERE name=?", (ingredient,))
#         ingredient_cost = c.fetchone()[0]
#         total_cost += ingredient_cost * amount
#     return total_cost
#
# # sample recipe
# recipe = {
#     'flour': 2,
#     'sugar': 1,
#     'butter': 0.5
# }
#
# # calculate the cost of the recipe
# total_cost = calculate_recipe_cost(recipe)
#
# # print the result
# print("The total cost of the recipe is $", round(total_cost, 2))