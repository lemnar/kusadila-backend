

class Category: 

    ## instantiations
    def __init__(self, name:str = "---", budget:any = "---", id:str = ""):
        self.name = name
        self.budget = budget
        self.available = budget
        self.activity = []
        self.id = id

    def setActivity(self, activities=[]):
        cost = 0
        if activities is []: 
            return "ERROR: activity list is empty"
        self.activity = []
        for transaction in activities: 
            try: 
                cost += float(transaction['amount'])
                self.activity.append(transaction)
            except: 
                print("ERROR RETRIEVING TRANSACTION AMOUNT, TRANSACTION DATA: ")
                print(transaction)
        if self.budget == "---":
            return
        self.available = self.budget - cost

class Budget:
    def __init__(self):
        self.budget = 0
        self.available = 0
        self.categories = []


    # creates categories from a list of objects of form {name, budget, available, activity}
    def setCategories(self, categories):
        self.available = self.budget
        self.categories = []
        for cat in categories: 
            # try:
            catobj = Category(cat['name'], cat['budget'], cat['id'])
            catobj.setActivity(cat['activity'])
            self.categories.append(catobj)
            # except: 
            #     print("Category ", cat, "is not in the correct form")

    def getCategories(self, dictForm: bool = True):
        if dictForm: 
            return [i.__dict__ for i in self.categories]
        return self.categories
    
        
## test setup
sex = {'name': 'sex', 'amount': '23'}
liq = {
    'name': 'Liqour',
    'amount': '730'
}
C = Category("main", 300)
budget = Budget()
budget.setCategories([C.__dict__])