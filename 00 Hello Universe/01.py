import easygui as eg

# Autogenerated with DRAKON Editor 1.31

def _item_remove():
    """cleanup from drakon for easy code reading!  ignore me!"""
    import os
    
    me = os.getcwd()+r'\01.py'
    file_of_me = open(me)
    content = file_of_me.readlines()
    file_of_me.close()
    
    import re
    
    new_code = []
    
    for txt in content:
    
    		new_code.append(txt)
    
    file_of_me = open(me,'w')
    for txt in new_code:
    	file_of_me.write(str(txt))


def basics_sort():
    print("sorting a list does not change the list, a new list is returned")
    
    a = [5, 1, 4, 3]
    print(sorted(a))  ## [1, 3, 4, 5]
    print(a)  ## [5, 1, 4, 3]
    print("sorting can take optional arguments and works with any iterable collection")
    
    strs = ['aa', 'BB', 'zz', 'CC']
    print(sorted(strs))  
    print(sorted(strs, reverse=True))
    print("For example, you can sort by length")
    strs = ['ccc', 'aaaa', 'd', 'bb', 'CC']
    print(sorted(strs, key=len))
    print("To pass a custom function in, create the function. and pass it in")
    print("sort_function1 returns the last value in a string")
    strs = ['xc', 'zb', 'yd' ,'wa']
    print(sorted(strs, key=sort_function1)) ## ['wa', 'zb', 'xc', 'yd']


def control_flow_main():
    """ demonstration of control flows in drakon """
    if_statement()
    select_flow(1)
    select_flow("one")
    select_flow(3)
    select_flow("3")
    print("_"*56)


def customer_class_main():
    cust1 = customer("Poor_David")
    cust2 = customer("Rich_David",100)
    print(cust1)
    cust2.send_funds(cust1,10)
    print(cust1)
    cust1.withdrawal(5)
    cust1.withdrawal(5)
    cust1.withdrawal(5)


def demo_multichoice(title):
    """ Popup a demo multichoice window """
    question = "This is your question"
    listOfOptions = ["option 1", "option 2", "option 3"]
    choice = eg.multchoicebox(question, title, listOfOptions)
    return(choice)


def dialogs_main():
    demo_multichoice("Siji")
    while_multichoice()
    print("DO WHILE DEMO")
    do_while_loop()


def dict_formatting():
    print("dict formatting")
    person = {}
    person['name'] = 'David'
    person['age'] = ' old enough'
    person['sex'] = 'yes'
    person['number'] = 42
    
    s_person = ("""
    This person is: %(name)s 
    	is: %(age)s
    	Sex: %(sex)s
    	number: %(number)d""" 
    % person)
    
    print(s_person)
    print(person)
    print("removing items from dictionaries is the same as lists")
    del person['number']
    print(person)


def dict_hash_table():
    print("dicts are hash table structures key:value")
    dict = {}
    dict['a'] = 'alpha'
    dict['g'] = 'gamma'
    dict['o'] = 'omega'
    print(dict)
    print(dict['a'])
    print("""print(dict['z']) ERROR""")
    if 'z' in dict: print(dict['z']  )
    print( dict.get('a'))
    print( dict.get('z'))
    
    for k in dict.items():
    	print(k)
    
    for key, value in dict.items():
    	print(key +': ' +value)
    for key in dict:
        print(key)


def dict_main():
    print("_"*56)
    dict_hash_table()
    print("_"*56)
    dict_formatting()
    print("_"*56)


def do_while_loop():
    """This is the demonstration of a do-while loop."""
    while True:
        
        ans = demo_multichoice("do while  loop demo")
        print(ans)
        if ans:
            pass
        else:
            break
        print("""This code path is being executed; it will loop again """)
    print("This code path is being executed, it will not loop again")


def foreach_loop(items_list):
    """This is the demonstration of a foreach loop;
     it will also serve to for expansion to print a list"""
    for my_item in items_list:
        print(my_item)


def if_statement():
    speed = 100
    if speed > 80:
        print("Have a nice day")
    else:
        print("Going to jail")


def introduction_main():
    """ This is the introduction main, edits here change what runs """
    #getting started http://drakon-editor.sourceforge.net/python/python.html#classes
    string_main()
    control_flow_main()
    #loops_demo()
    lists_main()
    sorting_main()
    tuples_main()
    dict_main()
    pattern_main()
    #dialogs_main()
    customer_class_main()


def list_comprehension2():
    
    strs = ['hello','universe']
    shout_strs = [pos.upper() + '!!!' for pos in strs]
    print(shout_strs)
    
    print("conditional list comprehension")
    nums = [2, 4, 188, 20, 5]
    small_enough = [ n for n in nums if n <= 100 ]
    print(small_enough)


