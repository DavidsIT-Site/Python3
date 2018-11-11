import easygui as eg

# Autogenerated with DRAKON Editor 1.31

def basics_sort():
    #item 498
    print("sorting a list does not change the list, a new list is returned")
    
    a = [5, 1, 4, 3]
    print(sorted(a))  ## [1, 3, 4, 5]
    print(a)  ## [5, 1, 4, 3]
    #item 501
    print("sorting can take optional arguments and works with any iterable collection")
    
    strs = ['aa', 'BB', 'zz', 'CC']
    print(sorted(strs))  
    print(sorted(strs, reverse=True))
    #item 502
    print("For example, you can sort by length")
    strs = ['ccc', 'aaaa', 'd', 'bb', 'CC']
    print(sorted(strs, key=len))
    #item 509
    print("To pass a custom function in, create the function. and pass it in")
    print("sort_function1 returns the last value in a string")
    strs = ['xc', 'zb', 'yd' ,'wa']
    print(sorted(strs, key=sort_function1)) ## ['wa', 'zb', 'xc', 'yd']


def class_ex_main():
    #item 302
    mw1 = MoneyWaster()
    mw1.set_account(10)
    mw1.spend(100)


def control_flow_main():
    #item 346
    """ demonstration of control flows in drakon """
    #item 345
    if_statement()
    #item 347
    select_flow(1)
    select_flow("one")
    select_flow(3)
    select_flow("3")
    #item 450
    print("_"*56)


def demo_multichoice(title):
    #item 596
    """ Popup a demo multichoice window """
    #item 593
    question = "This is your question"
    #item 594
    listOfOptions = ["option 1", "option 2", "option 3"]
    #item 592
    choice = eg.multchoicebox(question, title, listOfOptions)
    #item 595
    return(choice)


def dialogs_main():
    #item 614
    demo_multichoice("Siji")
    while_multichoice()
    #item 626
    print("DO WHILE DEMO")
    do_while_loop()


def dict_formatting():
    #item 570
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
    #item 563
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
        #item 566
        print(key)


def dict_main():
    #item 572
    print("_"*56)
    #item 562
    dict_hash_table()
    #item 573
    print("_"*56)
    #item 571
    dict_formatting()


def do_while_loop():
    #item 625
    """This is the demonstration of a do-while loop."""
    while True:
        #item 619
        
        ans = demo_multichoice("do while  loop demo")
        print(ans)
        #item 620
        if ans:
            pass
        else:
            break
        #item 622
        print("""This code path is being executed; it will loop again """)
    #item 621
    print("This code path is being executed, it will not loop again")


def foreach_loop(items_list):
    #item 284
    """This is the demonstration of a foreach loop;
     it will also serve to for expansion to print a list"""
    for my_item in items_list:
        #item 289
        print(my_item)


def if_statement():
    #item 393
    speed = 100
    #item 390
    if speed > 80:
        #item 395
        print("Have a nice day")
    else:
        #item 394
        print("Going to jail")


def list_comprehension2():
    #item 540
    
    strs = ['hello','universe']
    shout_strs = [pos.upper() + '!!!' for pos in strs]
    print(shout_strs)
    
    print("conditional list comprehension")
    nums = [2, 4, 188, 20, 5]
    small_enough = [ n for n in nums if n <= 100 ]
    print(small_enough)


def list_comprehensions_squares(my_passed_list):
    #item 532
    """syntax: [ expr for var in list ] -- the for var in list """
    #item 533
    squares = [ number*number for number in my_passed_list ]
    return squares


def list_methods():
    #item 465
    """ Working with common list methods """
    #item 457
    people_list = ['larry', 'curly', 'moe']
    
    #building on earlier loops work
    #print current list of people
    foreach_loop(people_list) 
    
    print("Adding a single element to the end of the list")
    people_list.append('david')
    #unlike all of the other people in this code; you are important
    #Make your name caps
    people_list.append('David')
    #item 466
    #I really meant to add Myself at the front of the list
    print("Inserting into a list at a particular location")
    people_list.insert(0,'David')
    print(people_list)
    #item 467
    #Now, I'm in the list multiple times
    print("removing elements from list")
    people_list.remove('david')
    print(people_list)
    #item 468
    #now, I'm only in the list twice
    
    people_list.pop(4)
    print(people_list)
    #item 481
    print("end of list methods; swear this is running")


def list_slices():
    #item 499
    """list slices methods demo"""
    #item 482
    print("Slices seem to work on lists & strings ")
    list = ['a', 'b', 'c', 'd']
    print(list[1:-1])   ## ['b', 'c']
    list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
    print(list)        ## ['z', 'c', 'd']


def lists_main():
    #item 463
    list_methods()
    #item 485
    print("_"*56)
    #item 472
    list_slices()
    #item 484
    print("_"*56)
    #item 531
    nums = [1,2,3,4]
    print(list_comprehensions_squares(nums))
    
    list_comprehension2()
    #item 534
    print("_"*56)


def loops_demo():
    #item 296
    """ Displays foreach, while, and do-while loops """
    #item 293
    print("FOREACH DEMO")
    fruits = ['apples', 'cherries', 'pears']
    foreach_loop(fruits)
    #item 451
    print("FOREACH DEMO 2")
    fruits = ['larry', 'curly', 'moe']
    foreach_loop(fruits)
    #item 294
    print("WHILE DEMO")
    #while_loop()
    #item 470
    print("_"*56)


