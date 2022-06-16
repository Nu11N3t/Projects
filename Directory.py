#######################################################

# Name:       Kyle McMahon

# Class:      CIS-1400

# Assignment: Homework 14 spring 2021

# File:       Homework_14.py

# Purpose:    Car Class

#######################################################
print('                ***kyle mcmahon***\n');

People = 10;
totvacs = 4;

def main(i, Name, Names, Zips, Vacs, Vaccines):
    choice = 0;
    print("Welcome to the COVID Vaccine Tracking Program (CVTP)\n");
    print("please pick an item from the menu below\n");
    print("1. Enter a new record\n");
    print("2. Look for\edit an existing record\n");
    print("3. Run reporting logs\n");
    print("Enter to quit");
    choice = input("")
    if (choice == "1"):
        newRecord(i, Name,Names, Zips, Vacs, Vaccines);
    elif (choice == "2"):
        look_editRecord(i, Name, Names, Zips, Vacs, Vaccines);
    elif (choice == "3"):
        report(i, Name, Names, Zips, Vacs, Vaccines);
    elif (choice == ""):
        return;
    while (choice != "1" or choice != "2" or choice != "3"):
        print("please pick an item from the menu below\n");
        print("1. Enter a new record\n");
        print("2. Look for\edit an existing record\n");
        print("3. Run reporting logs\n");
        print("Enter t quit");
        choice = input("")
        if (choice == "1"):
            newRecord(i, Name, Names, Zips, Vacs, Vaccines);
        elif (choice == "2"):
            look_editRecord(i, Name, Names, Zips, Vacs, Vaccines);
        elif (choice == "3"):
            report(i, Name, Names, Zips, Vacs, Vaccines);
        elif (choice == ""):
            return;

def newRecord(i, Name, Names, Zips, Vacs, Vaccines):
    print(i);
    Name[i] = input("What is the persons name? (enter to exit) ");
    if (Name[i] == ""):
        main(i, Name, Names, Zips, Vacs, Vaccines);
    else:
        Names[i] = Name[i] + "'s"
        print("What is ", Names[i]," zip code?");
        Zips[i] = input();
        while (len(Zips[i]) > 5 or len(Zips[i]) < 5):
            Zips[i] = input("Zip codes can only be 5 numbers long try again");
        print("what vaccine did ", Name[i], " get if any? (p for Pfiser, m for moderna, j for johnson & johnson, or press enter for none) ");
        Vacs[i] = input(); 
        if (Vacs[i] == "p" or Vacs[i] == "m" or Vacs[i] == "j" or Vacs[i] == ""):
            if (Vacs[i] == "p"):
                Vaccines[i] = "Pfiser";
            elif (Vacs[i] == "m"):
                Vaccines[i] = "Moderna";
            elif (Vacs[i] == "j"):
                Vaccines[i] = "Johnson & Johnson";
            elif (Vacs[i] == ""):
                Vaccines[i] = "None";
            i = i + 1;
            main(i, Name, Names, Zips, Vacs, Vaccines);
        while (Vacs[i] != "p" or Vacs[i] != "m" or Vacs[i] != "j" or Vacs[i] != ""):
            Vacs[i] = input("Invalid selection please select from p, m, j, or press enter for none");
            if (Vacs[i] == "p"):
                Vaccines[i] = "Pfiser";
                i = i + 1;
                main(i, Name, Names, Zips, Vacs, Vaccines);
            elif (Vacs[i] == "m"):
                Vaccines[i] = "Moderna";
                i = i + 1;
                main(i, Name, Names, Zips, Vacs, Vaccines);
            elif (Vacs[i] == "j"):
                Vaccines[i] = "Johnson & Johnson";
                i = i + 1;
                main(i, Name, Names, Zips, Vacs, Vaccines);
            elif (Vacs[i] == ""):
                Vaccines[i] = "None";
                i = i + 1;
                main(i, Name, Names, Zips, Vacs, Vaccines);

