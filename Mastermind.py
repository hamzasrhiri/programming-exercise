import random

# function to generate random number
def random_num():
    num = []
    for i in range(4):
        number = random.randint(1, 6)
        num.append(number)
    return num

def mastermind():
    #rand_num = [1,1,3,3]  # hardcode for testing
    rand_num = random_num() 
    count = 0 # for attempts

    while count < 10:
        guess_input = input("Enter your guess (4 digits between 1 and 6): ")

        # convert input to string
        user_string = []
        for i in guess_input:
            user_string.append(int(i))

        # to track the answer
        right_position = 0
        wrong_position = 0

        rand_num_copy = list(rand_num)

        # check correct positions +
        for i in range(4):
            if user_string[i] == rand_num_copy[i]:
                right_position += 1
                rand_num_copy[i] = None # to prevent counting the same number twice

        # check for wrong positions -
        for i in range(4):
            if user_string[i] != rand_num_copy[i] and user_string[i] in rand_num_copy:
                wrong_position += 1
                # removing the element found to prevent double counting
                for j in range(4):
                    if rand_num_copy[j] == user_string[i]:
                        rand_num_copy[j] = None # to prevent counting the same number twice
                        break

        # reuslts
        result = ""
        for i in range(right_position):
            result += "+"
        for i in range(wrong_position):
            result += "-"
        print("Result:", result)
        
        # check if the guess is correct
        if right_position == 4:
            print("Congratulations! You guessed the number:", rand_num)
            break

        count += 1

    if count == 10:
        print("Sorry, you lost :( the correct number was:", rand_num)

mastermind()
