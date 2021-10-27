# lista de variedades de toppings

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms" ]

prices = [2, 6, 1, 3, 2, 7, 2]

#contar la cantidad de 2$

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#contar la cantidad de toppings
num_pizzas = len(toppings)

#imprimir un mensaje
print("We sell", num_pizzas, "differents kinds of pizza")

#lista 2D (toppings - prices)

pizzas_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchoives"],[2, "mushrooms"]]

print(pizzas_and_prices)

#sort.pizzas and pirces

pizzas_and_prices.sort()

#guardar el primer elemnto de pizzas and prices en otra variable

cheapest_pizza = pizzas_and_prices[0]

#guardar el ultimo valor de pizzprice en otra variable

priciest_pizza = pizzas_and_prices[-1]

#eliminar la pizza de anchoas

pizzas_and_prices.pop(6)

#añadir una nueva pizza

pizzas_and_prices.insert(4, [2.5, "peppers"])
print(pizzas_and_prices)

#lowes cost pizzas

three_cheapest = pizzas_and_prices[:3]
print(three_cheapest)
