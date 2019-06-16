class User(object):
    def __init__(self, name, email):
        self.name = name #string
        self.email = email #string
        self.books = {} #dictionary key=Book object value=user rating

    def get_email(self):
        #Returns email asociated with this user
        return self.email

    def change_email(self, address):
        #replaces this user's previous email with a new email address
        #and prints a message notifying a successful update
        self.email = address
        return print("The email address has been updated to: " + address)

    def __repr__(self):
        #prints user name, email, and number of books read
        if not self.books:
            return "User " + self.name + ", email: " + self.email + ", books read: 0"
        else:
            listbooks = list(self.books.keys())
            numbooks = len(listbooks)
            return "User " + self.name + ", email: " + self.email + ", books read: " + str(numbooks)

    def __eq__(self, other_user):
        #dunder (==) returns true if both users have same name and email
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self,book,rating=None):
        #adds a key:value pair to books where key=book and value=rating
        self.book = book #Book object
        self.rating = rating
        self.books.update({self.book : self.rating})

    def get_average_rating(self):
        #returns average rating for all of this user's books
        userratetotal = 0
        self.numratedbooks = 0
        if not self.books:
            return "You have not read any books."
        else:
            bklist = list(self.books.values())
            for each in bklist:
                if each == None:
                    pass
                else:
                    userratetotal += each
                    self.numratedbooks += 1
            if self.numratedbooks == 0:
                return "You have not rated any books."
            else:
                useravg = userratetotal / self.numratedbooks
                return useravg

#USERTESTS
#Mommy = User("Mommy","allo@gmail")
#print(Mommy.get_average_rating())
#print(Mommy)
#Mommy.read_book("BookABC",4)
#print(Mommy.get_average_rating())
#print(Mommy)
#Mommy.change_email("yeaaah@gmail")
#print(Mommy)
#Daddy = User("Mommy","yeaaah@gmail")
#Daddy == Mommy

class Book(object):
    def __init__(self,title,isbn):
        self.title = title #string
        self.isbn = isbn #number
        self.ratings = [] #list
        
    def get_title(self):
        #returns the title of the book
        return self.title

    def get_isbn(self):
        #returns isbn of the book
        return self.isbn
    
    def set_isbn(self,new_isbn):
        #replaces this book's previous isbn with a new isbn
        #and prints a message notifying a successful update
        self.isbn = new_isbn
        return print("The isbn number has been updated to: " + str(new_isbn))

    def add_rating(self,rating):
        #adds rating to list of ratings only if between 0 and 4
        #prints "Invalid Rating" otherwise
        self.rating = rating
        if self.rating <=4 and self.rating >=0:
            return self.ratings.append(self.rating)
        else:
            return print("Invalid Rating")
                     
    def __eq__(self, other_book):
        #dunder (==) returns True if both books have same title and isbn
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
                     
    def get_average_rating(self):
        #returns average rating for this book
        self.total = 0
        if not self.ratings:
            return "This book has not been rated."
        else:
            for each in self.ratings:
                self.total += each
            return self.total / len(self.ratings)
    def __repr__(self):
        return self.title
                
    def __hash__(self):
        #makes this object hashable
        return hash((self.title, self.isbn))

#BOOKTESTS
#GOT = Book("A Song of Ice and Fire",64567547)
#print(GOT.get_title())
#print(GOT.get_isbn())
#GOT.set_isbn(93729472)
#print(GOT.get_average_rating())
#GOT.add_rating(4)
#print(GOT.get_average_rating())
#HP = Book("Goblet of Fire", 243532532)
#GOT == HP
#HP = Book("A Song of Ice and Fire",93729472)
#GOT == HP

class Fiction(Book):
    def __init__(self,title,author,isbn):
        super().__init__(title,isbn)
        self.author = author #string
        
    def get_author(self):
        #returns the author
        return self.author        
    def __repr__(self):
        #returns the string: "{title} by {author}"
        return self.title + " by " + self.author      

class Non_Fiction(Book):
    def __init__(self,title,subject,level,isbn):
        super().__init__(title,isbn)
        self.subject = subject #string (ex. Geology)
        self.level = level #string (ex. advanced)
        
    def __repr__(self):
        #returns the string: "{title}, a {level} manual on {subject}"
        return self.title + ", a " + self.level + " manual on " + self.subject