def list_comprehensions_squares(my_passed_list):
    """syntax: [ expr for var in list ] -- the for var in list """
    squares = [ number*number for number in my_passed_list ]
    return squares


def list_methods():
    """ Working with common list methods """
    people_list = ['larry', 'curly', 'moe']
    
    #building on earlier loops work
    #print current list of people
    foreach_loop(people_list) 
    
    print("Adding a single element to the end of the list")
    people_list.append('david')
    #unlike all of the other people in this code; you are important
    #Make your name caps
    people_list.append('David')
    #I really meant to add Myself at the front of the list
    print("Inserting into a list at a particular location")
    people_list.insert(0,'David')
    print(people_list)
    #Now, I'm in the list multiple times
    print("removing elements from list")
    people_list.remove('david')
    print(people_list)
    #now, I'm only in the list twice
    
    people_list.pop(4)
    print(people_list)
    print("end of list methods; swear this is running")


def list_slices():
    """list slices methods demo"""
    print("Slices seem to work on lists & strings ")
    list = ['a', 'b', 'c', 'd']
    print(list[1:-1])   ## ['b', 'c']
    list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
    print(list)        ## ['z', 'c', 'd']


def lists_main():
    list_methods()
    print("_"*56)
    list_slices()
    print("_"*56)
    nums = [1,2,3,4]
    print(list_comprehensions_squares(nums))
    
    list_comprehension2()
    print("_"*56)


def loops_demo():
    """ Displays foreach, while, and do-while loops """
    print("FOREACH DEMO")
    fruits = ['apples', 'cherries', 'pears']
    foreach_loop(fruits)
    print("FOREACH DEMO 2")
    fruits = ['larry', 'curly', 'moe']
    foreach_loop(fruits)
    print("WHILE DEMO")
    #while_loop()
    print("_"*56)


def main():
    _item_remove()
    #introduction_main()
    msqli_main()


def msqli_main():
    print("entering sql")
    mysql_create_drop_table()
    mysql_create_insert()
    mysql_read()


def mysql_create_drop_table():
    import sqlite3
    # Create a database in RAM
    dbr = sqlite3.connect(':memory:')
    # Creates or opens a file called mydb with a SQLite3 DB
    dbd = sqlite3.connect('mydb')
    cursor = dbd.cursor()
    cursor.execute('''
        CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                           phone TEXT, email TEXT unique, password TEXT)
    ''')
    dbd.commit()
    print("table created")
    cursor = dbd.cursor()
    cursor.execute('''DROP TABLE users''')
    dbd.commit()
    print("table dropped")
    dbr.close()
    dbd.close()


