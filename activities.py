

class Activities(): 
    def __init__(self):
        self.activity = []

    def getFromCategory(self, category):
        return_list = []
        for transaction in self.activity: 
            try: 
                if transaction['category'] == category: 
                    return_list.append(transaction)
            except: 
                print("Transaction does not have a 'category' section")
        return return_list