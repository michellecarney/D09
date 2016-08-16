import random

#We are going to count bulls and cows by comparing list indices
def number_str_to_list(n):
    list_n = [value for value in str(n)]
    return list_n

def user_guess(n):
    n_length = len(str(n))
    maxrounds = (2**n_length) + n_length
    print("Let's play the mimsmind1 game. You have {} guesses.".format(maxrounds))
    count = 0

    #Take user guesses and count
    user_n = input("Guess a {}-digit number: ".format(n_length))
    while count < maxrounds:
        try:
            user_n = int(user_n)
        except:
            user_n = input("Invalid input. Try again: ")
            continue
        count += 1
        if user_n == n:
            print("Congratulations. You guessed the correct number in {} times.".format(count))
            break

        #Max count reached, print number
        if count == maxrounds:
            print("Sorry you did not guess the number in {} tries. The correct number is {}.".format(maxrounds, n))
            break
       
        #Count bulls and cows, initialize var
        cow = 0
        bull = 0
       
        #Use fxn to compare elements in user's number to random n; compare as lists
        n_list = number_str_to_list(n)
        user_list = number_str_to_list(user_n)
        for index, value in enumerate(user_list):
            if value in n_list:
            # Bull: value is in the same location, remove from list for comparison
                if index == n_list.index(value):
                    bull += 1
                    user_list[index] = 'Done'
        for index, value in enumerate(user_list):
            # Cow: Checks if the value is in the list with remaining numbers.
            if value in n_list:
                cow += 1
        user_n = (input("{} bull(s), {} cow(s). Try again: ".format(bull, cow)))


def main():
    user_guess(random.randint(000, 1000))

if __name__ == '__main__':
    main()