from service.baseservice import BaseService
from dao.itemdao import ItemDao

class ItemService (BaseService):
    def __init__(self):
        self.dao = ItemDao()
        
    def find_all(self):
        return self.dao.find_all()
    