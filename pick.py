def check_guess(guess,answer):
    if guess == answer:
        return (0)
    elif guess > answer:
        return(guess - answer)
    elif answer > guess:
        return(answer - guess)

#def main():
 #   check_guess(4,5)