class TomeRater:
    def __init__(self):
        self.users = {} #dictionary user email:user
        self.books = {} #dictionary book object:number of users who have read
    def __repr__(self):
        # Return list of user and a list of their respective books read
        final_string = ""
        if not self.users:
            return "No Users Exist"
        for user in list(self.users.values()):
            small_string = ""
            uname = user.name
            if not user.books:
                small_string += "NO BOOKS READ"
            else:
                for ubook in user.books:
                    if small_string == "":
                        small_string += ("" + ubook.title)
                    else:
                        small_string += (", " + ubook.title)
            if final_string == "":
                final_string += uname
            else:
                final_string += ("\n" + uname)
            final_string += (": " + small_string)  
        return final_string
    def __eq__(self,other_rater):
        same = 1
        if not self.users and not other_rater.users and not self.books and not other_rater.books:
            pass
        elif not self.users and not other_rater.users:
            if not self.books or not other_rater.books:
                same = 0
            else:
                self_bk_keys = list(self.books.keys())
                other_bk_keys = list(other_rater.books.keys())
                self_bk_vals = list(self.books.values())
                other_bk_vals = list(other_rater.books.values())
                if len(self_bk_keys) != len(other_bk_keys):
                    same = 0
                else:
                    for num in range(len(self_bk_keys)):
                        if self_bk_keys[num] == other_bk_keys[num]:
                            pass
                        else:
                            same = 0
                    for num in range(len(self_bk_keys)):
                        if self_bk_vals[num] == other_bk_vals[num]:
                            pass
                        else:
                            same = 0
        elif not self.books and not other_rater.books:
            if not self.users or not other_rater.users:
                same = 0
            else:
                self_usr_keys = list(self.users.keys())
                other_usr_keys = list(other_rater.users.keys())
                self_usr_vals = list(self.users.values())
                other_usr_vals = list(other_rater.users.values())
                if len(self_usr_keys) != len(other_usr_keys):
                    same = 0
                else:
                    for num in range(len(self_usr_keys)):
                        if self_usr_keys[num] == other_usr_keys[num]:
                            pass
                        else:
                            same = 0
                    for num in range(len(self_usr_keys)):
                        if self_usr_vals[num] == other_usr_vals[num]:
                            pass
                        else:
                            same = 0
        else:
            if not self.users or not self.books or not other_rater.users or not other_rater.books:
                same = 0
            else:
                self_bk_keys = list(self.books.keys())
                other_bk_keys = list(other_rater.books.keys())
                self_bk_vals = list(self.books.values())
                other_bk_vals = list(other_rater.books.values())
                if len(self_bk_keys) != len(other_bk_keys):
                    same = 0
                else:
                    for num in range(len(self_bk_keys)):
                        if self_bk_keys[num] == other_bk_keys[num]:
                            pass
                        else:
                            same = 0
                    for num in range(len(self_bk_keys)):
                        if self_bk_vals[num] == other_bk_vals[num]:
                            pass
                        else:
                            same = 0
                self_usr_keys = list(self.users.keys())
                other_usr_keys = list(other_rater.users.keys())
                self_usr_vals = list(self.users.values())
                other_usr_vals = list(other_rater.users.values())
                if len(self_usr_keys) != len(other_usr_keys):
                    same = 0
                else:
                    for num in range(len(self_usr_keys)):
                        if self_usr_keys[num] == other_usr_keys[num]:
                            pass
                        else:
                            same = 0
                    for num in range(len(self_usr_keys)):
                        if self_usr_vals[num] == other_usr_vals[num]:
                            pass
                        else:
                            same = 0
        if same == 1:
            return True
        elif same == 0:
            return False
    def create_book(self,title,isbn):
        #creates a new book with this title and isbn
        #returns the book object
        self.title = title
        self.isbn = isbn
        NewBook = Book(self.title, self.isbn)
        self.books.update({NewBook:0})
        return NewBook
    def create_novel(self,title,author,isbn):
        #creates a new Fiction with this title,author, and isbn
        #returns Fiction object
        self.title = title
        self.author = author
        self.isbn = isbn
        NewNovel = Fiction(self.title,self.author,self.isbn)
        self.books.update({NewNovel:0})
        return NewNovel
    def create_non_fiction(self,title,subject,level,isbn):
        #creates a new non-fiction with this title,subject,level, and isbn
        #returns Non_Fiction object
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn
        NewNonFiction = Non_Fiction(self.title,self.subject,self.level,self.isbn)
        self.books.update({NewNonFiction:0})
        return NewNonFiction
    def add_book_to_user(self,book,email,rating=None):
        #using this email, if the user exists, it should:
            #call read_book in User with this book and rating
            #call add_rating in Book with this book and rating
            #check if the book object already exists in Books
                #if not, add book to self.books in User with 1 user having read it
                #if so, add 1 to number of users having read this book
        #if this user does not exist, return: "No user with email {email}!"
        self.book = book #Book object
        self.email = email
        self.rating = rating
        if self.email in self.users:
            self.users[self.email].read_book(self.book,self.rating)
            if not self.rating:
                pass
            else:
                self.book.add_rating(self.rating)
            if self.book in self.books:
                #print(self.book)
                #print(list(self.books.keys()))
                #print(list(self.books.values()))
                self.books[self.book] += 1
                #its finding Alice In Wonderland in list pulled from dictionary.keys() but not in dictionary format
                #print(list(self.books.values()))
            else:
                self.books[self.book] = 1
        else:
            return print("No user with the email: " +self.email)
        
    def add_user(self,name,email,user_books = None):
        #creates a new user with this name and email
        #if user_books is provided, each book should be added using add_book_to_user
        self.name = name
        self.email = email
        self.user_books = user_books #list of Book objects
        NewUser = User(self.name, self.email)
        self.users.update({self.email:NewUser})
        if not self.user_books:
            pass
        else:
            for each in self.user_books:
                self.add_book_to_user(each,self.email)
    def print_catalog(self):
        #prints each key from self.books in TomeRater
        return print(list(self.books.keys()))
    def print_users(self):
        #prints each value in self.users in TomeRater
        return print(list(self.users.values()))
    def most_read_book(self):
        #returns the name of the book that has been read the most from self.books in TomeRater
        if not self.books:
            return "No books have been added."
        else:
            self.readnum = list(self.books.values())[0]
            self.mostread = list(self.books.keys())[0]
            for self.key, self.value in self.books.items():
                if self.value > self.readnum:
                    self.readnum = self.value
                    self.mostread = self.key
            return self.mostread.title + " has been read the most: Read " + str(self.readnum) + " times."
    def highest_rated_book(self):
        #returns the name of the highest rated book from self.books
        #using book.get_average_rating
        if not self.books:
            return "No books have been added."
        else:
            self.bestbk = list(self.books.keys())[0]
            self.avgrate = self.bestbk.get_average_rating()
            self.bestavgrate = self.avgrate
            for self.eachbook in list(self.books.keys()):
                self.avgrate = self.eachbook.get_average_rating()
                if isinstance(self.avgrate, str) == True:
                    #Do not compare
                    pass
                elif self.avgrate > self.bestavgrate:
                    self.bestavgrate = self.avgrate
                    self.bestbk = self.eachbook
            if isinstance(self.bestavgrate, str) == True:
                return "No books have been rated."
            else:
                return self.bestbk.title + " is the highest rated book with a value of " + str(self.bestavgrate) + "."
    def most_positive_user(self):
        #returns the user with the highest average rating from self.users
        #using user.get_average_rating()
        if not self.users:
            return "No users have been added."
        else:
            self.mostpos = list(self.users.values())[0]
            self.avgrate = self.mostpos.get_average_rating()
            self.bestavgrate = self.avgrate
            for self.eachuser in list(self.users.values()):
                self.avgrate = self.eachuser.get_average_rating()
                if isinstance(self.avgrate, str) == True:
                    #Do not compare
                    pass
                elif self.avgrate > self.bestavgrate:
                    self.bestavgrate = self.avgrate
                    self.mostpos = self.eachuser
            if isinstance(self.bestavgrate, str):
                return "No books have been rated."
            else:
                return self.mostpos.name + " is the most positive user with an average rating of " + str(self.bestavgrate) + "."     

