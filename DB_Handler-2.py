import pymongo
import json

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
        def toSearch(self,userNameToSerach :str):
                try:
                        toSearchQuery = {"profileName":userNameToSerach}

                        data =collection_nameAndPw.find(toSearchQuery)

                        print("Type of return data is:",type(data))

                        return userNameToSerach
                except Exception as err:
                        print(err)
        def toUpate(self,profileName,NewName):
                try:
                        toUpdate = {'profileName':profileName}
                        name = {"$set":{'profileName':NewName}}
                        collection_nameAndPw.update_many(toUpdate,name)
                        print("Data Successfully updated!")

                except Exception as err:
                        print("Data Note Successfully updated!")
                        print(err)
if __name__ =="__main__":

        userNameToSerach = input("Please Enter a profile name to Update:")
        NewName = input("Enter New Name of Profile:")


        process=ToDelete(myquery)

        #data = process.toSearch(userNameToSerach)
        #print(data)
        process.print_data()
        process.toUpate(userNameToSerach,NewName)
        print("After Update")
        process.print_data()






