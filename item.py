class Item:
    def __init__(self, item_name):
        self.itemname = item_name
        self.itemdescription = None
    
    def set_description(self, item_description):
        self.itemdescription = item_description
    
    def get_description(self):
        return self.itemdescription
    
    def set_name(self, new_name ):
        self.itemname = new_name

    def get_name(self):
        return self.itemname