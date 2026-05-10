import random

def get_choice():
    options = ["rock", "paper", "scissors"]
    player = input("Choose: rock ✊, paper 📄, scissors ✂️\n").lower()
    if player not in options:
        print("❌ Invalid choice, try again!")
        return None
    return player

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def play():
    score_player = 0
    score_computer = 0

    print("🎮 Welcome to Rock Paper Scissors PRO version!\n")

    while True:
        player = get_choice()
        if player is None:
            continue

        computer = random.choice(["rock", "paper", "scissors"])

        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")

        result = get_winner(player, computer)

        if result == "player":
            print("🏆 You win this round!")
            score_player += 1
        elif result == "computer":
            print("😢 Computer wins this round!")
            score_computer += 1
        else:
            print("🤝 It's a draw!")

        print(f"\n📊 Score -> You: {score_player} | Computer: {score_computer}")

        again = input("\nDo you want to play again? (yes/no)\n").lower()
        if again != "yes":
            break

    print("\n🎮 Thanks for playing!")
    print(f"Final Score -> You: {score_player} | Computer: {score_computer}")

play()