def look_editRecord(i, Name, Names, Zips, Vacs, Vaccines):
    query = "";
    j = 0;
    found = False;
    update = "";
    query = input("Which record are you looking for? (input name of prson) ");
    if (query == ""):
        main(i, Name, Names, Zips, Vacs, Vaccines);
    else:
        while (found == False):
            while (j < People):
                if (query == Name[j]):
                    found = True;
                    print(Name[j]);
                    print("Zip code: ", Zips[j]);
                    print("Has vaccine: ", Vaccines[j]);
                    print("Would you like to update ", Names[j], " vaccine? (y/n) ");
                    update = input();
                    while (update != "y" or update != "n"): 
                        if (update == "y"):
                            print("Which Vaccine did ", Name[j], "get?");
                            Vacs[j] = input();
                            if (Vacs[j] == "p" or Vacs[j] == "m" or Vacs[j] == "j" or Vacs[j] == ""):
                                if (Vacs[j] == "p"):
                                    Vaccines[i] = "Pfiser";
                                    print("the record has been updated to show this");
                                    main(i, Name, Names, Zips, Vacs, Vaccines);
                                elif (Vacs[j] == "m"):
                                    Vaccines[j] = "Moderna";
                                    print("the record has been updated to show this");
                                    main(i, Name, Names, Zips, Vacs, Vaccines);
                                elif (Vacs[j] == "j"):
                                    Vaccines[j] = "Johnson & Johnson";
                                    print("the record has been updated to show this");
                                    main(i, Name, Names, Zips, Vacs, Vaccines);
                                elif (Vacs[j] == ""):
                                    Vaccines[j] = "None";
                                    print("the record has been updated to show this");
                                    main(i, Name, Names, Zips, Vacs, Vaccines);
                            while (Vacs[j] != "p" or Vacs[j] != "m" or Vacs[j] != "j" or Vacs[j] != ""):
                                Vacs[j] = input("Invalid selection please select from p, m, j, or press enter for none");
                                if (Vacs[j] == "p"):
                                    Vaccines[j] = "Pfiser";
                                    print("the record has been updated to show this");
                                    main(i, Name, Names, Zips, Vacs, Vaccines);
                                elif (Vacs[j] == "m"):
                                    Vaccines[j] = "Moderna";
                                    print("the record has been updated to show this");
                                    main(i, Name, Names, Zips, Vacs, Vaccines);
                                elif (Vacs[j] == "j"):
                                    Vaccines[j] = "Johnson & Johnson";
                                    print("the record has been updated to show this");
                                    main(i, Name, Names, Zips, Vacs, Vaccines);
                                elif (Vacs[j] == ""):
                                    Vaccines[j] = "None";
                                    print("the record has been updated to show this");
                                    main(i, Name, Names, Zips, Vacs, Vaccines);
                        elif (update == "n"):
                                main(i, Name, Names, Zips, Vacs, Vaccines);
                                j = j + 1;
                        update = input("Please choose between y/n");
                j = j + 1;
            if (found == False):
                print("invalid name no-one matches this name in the database");
                main(i, Name, Names, Zips, Vacs, Vaccines);

def report(i, Name, Names, Zips, Vacs, Vaccines):
    choice = 0;
    i = 0;
    j = 0;
    counter = 0;
    Results = [""] * totvacs;
    print("please select from of of the following options\n")
    print("1. Report by zip code\n");
    print("2. Full report");
    choice = input();
    if (choice == "1"):
        while (j < People):
            if (Vacs[j] == "p"):
                counter = counter + 1;
                counter1 = str(counter);
                Results[0] = Results[0] + counter1;
                j = j + 1
        counter = 0;
        j = 0; 
        while (j < People):
            if (Vacs[j] == "m"):
                counter = counter + 1;
                counter1 = str(counter);
                Results[1] = Results[1] + counter1;
                j = j + 1
        counter = 0;
        j = 0;
        while (j < People):
            if (Vacs[j] == "j"):
                counter = counter + 1;
                counter1 = str(counter);
                Results[2] = Results[2] + counter1;
                j = j + 1
        counter = 0;
        j = 0;
        while (j < People):
            if (Vacs[j] == ""):
                counter = counter + 1;
                counter1 = str(counter);
                Results[3] = Results[3] + counter1;
                j = j + 1
        counter = 0;
        j = 0;
        for i in range (0, len(Zips) - 1):
            for j in range (0, len(Zips) - 1 - i):
                if Zips[j] > Zips[j+1]:
                    Zips[j], Zips[j+1] = Zips[j+1], Zips[j];
                    Results[j], Results[j+1] = Results[j+1], Results[j];
        print(Zips[0], Results[0], Results[1]);
        print(Zips[1], Results[0], Results[1], Results[2], Results[3]);
        print(Zips[2], Results[0], Results[1], Results[2], Results[3]);
        print(Zips[3], Results[0], Results[1], Results[2], Results[3]);
        print(Zips[4], Results[0], Results[1], Results[2], Results[3]);
        print(Zips[5], Results[0], Results[1], Results[2], Results[3]);
        print(Zips[6], Results[0], Results[1], Results[2], Results[3]);
        print(Zips[7], Results[0], Results[1], Results[2], Results[3]);
        print(Zips[8], Results[0], Results[1], Results[2], Results[3]);
        print(Zips[9], Results[0], Results[1], Results[2], Results[3]);
        main(i, Name, Names, Zips, Vacs, Vaccines);
    elif (choice == "2"):
        while (j < People):
            if (Vacs[j] == "p"):
                counter = counter + 1;
                counter1 = str(counter);
                Results[0] = Results[0] + counter1;
                j = j + 1
        counter = 0;
        j = 0; 
        while (j < People):
            if (Vacs[j] == "m"):
                counter = counter + 1;
                counter1 = str(counter);
                Results[1] = Results[1] + counter1;
                j = j + 1
        counter = 0;
        j = 0;
        while (j < People):
            if (Vacs[j] == "j"):
                counter = counter + 1;
                counter1 = str(counter);
                Results[2] = Results[2] + counter1;
                j = j + 1
        counter = 0;
        j = 0;
        while (j < People):
            if (Vacs[j] == ""):
                counter = counter + 1;
                counter1 = str(counter);
                Results[3] = Results[3] + counter1;
                j = j + 1
        counter = 0;
        j = 0;
    print("pfiser, moderna, johnson & johnson, None");
    print(Results[0], Results[1], Results[2], Results[3]);
    main(i, Name, Names, Zips, Vacs, Vaccines);
        

main(i = 0, Name = [''] * People, Names = [''] * People, Zips = [''] * People, Vacs = [''] * People, Vaccines = [""] * People);
