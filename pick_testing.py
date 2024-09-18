import pick

def test_check_guess_correct():
    assert pick.check_guess(5,5) == 0
    #test case for when guess == answer

def test_check_guess_above():
    assert pick.check_guess(7,5) == 2
    #test case for when guess > answer and returns difference

def test_check_guess_below():
    assert pick.check_guess(2,5) == 3
        #test case for when guess < answer and returns difference
    
#running test using pytest pick_testing.py