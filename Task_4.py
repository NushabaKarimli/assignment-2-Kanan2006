#import libraries here

def main():
        m=int(input("Enter the year [ex. 2021]: "))      
        if m>0:
            if (m-2000)%12==0:
                print(f"{m} is the year of the Dragon")
            elif (m-2001)%12==0:
                print(f"{m} is the year of the Snake")
            elif (m-2002)%12==0:
                print(f"{m} is the year of the Horse")
            elif (m-2003)%12==0:
                print(f"{m} is the year of the Sheep")
            elif (m-2004)%12==0:
                print(f"{m} is the year of the Monkey")
            elif (m-2005)%12==0:
                print(f"{m} is the year of the Rooster")
            elif (m-2006)%12==0:
                print(f"{m} is the year of the Dog")
            elif (m-2007)%12==0:
                print(f"{m} is the year of the Pig")
            elif (m-2008)%12==0:
                print(f"{m} is the year of the Rat")
            elif (m-2009)%12==0:
                print(f"{m} is the year of the Ox")
            elif (m-2010)%12==0:
                print(f"{m} is the year of the Tiger")
            elif (m-2011)%12==0:
                print(f"{m} is the year of the Hare")
        else:
            print("Invalid input!")
        pass

if __name__ == "__main__":
  main()
