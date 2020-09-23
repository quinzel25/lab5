from peewee import *

db = SqliteDatabase('catch.sqlite')

class Catches(Model):
    name = CharField()
    country = CharField()
    num_of_catches = IntegerField()


    class Meta:
        database = db

    def __str__(self):
        return f'Name: {self.name} | Country: {self.country} | Chaninsaws Caught: {self.num_of_catches}'

db.connect()
db.create_tables([Catches])

# sample data

# janne = Catches(name="Janne Mustonen", country="Finland", num_of_catches=98)
# janne.save()

# ian = Catches(name="Ian Stewart", country="Canada", num_of_catches=94)
# ian.save()

# aaron = Catches(name="Aaron Gregg", country="Canada", num_of_catches=88)
# aaron.save()

# chad = Catches(name="Chad Taylor", country="USA", num_of_catches=78)
# chad.save()

#return



def find_all():
    
    print('All Things in DB')
    findAll = Catches.select()
    for x in findAll:
        print(x)


def add_new_holder():
    nameInput = input('Enter Holder\'s name: ')
    countryInput = input('Enter Holder\'s country: ' )
    catches = input('Enter Holder\'s amount of catches: ')

    add = Catches(name=nameInput, country=countryInput, num_of_catches=catches)
    add.save

    print(f'{nameInput} has been entered into the database')

def delete_holder():
    name = input('Enter name to be deleted: ')
    row_deleted = Catches.delete().where(Catches.name == name).execute()
    print('Rows delted:', row_deleted)

def search():
    name = input('Enter name to search: ')

    search = Catches.select().where(Catches.name == name)
    for x in search:
        print(x)

def update_holder(): 

    nameInput = input('Enter name to update cathced: ')
    catchesInput = input('Enter amount of catches: ')

    change = Catches.update(num_of_catches=catchesInput).where(Catches.name == nameInput)
    change.execute()

    print(f'{nameInput} amount of catches has changed to {catchesInput}')

def main():
    print('Welcome to Chainsaw Database!')
    
    print('1. Add Holder')
    print('2. Search Holder')
    print('3. Update Holder')
    print('4. View All Holder')
    print('5. Delete Holder')
    print('6. Quit')

    menu = input('Enter choice: ')
    print(menu)
    if menu == 1:
        add_new_holder()
    if menu == 2:
        search()
    if menu == 3:
        update_holder()
    if menu == 4:
        find_all()
    if menu == 5:
        delete_holder()
    if menu == 6:
        print('bye')
        
      
            

if __name__ == '__main__':
    main()