def mysql_create_insert():
    import sqlite3
    
    dbd = sqlite3.connect('mydb2')
    cursor = dbd.cursor()
    cursor.execute('''DROP TABLE users''')
    cursor.execute('''
        CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                   phone TEXT, email TEXT unique, password TEXT)
    ''')
    dbd.commit()
    print("table created")
    cursor = dbd.cursor()
    name1 = 'David'
    phone1 = '7064523484'
    email1 = 'David@DavidsIT.Site'
    # A very secure password
    password1 = 'Flanagan'
     
    name2 = 'Poor_David'
    phone2 = '6783696707'
    email2 = 'david@example.com'
    password2 = 'password'
    
    
    # Insert user 1
    cursor.execute('''INSERT INTO users(name, phone, email, password)
                      VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
    print('First user inserted')
     
    # Insert user 2
    cursor.execute('''INSERT INTO users(name, phone, email, password)
                      VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
    print('Second user inserted')
     
    dbd.commit()
    
    dbd.close()


def mysql_read():
    import sqlite3
    dbd = sqlite3.connect('mydb2')
    cursor = dbd.cursor()
    
    
    cursor.execute('''SELECT name, email, phone, password FROM users''')
    for row in cursor:
        # row[0] returns the first column in the query (name), row[1] returns email column.
        print('{0} - {3} : {1}, {2}'.format(row[0], row[1], row[2],row[3]))
    
    dbd.close()


def pattern1():
    print("Pattern1")
    from pampy import match, HEAD, TAIL, _
    
    x = [1, 2, 3]
    
    match(x, [1, TAIL],     lambda t: t)            # => [2, 3]
    
    print(match(x, [HEAD, TAIL],  lambda h, t: (h, t)))    # => (1, [2, 3])
    input = x
    pattern = [1,2,_]
    action = lambda x:	print("it's {}".format(x))
    match(input,pattern,action)


def pattern2():
    """ searching thru text for a particular pattern with regex: phone number example """
    text = """My number is (706)-452-3484; text anytime;
    this ad will go away when the offer has been filled;
    I have another number, in a slightly different format: (678)-369 6707\n"""
    
    print(text)
    import re
    
    #'\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'  if not raw string escape char
    phone_num_regex = re.compile(r'\+?1?\s*\(?-*\.*(\d{3})\)?\.*-*\s*(\d{3})\.*-*\s*(\d{4})$')
    matched_objects = phone_num_regex.search(text)
    print(matched_objects.group())


def pattern_main():
    """https://github.com/santinic/pampy"""
    pattern1()
    pattern2()
    print("_"*56)


def select_flow(input_state):
    """ select from multiple compute paths by switching with on an input """
    if input_state == 0:
        print("number 0")
    else:
        if input_state == "one":
            print("one")
        else:
            if input_state == 3:
                print("3")
            else:
                print("unknown state")


def sort_function1(s):
    """returns the last value in a string"""
    return s[-1]


def sorting_main():
    """The 'main' for running sorting demo"""
    basics_sort()
    print("_"*56)


def string_basic_hello():
    """ This is a demonstration of printing text """
    print("""
    
    Hello Universe; 
    	This is for fun, understanding
    	& does not include any promises
    
    """)


def string_basics1():
    """ Basic manipulation of strings (with other types) """
    # variable s stores the string "hello universe"
    s = "hello universe"
    # get the length of the variable s, and print it
    
    print(len(s))
    # working with strings and numbers
    
    text = 'The value of pi is ' 
    pi = 3.14
    print(text)
    print(pi)
    
    #TypeError: can only concatenate str (not "float") to str
    #print(text+pi) 
    
    print(text+str(pi))
    print("_"*56)


def string_basics2():
    """ Basic methods that operate on objects that are strings """
    # this are the strings we will be working with
    S1 = "Siji is here"
    S2 = "3.14"
    # returns an upper or lowercase version of the string
    print(S1.lower())
    print(S1.upper())
    # returns an upper or lowercase version of the string with no spaces
    
    print((S1.replace('a',"      ")).upper())
    print("_"*56)


def string_basics3():
    """ demonstration of string slices """
    # slice [start:end]
    s3 = "SIJI IS HERE"
    print(s3[5:7])
    print(s3[3:])
    print(s3[:2])
    print("_"*56)


def string_main():
    """ This is the main python file for demonstrating the string methods """
    string_basic_hello()
    string_basics1()
    string_basics2()
    string_basics3()


def string_pretty_print1():
    """ example adding data to print strings """
    text =  "%d people are valid. Watch us, %s, try" % (0,"billions")
    print("_"*56)


def tuples_basics():
    """ tuples are n dimensional groups of elements, the size is immutable """
    print("tuples can be accessed just like a list")
    my_tuple = (1,2,'hello','David')
    print(my_tuple)
    print(my_tuple[1])
    print("Single elements inside tuples can not be updated; the entire block needs to be re-assigned")
    my_tuple = (1,2,'hello','MartinMaker')
    print(my_tuple)
    #Easy assigning var names with tuples
    (choice1, choice2, chosen_greeting, player_name) = (1,2,'hello','MartinMaker')
    print(chosen_greeting)


def tuples_main():
    tuples_basics()
    print("_"*56)


def while_loop():
    """This is the demonstration of a while loop.
    Comment this out; it's infinite
    """
    ans = 1
    while True:
        if ans:
            pass
        else:
            break
        print("""This code path is being executed """)
        ans = "while loop demo"
        print(ans)
    print("This code path is being executed, it will not loop again")


def while_multichoice():
    """This is the demonstration of a while loop."""
    ans = 1
    while True:
        if ans:
            pass
        else:
            break
        print("""This code path is being executed """)
        ans = demo_multichoice("while loop demo")
        print(ans)
    print("This code path is being executed, it will not loop again")

class customer:


    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance


    def __repr__(self):
        return("%s has balance: %d" % (self.name, self.balance))


    def send_funds(self, send_to, amount_to_send):
        if amount_to_send > self.balance:
            print("too poor")
            #custom error not enough money
        else:
            self.balance = self.balance - amount_to_send
            send_to.balance = send_to.balance + amount_to_send
            print("%s has succesfully sent %s: %d"%(self.name, send_to.name, amount_to_send))


    def set_account_balance(self, account_balance):
        self.account_worth = account_balance


    def set_name(self, name):
        self.name = name


    def withdrawal(self, amount_withdrawal):
        if amount_withdrawal > self.balance:
            print("%s's does not have enough balance. No withdrawal"% self.name)
            #custom error not enough money
        else:
            self.balance = self.balance - amount_withdrawal
            print("%s succesful withdrawl. Remaining balance: %d"% (self.name, self.balance))

main()
