from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_update_score_win():
    # Win on 1st attempt: 100 - 10*(1+1) = 80
    score = update_score(0, "Win", 1)
    assert score == 80

def test_update_score_win_late():
    # Win on 5th attempt: 100 - 10*(5+1) = 40
    score = update_score(0, "Win", 5)
    assert score == 40

def test_update_score_win_min():
    # Win on 10th attempt: 100 - 10*11 = -10, but min 10
    score = update_score(0, "Win", 10)
    assert score == 10

def test_update_score_too_high():
    score = update_score(0, "Too High", 1)
    assert score == -5

def test_update_score_too_low():
    score = update_score(0, "Too Low", 1)
    assert score == -5
