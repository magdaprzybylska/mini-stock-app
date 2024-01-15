# On every stock exchange trading is realized by making buy and sell orders with given price and quantity. 

# For example buying 100 Apple shares with price 55.0. Those orders can be: added and/or removed. 

# Having the following orders: 
# 1) create an object that stores them,
# 2) write a piece of code that in every step displays the sum of buy/sell orders with best price.

import pandas as pd

from models.base import Base
from config import engine
from services.order_service import OrderService

# creates orders.db if it doesn't exist yet
new_db = Base.metadata.create_all(engine)

data = pd.read_csv('orders-data.csv')   
order_service = OrderService(data)
order_service.process_csv()

# example code for choosing order with best selling price and calculating profit
best_sell = order_service.get_best_deal('Sell')
best_sale = best_sell['Price'].mul(best_sell['Quantity'])
print(best_sale)

# example code for choosing order with best buying price and calculating profit
best_buy = order_service.get_best_deal('Buy')
best_buying = best_buy['Price'].mul(best_buy['Quantity'])
print(best_buying)