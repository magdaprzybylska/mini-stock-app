from config import session
from models.order import Order

# class responsible for performing various order operations
class OrderService():

    def __init__(self, data):
        self.session = session
        self.table = Order.__tablename__
        self.data = data

    def add(self, id, transaction_type, price, quantity):
        new_order = Order( 
            id=id,
            transaction_type=transaction_type, 
            price=price, 
            quantity=quantity)
        self.session.add(new_order)
        self.session.commit()

    def remove(self, order_id):
        order_to_delete = self.session.query(Order).filter(Order.id==order_id).delete()
        self.session.commit()

    def process_csv(self):
        for index, row in self.data.iterrows():
            if row['Type'] == 'Add':
                self.add(id=row['Id'], transaction_type=row['Order'], price=row['Price'], quantity=row['Quantity'])
            else:
                self.remove(row['Id'])

    def get_best_deal(self, transaction_type):
        if transaction_type.capitalize() == "Sell":
            sell_objects = self.data[self.data['Order'] == 'Sell'].sort_values(by='Price', ascending=False)
            return sell_objects.head(1)
        elif transaction_type.capitalize() == "Buy":
            buy_objects = self.data[self.data['Order'] == 'Buy'].sort_values(by='Price', ascending=False)
            return buy_objects.head(1)
        else:
            return "Wrong order requested."