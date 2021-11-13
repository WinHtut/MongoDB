import pymongo

connection=pymongo.MongoClient("localhost",27017)
database = connection["my_db1"]
collection_nameAndPw = database["nameAndPw"]
myquery ={"hint":"unknowuser"}

class ToDelete:
        def __init__(self,myquery):
                self.toDelete= myquery
        def delete(self):
                try:
                        data = collection_nameAndPw.delete_one(self.toDelete)
                        print("Deleted Documents:", data.deleted_count)

                except Exception as err:
                        print(err)
        def print_data(self):
                try:
                        all_data = collection_nameAndPw.find()
                        for i in all_data:
                                print(i)
                except Exception as err:
                        print(err)

if __name__ =="__main__":

        process=ToDelete(myquery)
        print("Before Delete:")
        process.print_data()
        process.delete()

        print("After delete data:")
        process.print_data()

