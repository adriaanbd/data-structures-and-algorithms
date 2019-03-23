# Halloween Party - HackerRank Challenge

# You wish to buy video games from the famous online video game store Mist.
# Usually, all games are sold at the same price, p, dollars
# However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. 
# Specifically, the first game you buy during the sale will be sold at p dollars
# but every subsequent game you buy will be sold at exactly d dollars less than the cost of the previous one you bought.
# This will continue until the cost becomes less than or equal to m dollars
# after which every game you buy will cost dollars each.
# For example, if p = 20, d = 3, and m = 6, then the following are the costs of the first 11 games you buy, in order:
# 20, 17, 14, 11, 8, 6, 6, 6, 6, 6, 6

# Input Format: The first and only line of input contains four space-separated integers p, d, m and s. 


def howManyGames(price: int, discount: int, lowest_price: int, budget: int) -> int:
  games = 0
  while can_purchase(price, budget):
    budget = make_purchase(price, budget)
    price = max(price - discount, lowest_price)
    games += 1
  return games

def make_purchase(price, budget):
  return budget - price

def can_purchase(price, budget):
  return budget - price >= 0

print(howManyGames(20, 3, 6, 85) == 7)
