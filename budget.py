

class Category: 

    ## instantiations
    def __init__(self, name:str = "UNNAMED", budget: int = 0):
        self.name = name
        self.budget = budget
        self.available = budget
        self.transactions = []

    # concept ## updates the values in the function based on transactions list (you have to update the transactions list using functions)
    # def __call__(self, *args, **kwds):
        
    ## apply a transaction to this budget category
    def apply_transaction(self, transaction=None) : 
        if transaction == None: 
            return "ERROR: transaction does not exist"
        try: 
            if (str(transaction['category']) != self.name): 
                return "ERROR: transaction does not belong to this category"
            cost = float(transaction['amount'])
            self.transactions.append(transaction)
            self.available -= cost

        except: 
            print("ERROR RETRIEVING TRANSACTION AMOUNT, TRANSACTION DATA: ")
            print(transaction)

        

class Budget:
    def __init__(self):

        self.categories = []
    def add_category(self, category):
        if (str(category) not in self.categories): 
            self.categories.append(str(category))
            return None
        else: 
            return "ERROR: Category already exists, could not add category: " + category
    def remove_category(self, category): 
        if (str(category) in self.categories): 
            self.categories.remove(category)
            return None
        else: 
            return "ERROR: Category does not exist in list, could not remove category: " + category
        
    