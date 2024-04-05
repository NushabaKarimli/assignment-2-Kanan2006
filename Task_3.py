#import libraries here

def main():
    l=int(input("Enter the wavelength in nm: "))
    if l>=380 and l<450:
        print("The relevant color is Violet")
    elif l>=450 and l<495:
        print("The relevant color is Blue")
    elif l>=495 and l<570:
        print("The relevant color is Green")
    elif l>=570 and l<590:
        print("The relevant color is Yellow")
    elif l>=590 and l<620:
        print("The relevant color is Orange")
    elif l>=620 and l<=750:
        print("The relevant color is Red")
    else:
        print("Invalid input!")
    pass

if __name__ == "__main__":
  main()
