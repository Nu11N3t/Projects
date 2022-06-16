#######################################################

# Name:       Kyle McMahon

# Class:      CIS-1400

# Assignment: Homework 14 spring 2021

# File:       Homework_14.py

# Purpose:    Car Class

#######################################################
print('                ***kyle mcmahon***\n');

class Car:
    def __init__(self):
        self.make = '';


    def yearModel(self):
        return 0;


    def speed(self):
        return 0;


    def set_make(self, make1):
        self.make = make1;


    def get_make(self):
        return self.make;


    def set_yearModel(self, yearModel):
        self.yearModel = yearModel;


    def get_yearModel(self):
        return self.yearModel;


    def accelerate(self, speed):
        self.speed = speed + 5;


    def brake(self, speed):
        self.speed = speed - 5;


def main():
    a = Car();
    make1 = input('What is the make of your car? ');
    a.set_make(make1);

    yearModel = int(input('What is the year of your car? '));
    a.set_yearModel(yearModel);

    print('Your car is a', a.get_make());
    print("Your car's year of make is", a.get_yearModel());

    speed = 0;
    i = 0;
    while (i < 5):
        a.accelerate(speed);
        speed = a.speed;
        print("you're speed is: ",a.speed, "MPH");
        i = i + 1;

    print("Slow down.");

    i = 0;
    while (i < 5):
        a.brake(speed);
        speed = a.speed;
        print("you're speed is: ",a.speed, "MPH");
        i = i + 1;
    print("You've stopped.");
main();
