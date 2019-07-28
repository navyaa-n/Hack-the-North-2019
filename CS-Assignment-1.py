#-----------------------------------------------------------------------------
# Name:        <Assignment 1> (Assignment1.py)
# Purpose:     <To meet requirements of assignment 1>
#
# Author:      <Navya Narukulla>
# Created:     <March-28-19>
# Updated:     <April-05-19>
#-----------------------------------------------------------------------------

import random

def RPSGame():
  """
  rock, paper, scissors, game with CPU
  
  warnings
  --------
  program will only work if the userChoice matches one of the choices which are in RPSOptions
  
  """

  RPSOptions = ['rock', 'paper', 'scissors']
  CPUMove = random.choice(RPSOptions)
  print('Its Rock Paper Scissors! You are playing against the CPU!')
  userChoice = input('What move will you make? ')
  
  # assert userChoice in RPSOptions
  
  print('The CPU chose ' + CPUMove)

  if userChoice == CPUMove:
      print('Tie')

  elif userChoice == 'rock' and CPUMove == 'paper' or userChoice == 'paper' and CPUMove == 'scissors' and userChoice == 'scissors' and CPUMove == 'rock':
      print('You lose')

  else:
      print('You win')

  return

def quadratic(a, b, c):
    """solve a quadratic

    :param a: the first coefficient 
    :param b: the second coefficient
    :param c: the third coefficient
    
    return
    ------
    float values of roots of quadratic
    
    raises
    ------
    if the 'a' value is 0 then it is not a quadratic
    """

    a = int(a)
    b = int(b)
    c = int(c)

    if a == 0:
        return 'Not a quadratic'

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return 'No real roots'

    if discriminant == 0:
        root = (-1 * b) / 2 * a
        return root

    root1 = (-1 * b + discriminant ** 0.5) / 2 * a
    root2 = (-1 * b - discriminant ** 0.5) / 2 * a
    roots = root1, root2

    return roots

def multiply(a, b):
    return a * b

def mathGame():
    """
    Simple muliplication Game
    
    User is asked to multiply number between 10 and 20
    They have a total of 3 lives which decrease to 0 if they type an incorrect answer
    User can get a scoreMultiplier if they keep up an answer streak
    scoreMultiplier is set back to 1 after any wrong answer
    Game ends once all lives finish and final score is displayed
    
    returns
    -------
    string of their score and whether their answer was correct or not
    """
    
  
    while True:

        score = 0
        scoreIncrement = 100
        scoreMultiplier = 1

        lives = 3
        while lives > 0:

            a = random.randint(10, 20)
            b = random.randint(10, 20)

            product = multiply(a, b)
            
            # print(str(product))
            
            print('You have ' + str(lives) + ' lives left.')
            print('Your current score: ' + str(score) + '.')

            userInput = input('What is the product of ' + str(a) + ' and ' + str(b) + '?')

            if userInput == str(product):
                score += scoreIncrement * scoreMultiplier
                scoreMultiplier += 0.5
                print('Correct!')

            else:
                print('WRONG')
                scoreMultiplier = 1
                lives -= 1

        print('Game Over! You ran out of lives! Your final score was ' + str(score))

        break

    return


def menu():
    print('0. Exit')
    print('1. RPS')
    print('2. Quadratic Solver')
    print('3. Mental Math Game')

    return


while True:
    menu()
    userInput = input('Please choose an option: ')

    if userInput == '1':
        while True:
            RPSGame()

            if input('Would you like to play again? ') != 'y':
                break

    if userInput == '2':
        while True:
            print('Quadratic Solver')
            a = input('Pass in an "a" value: ')
            b = input('Pass in a "b" value: ')
            c = input('Pass in a "c" value: ')
            roots = quadratic(a, b, c)
            print('The root(s) are/is ' + str(roots))

            if input('Would you like to try this option again? ') != 'y':
                break

    if userInput == '3':
        while True:
            mathGame()

            if input('Would you like to play again? ') != 'y':
                break

    if userInput == '0':
        break
