from service.itemservice import ItemService

if __name__ == "__main__":
    service = ItemService()
    for row in service.find_all():
        print(row)
    del service
