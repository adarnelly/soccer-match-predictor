#Andrew Darnell
#Compares 2 soccer teams and determines a predicted winner
#Sprint 2: added functions, loops, and if statements so an entire series between 2 teams can be predicted


def get_stat(prompt):
    #asks for a number and makes sure the number is not below zero
    number = int(input(prompt))
    while number < 0:
        print("That can't be negative, try again.")
        number = int(input(prompt))
    return number


def attack_rating(goals, sot):
    #Scoring is more important so it counts 3 times more than a regular shot
    return goals * 3 + sot


def defense_rating(goals_conceded, tackles):
    #goals against your team lose them points while tackles add to the defense rating
    return goals_conceded * -1.5 + tackles * 3


def chemistry_rating(passes, assists):
    #Players constantly pass the ball so the weight needs to be lower while assists prove good team chemistry.
    return passes * 0.2 + assists * 4


def team_rating(overall):
    #attempting to keep the scores around 100%
    return (overall / 500) * 99


def rating_word(rating):
    #turns the rating number into a word
    if rating >= 90:
        return "World Class"
    elif rating >= 60:
        return "Strong"
    elif rating >= 30:
        return "Average"
    else:
        return "Struggling"


def win_percent(overall1, overall2):
    #calculates team 1 win percent
    #if both teams are at 0 or less then the match is even
    if overall1 <= 0 and overall2 <= 0:
        return 50
    #a team can't be worse than 0 overall or the percents are over 100
    if overall1 < 0:
        overall1 = 0
    if overall2 < 0:
        overall2 = 0
    return overall1 / (overall1 + overall2) * 100


def print_report(name, sot, passes, overall, win_pct):
    #prints the extra stats for one team
    #shows last digit of shots on target
    shot_accuracy = sot % 10
    #squares the overall for a bonus
    dominance = overall ** 2
    #rating for every 100 passes completed
    pass_rating = passes // 100
    rating = team_rating(overall)
    print(name, "report", sep=" - ", end=":\n")
    print("  Win probability:", int(win_pct), "%")
    print("  Overall rating:", int(rating), "%", rating_word(rating))
    print("  Shot accuracy digit:", shot_accuracy, "| Dominance:", int(dominance), "| Pass rating:", pass_rating)


def play_match(match_number, team1_name, team2_name):
    #plays one match and returns 1,2, or 0 to determine which team wins or if they draw
    print("=" * 75)
    print("Match", match_number, sep=" #")
    team1_goals = get_stat("Enter " + team1_name + "'s goals scored: ")
    team1_sot = get_stat("Enter " + team1_name + "'s shots on target: ")
    team1_goals_conceded = get_stat("Enter " + team1_name + "'s goals conceded: ")
    team1_tackles = get_stat("Enter " + team1_name + "'s player tackles: ")
    team1_passes = get_stat("Enter " + team1_name + "'s team passes: ")
    team1_assists = get_stat("Enter " + team1_name + "'s goal assists: ")
    team2_goals = get_stat("Enter " + team2_name + "'s goals scored: ")
    team2_sot = get_stat("Enter " + team2_name + "'s shots on target: ")
    team2_goals_conceded = get_stat("Enter " + team2_name + "'s goals conceded: ")
    team2_tackles = get_stat("Enter " + team2_name + "'s player tackles: ")
    team2_passes = get_stat("Enter " + team2_name + "'s team passes: ")
    team2_assists = get_stat("Enter " + team2_name + "'s goal assists: ")
    #adds the three ratings together for one overall score
    team1_overall = attack_rating(team1_goals, team1_sot) + defense_rating(team1_goals_conceded, team1_tackles) + chemistry_rating(team1_passes, team1_assists)
    team2_overall = attack_rating(team2_goals, team2_sot) + defense_rating(team2_goals_conceded, team2_tackles) + chemistry_rating(team2_passes, team2_assists)
    team1_win_pct = win_percent(team1_overall, team2_overall)
    #team 2 gets whatever percent team 1 did not get
    team2_win_pct = 100 - team1_win_pct
    #divider to add space
    divider = "-" * 75
    print(divider)
    print(team1_name, "vs", team2_name, sep=" | ")
    print_report(team1_name, team1_sot, team1_passes, team1_overall, team1_win_pct)
    print_report(team2_name, team2_sot, team2_passes, team2_overall, team2_win_pct)
    if team1_win_pct == team2_win_pct:
        print("Prediction: it's a DRAW!")
        return 0
    elif team1_win_pct > team2_win_pct:
        print("Prediction:", team1_name, "wins!")
        return 1
    else:
        print("Prediction:", team2_name, "wins!")
        return 2


def play_series(matches, team1_name, team2_name):
    #plays every match in the series and tracks wins
    team1_wins = 0
    team2_wins = 0
    draws = 0
    #goes through each match, starting at 1 instead of 0
    for match_number in range(1, matches + 1):
        result = play_match(match_number, team1_name, team2_name)
        #gives a win to whoever wins the match
        if result == 1:
            team1_wins += 1
        elif result == 2:
            team2_wins += 1
        else:
            draws += 1
    print("=" * 75)
    print("SERIES RESULTS")
    print(team1_name, "wins:", team1_wins, "|", team2_name, "wins:", team2_wins, "| Draws:", draws)
    #only picks a series winner if they are not tied
    if team1_wins != team2_wins:
        if team1_wins > team2_wins:
            #one star for every match won
            print(team1_name + " takes the series! " + "*" * team1_wins)
        else:
            print(team2_name + " takes the series! " + "*" * team2_wins)
    else:
        print("The series is tied!")


def main():
    print("Welcome to the Soccer Match Predictor!")
    print("Determine the winner of any soccer match, or a whole series!")
    answer = "yes"
    #the loop ends when something other than yes is typed
    while answer == "yes":
        team1_name = input("Enter Team 1's name: ")
        team2_name = input("Enter Team 2's name: ")
        matches = get_stat("How many matches are in the series? ")
        #0 matches is not possible and more than 7 is too many so it gets set to 3 instead
        if matches == 0 or matches > 7:
            print("Series set to 3 matches instead.")
            matches = 3
        play_series(matches, team1_name, team2_name)
        answer = input("Run another series? (yes/no): ")
        if not answer == "yes":
            print("Thanks for using the Soccer Match Predictor!")


main()