def main():
    #item 544
    """ This is the main, edits here change what runs """
    #getting started http://drakon-editor.sourceforge.net/python/python.html#classes
    #item 545
    string_main()
    #item 546
    control_flow_main()
    #item 548
    loops_demo()
    #item 547
    lists_main()
    #item 549
    sorting_main()
    #item 550
    tuples_main()
    #item 561
    dict_main()
    #item 585
    pattern_main()
    #item 615
    dialogs_main()


def pattern1():
    #item 586
    print("Pattern1")
    from pampy import match, HEAD, TAIL, _
    
    x = [1, 2, 3]
    
    match(x, [1, TAIL],     lambda t: t)            # => [2, 3]
    
    print(match(x, [HEAD, TAIL],  lambda h, t: (h, t)))    # => (1, [2, 3])
    #item 587
    input = x
    pattern = [1,2,_]
    action = lambda x:	print("it's {}".format(x))
    match(input,pattern,action)


def pattern_main():
    #item 588
    """https://github.com/santinic/pampy"""
    #item 584
    pattern1()


def select_flow(input_state):
    #item 416
    """ select from multiple compute paths by switching with on an input """
    #item 4010001
    if input_state == 0:
        #item 411
        print("number 0")
    else:
        #item 4010002
        if input_state == "one":
            #item 412
            print("one")
        else:
            #item 4010003
            if input_state == 3:
                #item 413
                print("3")
            else:
                #item 415
                print("unknown state")


def sort_function1(s):
    #item 510
    """returns the last value in a string"""
    #item 508
    return s[-1]


def sorting_main():
    #item 500
    """The 'main' for running sorting demo"""
    #item 497
    basics_sort()
    #item 528
    print("_"*56)


def string_basic_hello():
    #item 429
    """ This is a demonstration of printing text """
    #item 428
    print("""
    
    Hello Universe; 
    	This is for fun, understanding
    	& does not include any promises
    
    """)


def string_basics1():
    #item 421
    """ Basic manipulation of strings (with other types) """
    #item 422
    # variable s stores the string "hello universe"
    s = "hello universe"
    #item 423
    # get the length of the variable s, and print it
    
    print(len(s))
    #item 424
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
    #item 433
    """ Basic methods that operate on objects that are strings """
    #item 434
    # this are the strings we will be working with
    S1 = "Siji is here"
    S2 = "3.14"
    #item 435
    # returns an upper or lowercase version of the string
    print(S1.lower())
    print(S1.upper())
    #item 436
    # returns an upper or lowercase version of the string with no spaces
    
    print((S1.replace('a',"      ")).upper())
    #item 446
    print("_"*56)


def string_basics3():
    #item 440
    """ demonstration of string slices """
    # slice [start:end]
    s3 = "SIJI IS HERE"
    print(s3[5:7])
    print(s3[3:])
    print(s3[:2])
    #item 447
    print("_"*56)


def string_main():
    #item 310
    """ This is the main python file for demonstrating the string methods """
    #item 316
    string_basic_hello()
    #item 309
    string_basics1()
    #item 329
    string_basics2()
    #item 379
    string_basics3()


def string_pretty_print1():
    #item 444
    """ example adding data to print strings """
    #item 445
    text =  "%d people are valid. Watch us, %s, try" % (0,"billions")
    #item 448
    print("_"*56)


def tuples_basics():
    #item 520
    """ tuples are n dimensional groups of elements, the size is immutable """
    #item 521
    print("tuples can be accessed just like a list")
    my_tuple = (1,2,'hello','David')
    print(my_tuple)
    print(my_tuple[1])
    print("Single elements inside tuples can not be updated; the entire block needs to be re-assigned")
    my_tuple = (1,2,'hello','MartinMaker')
    print(my_tuple)
    #item 530
    #Easy assigning var names with tuples
    (choice1, choice2, chosen_greeting, player_name) = (1,2,'hello','MartinMaker')
    print(chosen_greeting)


def tuples_main():
    #item 519
    tuples_basics()
    #item 529
    print("_"*56)


def while_loop():
    #item 280
    """This is the demonstration of a while loop.
    Comment this out; it's infinite
    """
    #item 274
    ans = 1
    while True:
        #item 275
        if ans:
            pass
        else:
            break
        #item 277
        print("""This code path is being executed """)
        ans = "while loop demo"
        print(ans)
    #item 276
    print("This code path is being executed, it will not loop again")


def while_multichoice():
    #item 608
    """This is the demonstration of a while loop."""
    #item 602
    ans = 1
    while True:
        #item 603
        if ans:
            pass
        else:
            break
        #item 605
        print("""This code path is being executed """)
        ans = demo_multichoice("while loop demo")
        print(ans)
    #item 604
    print("This code path is being executed, it will not loop again")

class MoneyWaster:


    def set_account(self, value):
        #item 213
        self.account_worth = value


    def set_name(self, name):
        #item 207
        self.name = name


    def spend(self, value):
        #item 220
        print("pre spend")
        print(value)
        print(self.account_worth)
        #item 219
        self.account_worth = self.account_worth - value
        #item 221
        print("post spend")
        print(value)
        print(self.account_worth)

main()
