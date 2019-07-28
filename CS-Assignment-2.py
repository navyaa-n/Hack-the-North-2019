#---------------------------------------------------------------------
# Name:        <Assignment2> main.py
# Purpose:     <Program meets requirements of Assigment 2 criteria>
#
# Author:      <Navya Narukulla>
# Created:     <June.2.2019>
# Updated:     <June.8.2019>
#---------------------------------------------------------------------
import logging
import random
logging.basicConfig(filename='log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def menu():
  '''
    A menu of options for the program

    This function will print a list of program options

    Parameters
    ----------
    None
    
    Returns
    -------
    None

  '''
  print('MENU\n'.center(150, ' '))
  print("0. Exit\n".center(150, ' '))
  print('1. Grocery Store\n'.center(150, ' '))
  print('2. Shakespeare Quotes\n'.center(150, ' '))
  return

logging.debug('Start of grocery store')

def grocery():
  '''
    This function is a grocery store which uses user inputs to buy fruits, a main meal and dessert.

    Gives 3 options for each categories and for desserts, there is an option to add in your own dessert to the list. The final price is calculated and returned to the customer.

    Parameters
    ----------
    none

    Returns
    -------
    none

    Raises
    ------
    ValueError
      if input is not a number between 1 and 9
  '''
  print ("It's time to go grocery shopping")
  print ('You are in need of fruits, a main meal and dessert.')

  logging.debug('Fruits are listed')
  fruitList = {'apple':0.50, 'orange':0.70, 'guava':1.00}
  for key in fruitList:
    print(key)
  fruitInput = input('Which fruit would you like to buy? ') 
  logging.debug('User chose the fruit: ' + str(fruitInput))
  assert isinstance(fruitInput, str), 'Expecting a string'
  if fruitInput in fruitList:
    print('How many' + ' ' + str(fruitInput) + 's ' 'would you like to buy?, Choose any muber between 1 to 9. ')
  fruitNum = int(input())
  try: 
    if fruitNum < 1 or fruitNum > 9:
      raise Exception('Expecting a number from 1 to 9')
      
  except Exception as e:
      print('The following error occurred:' + str(e))
      return 


  logging.debug('User chose ' + str(fruitNum) + ' ' + str(fruitInput) + 's.')
  print('You have bought ' + str(fruitNum) + ' ' + str(fruitInput) + '(s).')

  logging.debug('Meals are listed')
  mealList = {'burrito':4.50, 'pasta':6.00, 'sandwich':3.50}
  for key in mealList:
    print(key)
  mealInput = input('Which meal would you like to buy? ')
  logging.debug('User chose the meal: ' + str(mealInput))
  if mealInput in mealList:
    print(str(mealInput)+ ' ' + 'tastes good!')

  logging.debug('Desserts are listed')
  dessertList = {'icecream':2.00, 'brownie':1.50, 'cake':5.00}
  for key in dessertList:
    print(key)
  extraDessert = input('Add a dessert of your choice to the list.')
  logging.debug('User added an extra dessert: ' + str(extraDessert))
  dessertList[str(extraDessert)] = 4.00
  logging.debug('New desserts are listed')
  for key in dessertList:
    print(key)
  dessertInput = input('Which dessert would you like to buy?')
  logging.debug('User chose the dessert: ' + str(dessertInput))
  if input == 'icecream'or 'brownie'or'cake'or str(extraDessert):
    print(str(dessertInput)+ ' ' + 'tastes good!')
  
  print('This is your reciept!')
  logging.debug('Cost of the fruits is calculated')

  fruitsPrice = float(fruitList[fruitInput])* int(fruitNum)
  
  print (fruitInput.upper() + '     $' + str(fruitsPrice))
  print (mealInput.upper() + '     $' + str(mealList[mealInput]))
  print (dessertInput.upper() + '     $' + str(dessertList[dessertInput]))
  logging.debug('Total price is calculated')
  totalPrice = dessertList[dessertInput] + mealList[mealInput] + dessertList[dessertInput]
  logging.debug('Total price is returned to the user')
  print ('TOTAL PRICE: $' + str(totalPrice))


def shakespeare():
  '''
    Macbeth character quotes

    This function's purpose is to give an example quote from the script of Macbeth of a few main characters. The user choose the charcter from a list given and the program reads the story.txt file and returns the corresponding quote of the character. 

    Parameters
    ----------
    none

    Returns
    -------
    str
      random quote of character chosen

    Raises
    ------
    ValueError
      if input is not a number between 1 and 5

  '''

  logging.debug('Start of shakespeare function')
  characters = ['1. Macbeth', '2. Lady Macbeth', '3. Banquo', '4. Duncan', '5. Macduff']
  logging.debug('List of characters is printed')
  for character in characters:
    print(character)
  charChosen = int(input("Which character's quote would you like to read? Type a number from 1 to 5. "))
  logging.debug('User chose a character')
  try: 
    if charChosen < 1 or charChosen > 5:
      raise Exception('Expecting a number from 1 to 5')
      
  except Exception as e:
      print('The following error occurred:' + str(e))
      return 
  
  logging.debug('Reading in story.txt')
  with open('story.txt', 'r') as file:
      lines = file.readlines()
  logging.debug('Done reading in story.txt')

  positions = []
  character = characters[int(charChosen)-1]
  character = character[3:]
  print(character + ': ')
  for index, item in enumerate(lines):
    if item.rstrip() == character.upper():
      positions.append(index)
  lineNum = random.choice(positions)+1
  logging.debug("Charcter's line is printed")
  print ('''"'''+ lines[lineNum] + " ' ")
  
 
logging.debug('Start of menu')
while True:
  menu()
  userInput = input('Please choose an option: ')
  if userInput == '1':
    grocery()
  if userInput == '2':
    shakespeare()
  if userInput == '0':
    logging.debug('End of program')
    break
  user = input('Would you like to return to the main menu? (y/n)')
  
  if user.lower() == 'n':
    break
