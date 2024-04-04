#import libraries here

def main():
    m=str(input("Enter name of the month [ex. June]: "))
    d=int(input("Enter the day [ex. 5]: "))
    if m=="January" or m=="February" or m=="March":
        if m=="March":
            if d<20:
                print(f"{m} {d} is in Winter")
            else:
                print(f"{m} {d} is in Spring")
        else:
            print(f"{m} {d} is in Winter")
    elif m=="April" or m=="May" or m=="June":
        if m=="June":
            if d<21:
                print(f"{m} {d} is in Spring")
            else:
                print(f"{m} {d} is in Summer")
        else:
            print(f"{m} {d} is in Spring")
    elif m=="July" or m=="August" or m=="September":
        if m=="September":
            if d<22:
                print(f"{m} {d} is in Summer")
            else:
                print(f"{m} {d} is in Fall")
        else:
            print(f"{m} {d} is in Summer")
    elif m=="October" or m=="November" or m=="December":
        if m=="December":
            if d<21:
                print(f"{m} {d} is in Fall")
            else:
                print(f"{m} {d} is in Winter")
        else:
            print(f"{m} {d} is in Fall")
    else:
        print(f"The data entered is wrong.")
    pass

if __name__ == "__main__":
  main()