##TESTS
Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
#print("ADD USER 1")
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
#print("ADD USER 2")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
#print("ADD USER 3")
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
#print("ADD BOOK TO USER 1")
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
#print("ADD BOOK TO USER 2")
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
#print("ADD BOOK TO USER 3")
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
#print("ADD BOOK TO USER 4")
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
#print("ADD BOOK TO USER 5")
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
#print("ADD BOOK TO USER 6")
Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
#print("ADD BOOK TO USER 7")
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
#print("ADD BOOK TO USER 8")
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
print("CATELOG:")
Tome_Rater.print_catalog()
print("USERS:")
Tome_Rater.print_users()
print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())

#Get Creative!
# __repr__
#returns "User_Name: Book_read_by_user_1, Book_read_by_user_2, ..."
print(Tome_Rater)
# __eq__ and create BOBODY to compare
BOBODY = TomeRater()
book1 = BOBODY.create_book("Society of Mind", 12345678)
novel1 = BOBODY.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = BOBODY.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = BOBODY.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = BOBODY.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = BOBODY.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)
#print("ADD USER 1")
BOBODY.add_user("Alan Turing", "alan@turing.com")
#print("ADD USER 2")
BOBODY.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
#print("ADD USER 3")
BOBODY.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
#print("ADD BOOK TO USER 1")
BOBODY.add_book_to_user(book1, "alan@turing.com", 1)
#print("ADD BOOK TO USER 2")
BOBODY.add_book_to_user(novel1, "alan@turing.com", 3)
#print("ADD BOOK TO USER 3")
BOBODY.add_book_to_user(nonfiction1, "alan@turing.com", 3)
#print("ADD BOOK TO USER 4")
BOBODY.add_book_to_user(nonfiction2, "alan@turing.com", 4)
#print("ADD BOOK TO USER 5")
BOBODY.add_book_to_user(novel3, "alan@turing.com", 1)
#print("ADD BOOK TO USER 6")
BOBODY.add_book_to_user(novel2, "marvin@mit.edu", 2)
#print("ADD BOOK TO USER 7")
BOBODY.add_book_to_user(novel3, "marvin@mit.edu", 2)
#print("ADD BOOK TO USER 8")
BOBODY.add_book_to_user(novel3, "david@computation.org", 4)
#Compare
print(Tome_Rater == BOBODY)






        
