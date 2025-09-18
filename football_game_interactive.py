# 🏈 Interactive Python Football Drive
# Save this file as football_game_interactive.py and run:  python3 football_game_interactive.py

import random
import time

def say(msg):
    print(msg)
    time.sleep(0.6)  # small pause so it feels like a game

def yards_gain_for(play_type):
    """Return a yards gain/loss based on play type."""
    if play_type == "run":
        # Runs are steady: small gains, sometimes stuffed
        return random.randint(-2, 10)
    elif play_type == "pass":
        # Passes are boom-or-bust: big gains or nothing
        # 1 in 3 chance it's incomplete (0 yards)
        if random.random() < 0.33:
            return 0
        return random.randint(-10, 30)
    else:
        return 0

def choose_play():
    """Ask the user which play they want to run."""
    while True:
        play = input("Choose your play (run or pass): ").strip().lower()
        if play in ["run", "pass"]:
            return play
        print("Invalid choice. Please type 'run' or 'pass'.")

def touchdown_play(player):
    say(f"{player} runs it in for a TOUCHDOWN! 🥳")

def drive(player_name):
    say("Game Start! Kickoff! The ball is on the 50 yard line.")
    yards_to_goal = 50        # Need 50 yards for a TD
    yards_to_first = 10       # Need 10 yards for a 1st down
    down = 1                  # 1st, 2nd, 3rd, 4th down

    while down <= 4:
        say(f"\nDown: {down}   |  Yards to First: {yards_to_first}   |  Yards to Goal: {yards_to_goal}")
        play = choose_play()
        say(f"Coach calls a {play.upper()} play...")

        gain = yards_gain_for(play)

        # Announce special cases
        if play == "pass" and gain == 0:
            say("Pass is INCOMPLETE. No gain.")
        else:
            if gain > 0:
                say(f"It gains {gain} yards!")
            elif gain < 0:
                say(f"Uh oh, we lost {-gain} yards.")
            else:
                say("No gain on the play.")

        yards_to_goal = max(0, yards_to_goal - gain)  # can't go below 0
        yards_to_first = max(0, yards_to_first - gain)

        # Check for TOUCHDOWN
        if yards_to_goal == 0:
            touchdown_play(player_name)
            return True  # scored!

        # Check for FIRST DOWN
        if yards_to_first == 0:
            say("First down! We get a fresh set of 4 downs.")
            down = 1
            yards_to_first = 10
        else:
            down += 1

    # If we exit the loop, we used all 4 downs without a TD
    say("\nTurnover on downs. The drive is over.")
    return False

def extra_point():
    """Simple 95% chance to make the kick for the extra point."""
    say("The kicker lines up for the extra point...")
    made = random.random() < 0.95
    if made:
        say("The kick is GOOD! 🦵🎯")
        return 1
    else:
        say("Oh no, the kick is NO GOOD.")
        return 0

def main():
    say("Welcome to the Python Football Drive!")
    player_name = input("Enter your player's name: ").strip() or "Star Player"
    scored = drive(player_name)
    if scored:
        points = 6 + extra_point()
        say(f"\nFinal Score: Home {points} - Away 0")
    else:
        say("\nFinal Score: Home 0 - Away 0")
    say("\nThanks for playing! Run this again to try different choices.")

if __name__ == "__main__":
    main()