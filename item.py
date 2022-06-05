import csv

# Parent class
class Item:
    # The pay rate after 20% discount 
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to receive arguments
        assert price >= 0, f"Price {price}  is not greater or equal to 0!"
        assert quantity >= 0, f"Quantity {quantity}  is not greater or equal to 0!"

        # Assign to self object 
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    # Decorator for convert this method into a Class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)  
            
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )  
    
    @staticmethod
    def is_integer(num):
        # Count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @property
    # Property decorator = read-only attribute
    def name(self):
        return self.__name

    @name.setter 
    def name(self, value):
        print("You are trying to set.")
        self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # Change the representation of the Items saved in all variable
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello someone
        We have {self.name} {self.quantity} times.
        Regards!
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
        print("Mail sent successfully")