#import libraries here

def main():
  m=str(input("Enter a month [ex. March]: "))
  d=int(input("Enter the day [ex. 12]: "))
  if d>0:
      if m=="January":
          if d<20:
              print("Your zodiac sign is Capricorn")
          elif d>=20 and d<=31:
              print("Your zodiac sign is Aquarius")
          else:print("Either a month or a day is invalid!")
      elif m=="February":
          if d<19:
              print("Your zodiac sign is Aquarius")
          elif d>=19 and d<=29:
              print("Your zodiac sign is Pisces")
          else:
              print("Either a month or a day is invalid!")
      elif m=="March":
          if d<21:
              print("Your zodiac sign is Pisces")
          elif d>=21 and d<=31:
              print("Your zodiac sign is Aries")
          else:
              print("Either a month or a day is invalid!")
      elif m=="April":
          if d<20:
              print("Your zodiac sign is Aries")
          elif d>=20 and d<=30:
              print("Your zodiac sign is Taurus")
          else:
              print("Either a month or a day is invalid!")
      elif m=="May":
          if d<21:
              print("Your zodiac sign is Taurus")
          elif d>=21 and d<=31:
              print("Your zodiac sign is Gemini")
          else:
              print("Either a month or a day is invalid!")
      elif m=="June":
          if d<21:
              print("Your zodiac sign is Gemini")
          elif d>=21 and d<=30:
              print("Your zodiac sign is Cancer")
          else:
              print("Either a month or a day is invalid!")
      elif m=="July":
          if d<23:
              print("Your zodiac sign is Cancer")
          elif d>=23 and d<=31:
              print("Your zodiac sign is Leo")
          else:
              print("Either a month or a day is invalid!")
      elif m=="August":
          if d<23:
              print("Your zodiac sign is Leo")
          elif d>=23 and d<=31:
              print("Your zodiac sign is Virgo")
          else:
              print("Either a month or a day is invalid!")
      elif m=="September":
          if d<23:
              print("Your zodiac sign is Virgo")
          elif d>=23 and d<=30:
              print("Your zodiac sign is Libra")
          else:
              print("Either a month or a day is invalid!")
      elif m=="October":
          if d<23:
              print("Your zodiac sign is Libra")
          elif d>=23 and d<=31:
              print("Your zodiac sign is Scorpion")
          else:
              print("Either a month or a day is invalid!")
      elif m=="November":
          if d<22:
              print("Your zodiac sign is Scorpion")
          elif d>=22 and d<=30:
              print("Your zodiac sign is Sagittarius")
          else:
              print("Either a month or a day is invalid!")
      elif m=="December":
          if d<22:
              print("Your zodiac sign is Sagittarius")
          elif d>=22 and d<=31:
              print("Your zodiac sign is Capricorn")
          else:
              print("Either a month or a day is invalid!")
      else:
          print("Either a month or a day is invalid!")
  else:
      print("Either a month or a day is invalid!")
  pass

if __name__ == "__main__":
  main()
