import pandas as pd
import os


class ProdIncom:
    filepath = 'data/'
    if os.path.exists(filepath + 'out.csv'):
        income_expense = pd.read_csv(rf"{filepath}out.csv", sep=';', converters={'date': str, 'product':str, 'price':float, 'quantity':int})
    else:
        income_expense = pd.DataFrame(columns=['date', 'product', 'price', 'quantity'])

    def help(self):
        print('text: receive product price quantity  -- receiving')
        print('text: sell product price quantity     -- selling')
        print('text: goods_list                    -- list of incoming and outgoing item')
        print('text: n_goods product                 -- quantity of selected item')
        print('text: expenses                        -- cost of purchasing items')
        print('text: income                          -- cost of sold items')
        print('text: profit                          -- shop profit')
        print('text: report days                     -- shop profit')
        print('text: exit                            -- to exit')

    def _is_correct(self, price, quantity):
        try:
            float(price)
        except ValueError:
            print("Input wrong price type")
            return
        try:
            int(quantity)
        except ValueError:
            print("Input wrong quantity type")
            return

    def exit(self):
        exit()

    def receive(self, product, price, quantity):
        self._is_correct(price, quantity)
        price = float(price)
        quantity = int(quantity)
        today = pd.to_datetime('today').date()
        df = pd.DataFrame({'date': today, 'product': [product], 'price': [price], 'quantity': [quantity]})
        self.income_expense = pd.concat([self.income_expense, df])
        self._safe_data()

    def _safe_data(self):
        if not os.path.exists(self.filepath):
            os.makedirs(self.filepath)
        self.income_expense.to_csv(self.filepath + 'out.csv', sep=";", index=False)
        print('changes saved')

    def goods_list(self):
        print(self.income_expense)

    def sell(self, product, price, quantity):
        self._is_correct(price, quantity)
        price= float(price)
        quantity = int(quantity)
        if quantity <= self.product_quantity(product):
            self.receive(product, price, -quantity)
        else:
            print(f"Not enough {product}: Available = {self.product_quantity(product)}/{quantity}")

    def report(self, n):
        if not (n.isdigit()):
            print("Input wrong type")
        else:
            today = pd.to_datetime('today').date()
            start = today - pd.offsets.Day(int(n))
            s = pd.date_range(start, today, freq='D').to_series()
            time_list = []
            for i in s:
                time_list.append(i.strftime("%Y-%m-%d"))
            df_selected = self.income_expense[self.income_expense['date'].isin(time_list)]
            exp = round((df_selected[df_selected['quantity'] > 0]['quantity'] *
                         df_selected[df_selected['quantity'] > 0]['price']).sum(), 2)
            print(f"Our expenses last {n} days = {exp}")
            inc = round(-(df_selected[df_selected['quantity'] < 0]['quantity'] *
                          df_selected[df_selected['quantity'] < 0]['price']).sum(), 2)
            print(f"Our income for last {n} days = {inc}")
            prof = round(-(df_selected['quantity'] * df_selected['price']).sum(), 2)
            print(f"Our profit for last {n} days = {prof}")

    def n_goods(self, product):
        print(self.product_quantity(product))

    def product_quantity(self, product):
        quantity = self.income_expense[self.income_expense['product'] == product]['quantity'].sum()
        return quantity

    def expenses(self):
        exp = round((self.income_expense[self.income_expense['quantity'] > 0]['quantity'] *
                     self.income_expense[self.income_expense['quantity'] > 0]['price']).sum(), 2)
        print(f"Our expenses for the whole time = {exp}")

    def income(self):
        inc = round(-(self.income_expense[self.income_expense['quantity'] < 0]['quantity'] *
                      self.income_expense[self.income_expense['quantity'] < 0]['price']).sum(), 2)
        print(f"Our income for the whole time = {inc}")

    def profit(self):
        prof = round(-(self.income_expense['quantity']*self.income_expense['price']).sum(), 2)
        print(f"Our profit for the whole time = {prof}")


if __name__ == '__main__':

    my_store = ProdIncom()
    while True:
        action = input("Take action ")
        if action.find(' ') == -1:
            if hasattr(my_store, action):
                getattr(my_store, action)()
            else:
                print("action unavailable")
        else:
            arg = (action.split(' ')[0])
            prop = (action.split(' ')[1:])
            if hasattr(my_store, arg):
                getattr(my_store, arg)(*prop)
            else:
                print("action unavailable")
