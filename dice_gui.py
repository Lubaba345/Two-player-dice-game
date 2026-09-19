import tkinter as tk
import random

toto_points = 0
titi_points = 0
turn = "TOTO"

dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

def play_turn():
    play_button.config(state="disabled")
    roll_animation(10)

def roll_animation(count):
    global toto_points, titi_points, turn

    dice = random.randint(1, 6)

    if turn == "TOTO":
        toto_dice.config(text=dice_faces[dice])
    else:
        titi_dice.config(text=dice_faces[dice])

    if count > 0:
        root.after(100, roll_animation, count - 1)
    else:
        if turn == "TOTO":
            toto_points += dice
            toto_score.config(text=f"TOTO Total: {toto_points}")
            status.config(text=f"TOTO rolled {dice}")
            turn = "TITI"
        else:
            titi_points += dice
            titi_score.config(text=f"TITI Total: {titi_points}")
            status.config(text=f"TITI rolled {dice}")
            turn = "TOTO"

        if toto_points >= 50:
            status.config(text="TOTO wins!")
        elif titi_points >= 50:
            status.config(text="TITI wins!")
        else:
           play_button.config(state="normal")


def reset_game():
    global toto_points, titi_points, turn

    toto_points = 0
    titi_points = 0
    turn = "TOTO"

    toto_dice.config(text="⚀")
    titi_dice.config(text="⚀")
    toto_score.config(text="TOTO Total: 0")
    titi_score.config(text="TITI Total: 0")
    status.config(text="Click Play Turn to start")
    play_button.config(state="normal")

root = tk.Tk()
root.title("Two Player Dice Game")
root.geometry("450x380")

title = tk.Label(root, text="2-Player Dice Game", font=("Arial", 20, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=20)

toto_frame = tk.Frame(frame)
toto_frame.grid(row=0, column=0, padx=35)

titi_frame = tk.Frame(frame)
titi_frame.grid(row=0, column=1, padx=35)

tk.Label(toto_frame, text="TOTO", font=("Arial", 16, "bold")).pack()
toto_dice = tk.Label(toto_frame, text="⚀", font=("Arial", 70))
toto_dice.pack()
toto_score = tk.Label(toto_frame, text="TOTO Total: 0", font=("Arial", 12))
toto_score.pack()

tk.Label(titi_frame, text="TITI", font=("Arial", 16, "bold")).pack()
titi_dice = tk.Label(titi_frame, text="⚀", font=("Arial", 70))
titi_dice.pack()
titi_score = tk.Label(titi_frame, text="TITI Total: 0", font=("Arial", 12))
titi_score.pack()

status = tk.Label(root, text="Click Play Turn to start", font=("Arial", 13))
status.pack(pady=10)

play_button = tk.Button(root, text="Play Turn", command=play_turn, font=("Arial", 12))
play_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 12))
reset_button.pack(pady=5)

root.mainloop()