import random

name = input("What is your name?\n")
print(f"Welcome {name} to the Rock, Paper, Scissors game ✊📄✂️")

choice = input("Do you know the rules? (yes / no)\n").lower()

if choice == "yes":
    print("""
Sure 😊 Here are the rules of Rock Paper Scissors:

1- ✊ Rock beats ✂️ Scissors  
2- 📄 Paper covers ✊ Rock  
3- ✂️ Scissors cut 📄 Paper  

👉 If both choose the same, it's a draw 🤝
""")
else:
    print("No problem 😊 Let's play!")

options = ["rock", "paper", "scissors"]

player = input("Choose: rock ✊, paper 📄, scissors ✂️\n").lower()

if player not in options:
    print("❌ Error: invalid choice")
    exit()

computer = random.choice(options)

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art = {
    "rock": rock_art,
    "paper": paper_art,
    "scissors": scissors_art
}

print(f"\nYou chose: {player}")
print(art[player])

print(f"\nComputer chose: {computer}")
print(art[computer])

if player == computer:
    print("\n🤝 It's a draw!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("\n🏆 You win!")
else:
    print("\n😢 You lost!")

print(f"\nThank you {name} for playing 🙏🎮")