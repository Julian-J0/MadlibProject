from random import randint
uinput = input("Choose from 1-2 or type random: " )
def story_1():
  Title_1 = input("Input a title: ")
  Name_1 = input("Input a name: ")
  Adjective_1 = input("Input an adjective: ")
  Group_1 = input("Input a group, ex. soldiers: ")
  Verbed_1 = input("Input a verb ending in -ed: ")
  Feeling_1 = input("Input a feeling: ")
  Verb_1 = input("Insert a verb ending with s: ")
  print ("Story 1:")
  print ("Once upon a time, there was a (", Title_1,"). Their name was (", Name_1, "), and they were (", Adjective_1,"). They had (", Group_1, ") full of people and they were they were (", Name_1, ") to command. One day, they (", Verbed_1, ") all day long as training, and they felt (", Feeling_1, ")about it. They ended their day doing (", Verb_1, "). The End!")

def story_2():
  MrMs_2 = input("Enter Mr or Ms: ")
  Lname_2 = input("Input a last name:")
  Adjective_2 = input("Input an adjective: ")
  Verb_2 = input("Input a verb ending with -ing: ")

  print ("Story 2:")
  print ("Hello (", MrMs_2,")(", Lname_2, "), We are writing to you to inform you about your childs(", Adjective_2, ")behavior. While we are aware that you have limited time, we suggest that you start(", Verb_2, ")with your child so they can build more character. Thank you (", MrMs_2,")(", Lname_2, "), have a good day." )

def randomc():
  rando = randint(1,2);
  print (rando)
  if rando == 1:
    return (story_1())
  elif rando == 2:
    return (story_2())


def u_choice():
  if uinput == ("1"):
   return (story_1());
  elif uinput ==("2"):
    return (story_2());
  elif uinput ==("R"):
    return (randomc());
  else:
    print (input("Please enter 1-2 or (R)andom "));
u_choice()