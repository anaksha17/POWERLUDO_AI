import tkinter 
from tkinter import *
from tkinter import messagebox
import random
import time
from enum import Enum
import pygame
import copy
COLORS = {
    "board_bg": "#1E824C",
    "red_player": "#E74C3C",
    "blue_player": "#3498DB",
    "green_player": "#2ECC71",
    "yellow_player": "#F1C40F",
    "text": "#2C3E50",
    "highlight": "#ECF0F1"
}

class PlayerType(Enum):
    HUMAN = "Human"
    AI = "AI"

PLAYER_TYPES = {
    "RED": PlayerType.HUMAN,
    "BLUE": PlayerType.AI,
    "GREEN": PlayerType.HUMAN,
    "YELLOW": PlayerType.HUMAN
}

AI_DEPTH = 2
AI_THINKING_TIME = 0.5
AI_ROLL_DELAY = 1.0
AI_MOVE_DELAY = 1.0
AI_TURN_DELAY = 0.5
ANIMATION_SPEED = 0.05
TOKEN_RADIUS = 15

root = Tk()
root.resizable(width=False, height=False)
root.geometry('1000x750')
root.configure(background=COLORS["board_bg"])
root.title("Ludo Game")

pygame.mixer.init()

# Image paths (update as needed)
logo = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\whitebox.gif")
logo2 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\red side.gif")
logo3 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\red.gif")
logo4 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\blue side.gif")
logo5 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\green side.gif")
logo6 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\yellow side.gif")
logo7 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\center.gif")
logoxx = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\test.gif")
logog = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\greenbox.gif")
logogs = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\greenstop.gif")
logoy = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\yellowbox.gif")
logoys = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\yellowstop.gif")
logob = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\bluebox.png")
logobs = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\bluestop.gif")
logor = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\redbox.gif")
logors = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\redstop.gif")
logoh = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\head.gif")
logot = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\tail.gif")
logoh1 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\head1.gif")
logot1 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\tail1.gif")
logoh2 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\head2.gif")
logot2 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\tail2.gif")
logoh3 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\head3.gif")
logot3 = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\tail3.gif")
logoab = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\blue.gif")
logoay = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\yellow.gif")
logoag = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\green.gif")

Label(image=logo2, width=298, height=298).place(x=-1, y=-1)
Label(image=logo4, width=300, height=300).place(x=-2, y=448)
Label(image=logo5, width=296, height=296).place(x=450, y=0)
Label(image=logo6, width=294, height=294).place(x=450, y=450)
Label(image=logo7, width=150, height=150).place(x=298, y=298)
# After existing PhotoImage declarations
power_tile_img = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\rating.gif")
dice_img = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\dice.gif")
skull_img = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\skull.gif")
shield_img = PhotoImage(file=r"C:\Users\anaks\OneDrive\Documents\Semester 6\AI Tth-Lab\Ludo-Python-game-\shield.gif")


c = 0
lx = 0
bb = 0
nc = 0
rollc = 0
rolls = []
dice = 0
cx = 0
cy = 0
RED = True
BLUE = False
GREEN = False
YELLOW = False
TURN = True
REDKILL = False
BLUEKILL = False
GREENKILL = False
YELLOWKILL = False
dice_labels = []
ai_timer = None
puzzle_active = False
first_kill_tracker = {"RED": False, "BLUE": False, "GREEN": False, "YELLOW": False}
animation_in_progress = False
# Power tile positions (arbitrary, spaced out on the board)
POWER_TILE_POSITIONS = [5, 18, 31, 44]
# Dictionary to store power assignments for each tile
POWER_TILE_ASSIGNMENTS = {}
# Dictionary to track powers held by each player
SKIPPED_PLAYER = None  # Tracks the player whose turn is skipped
PLAYER_POWERS = {
    "RED": [],
    "BLUE": [],
    "GREEN": [],
    "YELLOW": []
}
# Track which powers have been used to enforce single-use
POWER_USED = {
    "RED": set(),
    "BLUE": set(),
    "GREEN": set(),
    "YELLOW": set()
}
box = None
redbox = None
bluebox = None
greenbox = None
yellowbox = None
redhome = None
bluehome = None
yellowhome = None
greenhome = None
red = None
blue = None
yellow = None
green = None
def player_path_to_global(player_color, player_pos):
    start_positions = {"RED": 14, "BLUE": 1, "YELLOW": 40, "GREEN": 27}
    start_pos = start_positions[player_color]
    return (start_pos + player_pos) % 52
from enum import Enum

class PowerType(Enum):
    SKIP_TURN = "Skip Turn"
    INSTANT_CAPTURE = "Instant Capture"
    IMMUNITY = "Immunity"
# Dictionary to map PowerType to images
power_images = {
    PowerType.SKIP_TURN: dice_img,  # Reuse dice_img or replace with skip_turn_img
    PowerType.INSTANT_CAPTURE: skull_img,
    PowerType.IMMUNITY: shield_img
}
def initialize_power_tiles():
    global POWER_TILE_ASSIGNMENTS
    POWER_TILE_ASSIGNMENTS = {}
    available_powers = [PowerType.SKIP_TURN, PowerType.INSTANT_CAPTURE, PowerType.IMMUNITY]
    random.shuffle(available_powers)
    for i, pos in enumerate(POWER_TILE_POSITIONS):
        POWER_TILE_ASSIGNMENTS[pos] = available_powers[i % len(available_powers)]
    print(f"Power Tiles Assigned: {POWER_TILE_ASSIGNMENTS}")

 
def assign_power_to_player(player_color, new_pos):
    """Assign a power to the player when landing on a power tile, only if no active powers exist."""
    global PLAYER_POWERS, TURN, nc, rolls, rollc, SKIPPED_PLAYER
    global_pos = player_path_to_global(player_color, new_pos)
    
    # Check if the player has any active (unused) powers
    active_powers = [p for p in PLAYER_POWERS[player_color] if p not in POWER_USED[player_color]]
    if active_powers:
        print(f"{player_color} cannot acquire new power: already has active powers {active_powers}")
        return
    
    # Assign power if landing on a power tile and the power is not already acquired
    if global_pos in POWER_TILE_ASSIGNMENTS and POWER_TILE_ASSIGNMENTS[global_pos] not in PLAYER_POWERS[player_color]:
        power = POWER_TILE_ASSIGNMENTS[global_pos]
        PLAYER_POWERS[player_color].append(power)
        messagebox.showinfo("Power Acquired", f"{player_color} gained {power.value} power!")
        update_power_indicators(player_color)
        
        # Handle SKIP_TURN power immediately
        if power == PowerType.SKIP_TURN:
            POWER_USED[player_color].add(PowerType.SKIP_TURN)
            PLAYER_POWERS[player_color].remove(power)
            turn_order = ["RED", "BLUE", "YELLOW", "GREEN"]
            current_idx = turn_order.index(player_color)
            next_idx = (current_idx + 1) % 4
            SKIPPED_PLAYER = turn_order[next_idx]
            messagebox.showinfo("Power Used", f"{player_color} used Skip Turn power! {SKIPPED_PLAYER}'s turn is skipped!")
            update_power_indicators(player_color)
            
            # Advance to the player after the skipped player
            nc = 0
            rolls = []
            rollc = 0
            TURN = True
            skip_idx = turn_order.index(SKIPPED_PLAYER)
            next_player_idx = (skip_idx + 1) % 4
            next_player = turn_order[next_player_idx]
            global RED, BLUE, YELLOW, GREEN
            RED = BLUE = YELLOW = GREEN = False
            if next_player == "RED":
                RED = True
            elif next_player == "BLUE":
                BLUE = True
            elif next_player == "YELLOW":
                YELLOW = True
            elif next_player == "GREEN":
                GREEN = True
            turn()
            if PLAYER_TYPES[next_player] == PlayerType.HUMAN:
                roll_button.config(state="normal")
            else:
                root.after(int(AI_TURN_DELAY * 1000), handle_ai_turn)
class AIPlayer:
    def __init__(self, color):
        self.color = color
        self.thinking = False

    def evaluate_position(self, pieces, home_positions, board_positions):
        score = 0
        PROGRESS_WEIGHT = 10
        SAFE_SPOT_BONUS = 50
        HOME_PENALTY = -100
        WIN_BONUS = 10000
        DOUBLE_BONUS = 30
        KILL_POTENTIAL = 75
        safe_spots = [1, 9, 14, 22, 27, 35, 40, 48]
        
        if self.check_win(pieces):
            return WIN_BONUS
            
        for piece in pieces:
            if piece.num == -1:
                score += HOME_PENALTY
            elif piece.num == 57:
                score += PROGRESS_WEIGHT * 57
            else:
                score += PROGRESS_WEIGHT * piece.num
                if piece.num in safe_spots:
                    score += SAFE_SPOT_BONUS
                if piece.double:
                    score += DOUBLE_BONUS
                if 50 <= piece.num < 57:
                    score += PROGRESS_WEIGHT * (piece.num - 49) * 2
                    
        for piece in pieces:
            if piece.num != -1 and piece.num != 57:
                current_pos = piece.num
                for dice in range(1, 7):
                    target_pos = (current_pos + dice) % len(board_positions)
                    if target_pos not in safe_spots and target_pos < len(board_positions):
                        score += KILL_POTENTIAL * 0.1
                        
        return score

    def get_best_move(self, pieces, home_positions, board_positions, dice_value):
        if dice_value is None or len(pieces) == 0:
            return None
            
        # Priority 1: Move a piece out of home with a 6
        if dice_value == 6:
            for i, piece in enumerate(pieces):
                if piece.num == -1:
                    return i
                    
        # Priority 2: Move to a power tile if not yet acquired
        for i, piece in enumerate(pieces):
            if piece.num != -1:
                new_pos = piece.num + dice_value
                if new_pos <= 57 and (new_pos < 50 or piece.kills > 0):
                    if (new_pos in POWER_TILE_ASSIGNMENTS and 
                        POWER_TILE_ASSIGNMENTS[new_pos] not in PLAYER_POWERS[self.color] and
                        POWER_TILE_ASSIGNMENTS[new_pos] not in POWER_USED[self.color]):
                        return i
                        
        # Priority 3: Move a piece to position 57 (home) if kills > 0
        for i, piece in enumerate(pieces):
            if piece.num != -1 and piece.num + dice_value == 57 and piece.kills > 0:
                return i
                
        # Priority 4: Move a piece to a safe spot
        safe_spots = [1, 9, 14, 22, 27, 35, 40, 48]
        for i, piece in enumerate(pieces):
            if piece.num != -1:
                new_pos = piece.num + dice_value
                if new_pos <= 57 and (new_pos < 50 or piece.kills > 0):
                    if new_pos in safe_spots:
                        return i
                        
        # Priority 5: Move the piece furthest along the board, respecting kills
        best_piece_idx = None
        max_progress = -1
        for i, piece in enumerate(pieces):
            if piece.num != -1 and piece.num != 57:
                new_pos = piece.num + dice_value
                if new_pos <= 57 and (new_pos < 50 or piece.kills > 0):
                    if piece.num > max_progress:
                        max_progress = piece.num
                        best_piece_idx = i
                        
        if best_piece_idx is not None:
            return best_piece_idx
            
        # Priority 6: Any valid move
        for i, piece in enumerate(pieces):
            if piece.num != -1 and piece.num != 57:
                new_pos = piece.num + dice_value
                if new_pos <= 57 and (new_pos < 50 or piece.kills > 0):
                    return i
                    
        return None

    def check_win(self, pieces):
        for piece in pieces:
            if piece.num != 57:
                return False
        return True


blue_ai = AIPlayer("BLUE")

class Box:
    rap = None
    count_label = None
    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0):
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=logo3, width=20, height=20)
        self.count = 1
        self.count_label = None
        self.color = "RED"
        self.double = False
        self.kills = 0
    def swap(self, offset_x=0, offset_y=0):
        self.rap.place(x=self.x0 + 13 + offset_x, y=self.y0 + 14 + offset_y)
        self.rap.lift()  # Raise piece above board and power tiles
        if self.count_label:
            self.count_label.destroy()
            self.count_label = None
        if self.count > 1:
            label_color = COLORS["red_player"] if self.is_safe() else "white"
            self.count_label = Label(root, text=str(self.count), fg="black", bg=label_color,
                                    font=("Arial", 10, "bold"))
            self.count_label.place(x=self.x0 + 20 + offset_x, y=self.y0 + 20 + offset_y)
            self.count_label.lift()  # Raise count label
    def is_safe(self):
        safe_spots = [1, 9, 14, 22, 27, 35, 40, 48]
        return self.num in safe_spots

class BBox:
    rap = None
    count_label = None
    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0):
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=logoab, width=20, height=20)
        self.count = 1
        self.count_label = None
        self.color = "BLUE"
        self.double = False
        self.kills = 0
    def swap(self, offset_x=0, offset_y=0):
        self.rap.place(x=self.x0 + 13 + offset_x, y=self.y0 + 14 + offset_y)
        self.rap.lift()  # Raise piece above board and power tiles
        if self.count_label:
            self.count_label.destroy()
            self.count_label = None
        if self.count > 1:
            label_color = COLORS["blue_player"] if self.is_safe() else "white"
            self.count_label = Label(root, text=str(self.count), fg="black", bg=label_color,
                                    font=("Arial", 10, "bold"))
            self.count_label.place(x=self.x0 + 20 + offset_x, y=self.y0 + 20 + offset_y)
            self.count_label.lift()  # Raise count label
    def is_safe(self):
        safe_spots = [1, 9, 14, 22, 27, 35, 40, 48]
        return self.num in safe_spots

class GBox:
    rap = None
    count_label = None
    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0):
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=logoag, width=20, height=20)
        self.count = 1
        self.count_label = None
        self.color = "GREEN"
        self.double = False
        self.kills = 0
    def swap(self, offset_x=0, offset_y=0):
        self.rap.place(x=self.x0 + 13 + offset_x, y=self.y0 + 14 + offset_y)
        self.rap.lift()  # Raise piece above board and power tiles
        if self.count_label:
            self.count_label.destroy()
            self.count_label = None
        if self.count > 1:
            label_color = COLORS["green_player"] if self.is_safe() else "white"
            self.count_label = Label(root, text=str(self.count), fg="black", bg=label_color,
                                    font=("Arial", 10, "bold"))
            self.count_label.place(x=self.x0 + 20 + offset_x, y=self.y0 + 20 + offset_y)
            self.count_label.lift()  # Raise count label
            

    def is_safe(self):
        safe_spots = [1, 9, 14, 22, 27, 35, 40, 48]
        return self.num in safe_spots

class YBox:
    rap = None
    count_label = None
    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0):
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=logoay, width=20, height=20)
        self.count = 1
        self.count_label = None
        self.color = "YELLOW"
        self.double = False
        self.kills = 0
    def swap(self, offset_x=0, offset_y=0):
        self.rap.place(x=self.x0 + 13 + offset_x, y=self.y0 + 14 + offset_y)
        self.rap.lift()  # Raise piece above board and power tiles
        if self.count_label:
            self.count_label.destroy()
            self.count_label = None
        if self.count > 1:
            label_color = COLORS["yellow_player"] if self.is_safe() else "white"
            self.count_label = Label(root, text=str(self.count), fg="black", bg=label_color,
                                    font=("Arial", 10, "bold"))
            self.count_label.place(x=self.x0 + 20 + offset_x, y=self.y0 + 20 + offset_y)
            self.count_label.lift()  # Raise count label
    def is_safe(self):
        safe_spots = [1, 9, 14, 22, 27, 35, 40, 48]
        return self.num in safe_spots



def board():
    tkinter.messagebox.showinfo(title="Ludo Game", message="TO START GAME PRESS OKAY & TO EXIT PRESS CROSS UP IN THE WINDOW")
    v = 0
    z = 0
    while v != 300:
        z = 0
        while z != 150:
            Label(image=logo, width=46, height=46).place(x=(300 + z), y=(0 + v))
            z = z + 50
        v = v + 50
        
    z = 0
    v = 0
    while v != 300:
        z = 0
        while z != 150:
            Label(image=logo, width=46, height=46).place(x=(0 + v), y=(300 + z))
            z = z + 50
        v = v + 50
    v = 0
    z = 0
    while v != 300:
        z = 0
        while z != 150:
            Label(image=logo, width=46, height=46).place(x=(300 + z), y=(450 + v))
            z = z + 50
        v = v + 50
    z = 0
    v = 0
    while v != 300:
        z = 0
        while z != 150:
            Label(image=logo, width=46, height=46).place(x=(450 + v), y=(300 + z))
            z = z + 50
        v = v + 50
    v = 0
    while v != 250:
        Label(image=logog, width=46, height=46).place(x=(350), y=(50 + v))
        v = v + 50
    Label(image=logog, width=46, height=46).place(x=(300), y=(100))
    Label(image=logogs, width=46, height=46).place(x=(400), y=(50))
    v = 0
    while v != 250:
        Label(image=logoy, width=46, height=46).place(x=(450 + v), y=(350))
        v = v + 50
    Label(image=logoy, width=46, height=46).place(x=(600), y=(300))
    Label(image=logoys, width=46, height=46).place(x=(650), y=(400))
    v = 0
    while v != 250:
        Label(image=logor, width=46, height=46).place(x=(50 + v), y=(350))
        v = v + 50
    Label(image=logor, width=46, height=46).place(x=(100), y=(400))
    Label(image=logors, width=46, height=46).place(x=(50), y=(300))
    v = 0
    while v != 250:
        Label(image=logob, width=46, height=46).place(x=(350), y=(450 + v))
        v = v + 50
    Label(image=logobs, width=46, height=46).place(x=(300), y=(650))
    Label(image=logob, width=46, height=46).place(x=(400), y=(600))
    Label(image=logoh, width=46, height=46).place(x=250, y=400)
    Label(image=logot, width=46, height=46).place(x=300, y=450)
    Label(image=logoh1, width=46, height=46).place(x=400, y=450)
    Label(image=logot1, width=46, height=46).place(x=450, y=400)
    Label(image=logoh2, width=46, height=46).place(x=450, y=300)
    Label(image=logot2, width=46, height=46).place(x=400, y=250)
    Label(image=logoh3, width=46, height=46).place(x=300, y=250)
    Label(image=logot3, width=46, height=46).place(x=250, y=300)
    # Add power tile images with error handling
    if box is None:
        print("Error: box is None in board()")
        return
    for pos in POWER_TILE_POSITIONS:
        if 0 <= pos < len(box) and box[pos] is not None:
            power_label = Label(root, image=power_tile_img, width=46, height=46, bg="yellow")
            print(f"Placing power tile at position {pos}: x={box[pos].x}, y={box[pos].y}")
            Label(image=power_tile_img, width=46, height=46).place(x=box[pos].x, y=box[pos].y)
            power_label.lower()
        else:
            print(f"Warning: Invalid position {pos} or box[{pos}] is None")

def doublecheck(a):
    for piece in a:
        piece.double = False
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[i].num == a[j].num and 
                a[i].num != -1 and 
                a[i].x0 == a[j].x0 and 
                a[i].y0 == a[j].y0):
                a[i].double = True
                a[j].double = True

def doublecheck_all():
    global red, blue, green, yellow
    all_pieces = [(piece, idx, "RED") for idx, piece in enumerate(red) if piece.num != -1 and piece.num != 57] + \
                 [(piece, idx, "BLUE") for idx, piece in enumerate(blue) if piece.num != -1 and piece.num != 57] + \
                 [(piece, idx, "GREEN") for idx, piece in enumerate(green) if piece.num != -1 and piece.num != 57] + \
                 [(piece, idx, "YELLOW") for idx, piece in enumerate(yellow) if piece.num != -1 and piece.num != 57]
    
    for piece_list in [red, blue, green, yellow]:
        for piece in piece_list:
            piece.count = 0
            if piece.count_label:
                piece.count_label.destroy()
                piece.count_label = None
    
    pos_counts = {}
    for piece, idx, color in all_pieces:
        pos = (piece.x0, piece.y0, piece.num, color)
        if pos not in pos_counts:
            pos_counts[pos] = []
        pos_counts[pos].append((piece, idx, color))
    
    for pos, tokens in pos_counts.items():
        if len(tokens) >= 1:
            color = tokens[0][2]
            count = sum(1 for t in tokens if t[2] == color)
            for piece, _, _ in tokens:
                piece.count = count
            if piece.is_safe():
                arrange_safe_point_tokens(tokens)
            else:
                for piece, _, _ in tokens:
                    piece.swap()

def arrange_safe_point_tokens(tokens):
    offsets = [(0, 0), (15, 0), (0, 15), (15, 15)]
    color_groups = {"RED": [], "BLUE": [], "GREEN": [], "YELLOW": []}
    for piece, idx, color in tokens:
        color_groups[color].append((piece, idx))
    
    offset_index = 0
    for color in color_groups:
        if color_groups[color]:
            if offset_index < len(offsets):
                offset_x, offset_y = offsets[offset_index]
                for piece, _ in color_groups[color]:
                    piece.swap(offset_x, offset_y)
                offset_index += 1
            else:
                for piece, _ in color_groups[color]:
                    piece.swap()

def animate_move(piece, end_x, end_y, steps=20):
    """Animate a piece moving to a new position, ensuring state sync."""
    global animation_in_progress
    if animation_in_progress:
        root.after(100, lambda: animate_move(piece, end_x, end_y, steps))
        return
    animation_in_progress = True
    start_x = piece.x0
    start_y = piece.y0
    dx = (end_x - start_x) / steps
    dy = (end_y - start_y) / steps
    def move_step(i):
        global animation_in_progress
        if i < steps:
            x_pos = start_x + dx * i
            y_pos = start_y + dy * i
            piece.rap.place(x=x_pos + 13, y=y_pos + 14)
            if piece.count_label:
                piece.count_label.place(x=x_pos + 20, y=y_pos + 20)
            root.after(15, lambda: move_step(i + 1))
        else:
            piece.x0 = end_x
            piece.y0 = end_y
            piece.x = end_x + 25
            piece.y = end_y + 25
            piece.swap()
            doublecheck_all()
            animation_in_progress = False
            print(f"Animation complete for {piece.color} piece: x0={piece.x0}, y0={piece.y0}, num={piece.num}")
    move_step(0)

def is_valid_move(piece, dice_value, board_positions):
    if piece.num == -1:
        return dice_value == 6
    elif piece.num == 57:
        return False
    else:
        new_pos = piece.num + dice_value
        return new_pos <= 57 and (new_pos < 50 or piece.kills > 0)

def highlight_dice(move_index):
    global dice_labels
    for lbl in dice_labels:
        lbl.destroy()
    dice_labels = []
    if rolls:
        for i, roll in enumerate(rolls):
            lbl = Label(dice_frame, text=str(roll), width=2, height=1, 
                        bg="white", fg="black", font=("Arial", 16))
            lbl.place(x=10 + i*40, y=10)
            dice_labels.append(lbl)
    if dice_labels and move_index < len(dice_labels):
        for i, lbl in enumerate(dice_labels):
            lbl.config(bg="white" if i != move_index else "yellow")

def clear():
    global nc, rolls, TURN, dice_history_labels, dice_labels
    nc = 0
    del rolls[:]
    TURN = True
    for lbl in dice_labels:
        lbl.destroy()
    dice_labels = []
    if not hasattr(clear, 'dice_history_labels'):
        clear.dice_history_labels = []
    for label in clear.dice_history_labels:
        label.destroy()
    clear.dice_history_labels = []
    turn()

def cancel_ai_timer():
    global ai_timer
    if ai_timer is not None:
        root.after_cancel(ai_timer)
        ai_timer = None

 

dashboard = Frame(root, bg="#34495E", width=250, height=700)
dashboard.place(x=750, y=0)
puzzle_result_label = Label(dashboard, text="", fg="white", bg="#34495E", font=("Arial", 12))
puzzle_result_label.place(x=10, y=600)

def clear_puzzle_result():
    puzzle_result_label.config(text="")

def is_last_token(pieces, piece_idx):
    """Check if the piece is the last token (3 others are at position 57)."""
    home_count = sum(1 for p in pieces if p.num == 57)
    return home_count == 3 and pieces[piece_idx].num != 57

def kill(a, pos, b, c, d, bh, ch, dh, pieces, move_idx):
    global REDKILL, BLUEKILL, GREENKILL, YELLOWKILL, puzzle_active
    safe_spots = [
        (box[1].x, box[1].y),
        (box[9].x, box[9].y),
        (box[14].x, box[14].y),
        (box[22].x, box[22].y),
        (box[27].x, box[27].y),
        (box[35].x, box[35].y),
        (box[40].x, box[40].y),
        (box[48].x, box[48].y)
    ]
    if pos < len(a):
        current_pos = (a[pos].x, a[pos].y)
        if current_pos not in safe_spots:
            kill_occurred = False
            immune_token_present = False
            # Check if any opponent token on this tile has immunity
            for opponent, _ in [(b, bh), (c, ch), (d, dh)]:
                for i in range(len(opponent)):
                    if (opponent[i].x0 == a[pos].x and 
                        opponent[i].y0 == a[pos].y and 
                        not opponent[i].double and
                        opponent[i].num != -1):
                        opponent_color = opponent[i].color
                        has_immunity = PowerType.IMMUNITY in PLAYER_POWERS[opponent_color] and not PowerType.IMMUNITY in POWER_USED[opponent_color]
                        if has_immunity:
                            immune_token_present = True
                            POWER_USED[opponent_color].add(PowerType.IMMUNITY)
                            messagebox.showinfo("Power Used", f"{opponent_color}'s token used Immunity power and was not captured!")
                            update_power_indicators(opponent_color)
                        else:
                            kill_occurred = True
                        # Continue checking all tokens to ensure all immune tokens are marked
            # If any token has immunity, skip all captures
            if immune_token_present:
                assign_power_to_player(pieces[move_idx].color, pos)
                doublecheck_all()
                return
            # Proceed with puzzle or INSTANT_CAPTURE if no immunity
            if kill_occurred:
                player_color = ""
                if a is redbox:
                    player_color = "RED"
                elif a is bluebox:
                    player_color = "BLUE"
                elif a is greenbox:
                    player_color = "GREEN"
                elif a is yellowbox:
                    player_color = "YELLOW"
                # Check for INSTANT_CAPTURE power for first kill
                has_instant_capture = PowerType.INSTANT_CAPTURE in PLAYER_POWERS[player_color] and not PowerType.INSTANT_CAPTURE in POWER_USED[player_color] and not first_kill_tracker[player_color]
                if has_instant_capture:
                    # Use INSTANT_CAPTURE to bypass puzzle for first kill
                    first_kill_tracker[player_color] = True
                    pieces[move_idx].kills += 1
                    POWER_USED[player_color].add(PowerType.INSTANT_CAPTURE)
                    messagebox.showinfo("Power Used", f"{player_color} used Instant Capture power!")
                    update_power_indicators(player_color)
                    # Perform the capture immediately
                    for opponent, home in [(b, bh), (c, ch), (d, dh)]:
                        for i in range(len(opponent)):
                            if (opponent[i].x0 == a[pos].x and 
                                opponent[i].y0 == a[pos].y and 
                                not opponent[i].double and
                                opponent[i].num != -1):
                                animate_move(opponent[i], home[i].x, home[i].y)
                                opponent[i].x0 = home[i].x
                                opponent[i].y0 = home[i].y
                                opponent[i].x = home[i].x + 25
                                opponent[i].y = home[i].y + 25
                                opponent[i].num = -1
                                opponent[i].swap()
                                break
                elif not first_kill_tracker[player_color]:
                    # Open puzzle for first kill if no INSTANT_CAPTURE
                    PuzzleWindow(player_color, pieces[move_idx], pos, a, [b, c, d], [bh, ch, dh], pieces, move_idx)
                    return
                else:
                    # Normal kill for subsequent kills
                    first_kill_tracker[player_color] = True
                    pieces[move_idx].kills += 1
                    # Perform captures for non-immune tokens
                    for opponent, home in [(b, bh), (c, ch), (d, dh)]:
                        for i in range(len(opponent)):
                            if (opponent[i].x0 == a[pos].x and 
                                opponent[i].y0 == a[pos].y and 
                                not opponent[i].double and
                                opponent[i].num != -1):
                                animate_move(opponent[i], home[i].x, home[i].y)
                                opponent[i].x0 = home[i].x
                                opponent[i].y0 = home[i].y
                                opponent[i].x = home[i].x + 25
                                opponent[i].y = home[i].y + 25
                                opponent[i].num = -1
                                opponent[i].swap()
                                break
        # Check if the piece is the last token reaching position 57
        if pos == 57 and is_last_token(pieces, move_idx) and not puzzle_active:
            player_color = pieces[move_idx].color
            PuzzleWindow(player_color, pieces[move_idx], pos, a, [b, c, d], [bh, ch, dh], pieces, move_idx, is_last_token_puzzle=True)
            return
        assign_power_to_player(pieces[move_idx].color, pos)
        doublecheck_all()

 




def next_turn():
    """Advance to the next player's turn, handling SKIP_TURN."""
    global RED, BLUE, GREEN, YELLOW, TURN, nc, rolls, rollc, SKIPPED_PLAYER
    current_color = ""
    if RED:
        current_color = "RED"
    elif BLUE:
        current_color = "BLUE"
    elif YELLOW:
        current_color = "YELLOW"
    elif GREEN:
        current_color = "GREEN"
    # Reset state for the current turn
    nc = 0
    rolls = []
    rollc = 0
    TURN = True
    # Check if the next player should be skipped
    turn_order = ["RED", "BLUE", "YELLOW", "GREEN"]
    current_idx = turn_order.index(current_color)
    next_idx = (current_idx + 1) % 4
    next_player = turn_order[next_idx]
    if SKIPPED_PLAYER == next_player:
        # Skip the next player and move to the one after
        skip_idx = next_idx
        next_idx = (skip_idx + 1) % 4
        next_player = turn_order[next_idx]
        SKIPPED_PLAYER = None  # Reset after skipping
    # Update turn flags
    RED = BLUE = YELLOW = GREEN = False
    if next_player == "RED":
        RED = True
    elif next_player == "BLUE":
        BLUE = True
    elif next_player == "YELLOW":
        YELLOW = True
    elif next_player == "GREEN":
        GREEN = True
    turn()
    # Enable/disable roll button based on player type
    if PLAYER_TYPES[next_player] == PlayerType.HUMAN:
        roll_button.config(state="normal")
    else:
        roll_button.config(state="disabled")
        root.after(int(AI_TURN_DELAY * 1000), handle_ai_turn)
import copy
import random
from tkinter import Toplevel, Label, Frame, Entry, Button, messagebox

import copy
import random
from tkinter import Toplevel, Label, Frame, Entry, Button, messagebox

import copy
import random
from tkinter import Toplevel, Label, Frame, Entry, Button, messagebox

class PuzzleWindow:
    def __init__(self, player_color, piece, new_pos, board, opponents, opponents_homes, pieces, move_idx, is_last_token_puzzle=False):
        global puzzle_active
        self.player_color = player_color
        self.piece = piece
        self.new_pos = new_pos
        self.board = board
        self.opponents = opponents
        self.opponents_homes = opponents_homes
        self.pieces = pieces
        self.move_idx = move_idx
        self.is_last_token_puzzle = is_last_token_puzzle
        self.original_state = copy.deepcopy({
            'piece': {
                'num': piece.num,
                'x0': piece.x0,
                'y0': piece.y0,
                'x': piece.x,
                'y': piece.y
            }
        })
        self.solved_puzzle = False
        self.puzzle_types = ["Sudoku", "WordUnscramble", "Boggle"]
        self.selected_puzzle = random.choice(self.puzzle_types)
        self.time_left = 60
        puzzle_active = True
        root.attributes('-disabled', True)
        roll_button.config(state="disabled")
        
        self.window = Toplevel(root)
        self.window.title("Puzzle Challenge")
        self.window.geometry("500x600")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_timeout)
        
        self.timer_label = Label(
            self.window,
            text=f"Time Left: {self.time_left}s",
            font=("Arial", 12)
        )
        self.timer_label.pack(pady=10)
        
        self.status_label = Label(
            self.window,
            text=f"Puzzle: {self.selected_puzzle}",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=5)
        
        self.puzzle_frame = Frame(self.window)
        self.puzzle_frame.pack(pady=10)
        
        self.setup_puzzle()
        self.start_timer()
        
        if PLAYER_TYPES[player_color] == PlayerType.AI:
            self.handle_ai_puzzle()

    def close_puzzle(self, success, ai_success=False):
        global puzzle_active, nc
        result_text = ""
        
        if PLAYER_TYPES[self.player_color] == PlayerType.AI:
            result_text = f"AI {self.player_color} {'Solved' if ai_success else 'Failed'} {self.selected_puzzle}!"
            success = ai_success
        else:
            result_text = f"{self.player_color} {'Solved' if success else 'Failed'} {self.selected_puzzle}!"
        
        if success:
            if not self.is_last_token_puzzle:
                first_kill_tracker[self.player_color] = True
                self.piece.kills += 1
                
                for opponent, home in zip(self.opponents, self.opponents_homes):
                    for i in range(len(opponent)):
                        if (opponent[i].x0 == self.board[self.new_pos].x and 
                            opponent[i].y0 == self.board[self.new_pos].y and 
                            not opponent[i].double and
                            opponent[i].num != -1):
                            animate_move(opponent[i], home[i].x, home[i].y)
                            opponent[i].x0 = home[i].x
                            opponent[i].y0 = home[i].y
                            opponent[i].x = home[i].x + 25
                            opponent[i].y = home[i].y + 25
                            opponent[i].num = -1
                            opponent[i].swap()
                            break
            
            animate_move(self.piece, self.board[self.new_pos].x, self.board[self.new_pos].y)
            self.piece.num = self.new_pos
            self.piece.x0 = self.board[self.new_pos].x
            self.piece.y0 = self.board[self.new_pos].y
            self.piece.x = self.board[self.new_pos].x + 25
            self.piece.y = self.board[self.new_pos].y + 25
            self.piece.swap()
            nc += 1
            
            if self.new_pos == 57:
                self.pieces.remove(self.piece)
        else:
            self.piece.num = self.original_state['piece']['num']
            self.piece.x0 = self.original_state['piece']['x0']
            self.piece.y0 = self.original_state['piece']['y0']
            self.piece.x = self.original_state['piece']['x']
            self.piece.y = self.original_state['piece']['y']
            self.piece.swap()
            nc += 1
        
        self.window.destroy()
        puzzle_active = False
        root.attributes('-disabled', False)
        roll_button.config(state="normal" if PLAYER_TYPES[self.player_color] == PlayerType.HUMAN else "disabled")
        puzzle_result_label.config(text=result_text)
        root.after(2000, clear_puzzle_result)
        doublecheck(self.pieces)
        doublecheck_all()
        
        if nc >= len(rolls) or (rolls and rolls[-1] != 6) or rollc >= 2:
            next_turn()
        else:
            if PLAYER_TYPES[self.player_color] == PlayerType.AI:
                root.after(int(AI_MOVE_DELAY * 1000), lambda: handle_ai_move(self.player_color))
            else:
                handle_ai_turn()

    def setup_puzzle(self):
        clear_puzzle_result()
        for widget in self.puzzle_frame.winfo_children():
            widget.destroy()
        
        if self.selected_puzzle == "Sudoku":
            self.setup_sudoku()
        elif self.selected_puzzle == "WordUnscramble":
            self.setup_word_unscramble()
        elif self.selected_puzzle == "Boggle":
            self.setup_boggle()

    def setup_sudoku(self):
        Label(
            self.puzzle_frame,
            text="Sudoku (6x6): Fill the grid with numbers 1-6",
            font=("Arial", 12)
        ).pack()
        
        self.sudoku_grid, self.solution = self.generate_sudoku()
        self.entries = [[None for _ in range(6)] for _ in range(6)]
        
        for i in range(6):
            row = Frame(self.puzzle_frame)
            row.pack()
            for j in range(6):
                if self.sudoku_grid[i][j] != 0:
                    Label(
                        row,
                        text=str(self.sudoku_grid[i][j]),
                        width=4,
                        font=("Arial", 12)
                    ).pack(side=LEFT, padx=5)
                else:
                    entry = Entry(
                        row,
                        width=4,
                        font=("Arial", 12)
                    )
                    entry.pack(side=LEFT, padx=5)
                    self.entries[i][j] = entry
        
        Button(
            self.puzzle_frame,
            text="Submit",
            command=self.check_sudoku
        ).pack(pady=10)

    def generate_sudoku(self):
        grid = [[0 for _ in range(6)] for _ in range(6)]
        solution = [[0 for _ in range(6)] for _ in range(6)]
        
        def is_valid(num, row, col, grid):
            for x in range(6):
                if grid[row][x] == num or grid[x][col] == num:
                    return False
            box_row, box_col = 3 * (row // 3), 2 * (col // 2)
            for i in range(3):
                for j in range(2):
                    if grid[box_row + i][box_col + j] == num:
                        return False
            return True
        
        def solve(grid, row=0, col=0):
            if row == 6:
                return True
            if col == 6:
                return solve(grid, row + 1, 0)
            if grid[row][col] != 0:
                return solve(grid, row, col + 1)
            nums = list(range(1, 7))
            random.shuffle(nums)
            for num in nums:
                if is_valid(num, row, col, grid):
                    grid[row][col] = num
                    if solve(grid, row, col + 1):
                        return True
                    grid[row][col] = 0
            return False
        
        solve(grid)
        for i in range(6):
            for j in range(6):
                solution[i][j] = grid[i][j]
        
        empty_cells = random.randint(14, 16)
        cells = [(i, j) for i in range(6) for j in range(6)]
        random.shuffle(cells)
        for i, j in cells[:empty_cells]:
            grid[i][j] = 0
        
        return grid, solution

    def check_sudoku(self):
        grid = [[0 for _ in range(6)] for _ in range(6)]
        valid = True
        
        for i in range(6):
            for j in range(6):
                if self.entries[i][j] is None:
                    grid[i][j] = self.sudoku_grid[i][j]
                else:
                    try:
                        val = self.entries[i][j].get().strip()
                        if not val:
                            valid = False
                            break
                        val = int(val)
                        if val < 1 or val > 6:
                            valid = False
                            break
                        grid[i][j] = val
                    except ValueError:
                        valid = False
                        break
            if not valid:
                break
        
        if valid:
            for i in range(6):
                row = set(grid[i])
                col = set(grid[x][i] for x in range(6))
                if len(row) != sum(1 for x in grid[i] if x != 0) or len(col) != sum(1 for x in range(6) if grid[x][i] != 0):
                    valid = False
                    break
            
            for box_row in range(0, 6, 3):
                for box_col in range(0, 6, 2):
                    box = set()
                    for i in range(3):
                        for j in range(2):
                            if grid[box_row + i][box_col + j] != 0:
                                box.add(grid[box_row + i][box_col + j])
                    if len(box) != sum(1 for i in range(3) for j in range(2) if grid[box_row + i][box_col + j] != 0):
                        valid = False
                        break
        
        if valid and all(grid[i][j] == self.solution[i][j] for i in range(6) for j in range(6)):
            self.solved_puzzle = True
            self.close_puzzle(True)
        else:
            messagebox.showerror("Error", "Invalid Sudoku solution! Use numbers 1-6 only.")

    def setup_word_unscramble(self):
        words = [
            "CAPTURE", "LUDOGAME", "ROLLDICE", "STRATEGY", "BOARDGAME", "MOVEMENT",
            "POWERUP", "TOKENS", "HOMEPATH", "VICTORY"
        ]
        self.target_word = random.choice(words)
        scrambled = list(self.target_word)
        random.shuffle(scrambled)
        scrambled_text = ''.join(scrambled)
        
        Label(
            self.puzzle_frame,
            text=f"Unscramble the word: {scrambled_text}",
            font=("Arial", 12)
        ).pack()
        
        Label(
            self.puzzle_frame,
            text=f"Hint: {len(self.target_word)} letters, related to Ludo or board games",
            font=("Arial", 10)
        ).pack()
        
        self.entry = Entry(self.puzzle_frame, font=("Arial", 12))
        self.entry.pack(pady=10)
        
        Button(
            self.puzzle_frame,
            text="Submit",
            command=self.check_word_unscramble
        ).pack()

    def check_word_unscramble(self):
        guess = self.entry.get().upper().strip()
        if len(guess) > 8:
            messagebox.showerror("Error", "Word too long! Maximum 8 letters.")
            return
        if guess == self.target_word:
            self.solved_puzzle = True
            self.close_puzzle(True)
        else:
            messagebox.showerror(
                "Error",
                f"Incorrect word! Hint: It's a {len(self.target_word)}-letter word related to Ludo."
            )

    def setup_boggle(self):
        Label(
            self.puzzle_frame,
            text="Boggle (5x5): Find a word (5-7 letters)",
            font=("Arial", 12)
        ).pack()
        
        self.boggle_board, self.valid_words = self.generate_boggle()
        
        for i in range(5):
            row = Frame(self.puzzle_frame)
            row.pack()
            for j in range(5):
                Label(
                    row,
                    text=self.boggle_board[i][j],
                    width=4,
                    font=("Arial", 12)
                ).pack(side=LEFT, padx=5)
        
        Label(
            self.puzzle_frame,
            text="Hint: Related to Ludo or board games",
            font=("Arial", 10)
        ).pack()
        
        self.entry = Entry(self.puzzle_frame, font=("Arial", 12))
        self.entry.pack(pady=10)
        
        Button(
            self.puzzle_frame,
            text="Submit",
            command=self.check_boggle
        ).pack()

    def generate_boggle(self):
        words = [
            "LUDOGAME", "ROLLDICE", "CAPTURED", "STRATEGY", "BOARDGAME",
            "MOVEMENT", "POWERUPS", "TOKENS", "HOMEPATH", "VICTORY"
        ]
        # Select a target word
        target_word = random.choice(words)
        
        # Define all possible directions for word placement
        directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
        
        # Filter directions based on word length to ensure the word fits in the 5x5 grid
        valid_directions = []
        for dr, dc in directions:
            steps = len(target_word) - 1
            max_row_steps = steps * abs(dr)
            max_col_steps = steps * abs(dc)
            max_start_row = 4 - max_row_steps
            max_start_col = 4 - max_col_steps
            if max_start_row >= 0 and max_start_col >= 0:
                valid_directions.append((dr, dc))
        
        # If no valid directions, try a shorter word
        if not valid_directions:
            target_word = random.choice([w for w in words if len(w) <= 5])  # Fallback to 5-letter words
            for dr, dc in directions:
                steps = len(target_word) - 1
                max_row_steps = steps * abs(dr)
                max_col_steps = steps * abs(dc)
                max_start_row = 4 - max_row_steps
                max_start_col = 4 - max_col_steps
                if max_start_row >= 0 and max_start_col >= 0:
                    valid_directions.append((dr, dc))
        
        # If still no valid directions, default to a simple word and direction
        if not valid_directions:
            target_word = "TOKENS"
            valid_directions = [(0, 1)]  # Default to right
        
        # Choose a random valid direction
        dir_choice = random.choice(valid_directions)
        
        # Recalculate max start positions for the chosen direction
        steps = len(target_word) - 1
        max_start_row = 4 - steps * abs(dir_choice[0])
        max_start_col = 4 - steps * abs(dir_choice[1])
        
        # Ensure non-negative values
        max_start_row = max(0, max_start_row)
        max_start_col = max(0, max_start_col)
        
        # Choose random start position
        start_row = random.randint(0, max_start_row)
        start_col = random.randint(0, max_start_col)
        
        # Initialize the board
        board = [['' for _ in range(5)] for _ in range(5)]
        
        # Place the target word on the board
        for i, char in enumerate(target_word):
            r = start_row + i * dir_choice[0]
            c = start_col + i * dir_choice[1]
            board[r][c] = char
        
        # Fill remaining cells with random letters
        letters = "BCDFGHJKLMNPQRSTVWXYZ" * 2 + "AEIOU" * 3
        for i in range(5):
            for j in range(5):
                if not board[i][j]:
                    board[i][j] = random.choice(letters)
        
        return board, words

    def check_boggle(self):
        guess = self.entry.get().upper().strip()
        if len(guess) > 7:
            messagebox.showerror("Error", "Word too long! Maximum 7 letters.")
            return
        if guess in self.valid_words and 5 <= len(guess) <= 7:
            self.solved_puzzle = True
            self.close_puzzle(True)
        else:
            messagebox.showerror(
                "Error",
                "Invalid word! Must be 5-7 letters, related to Ludo or board games."
            )

    def start_timer(self):
        if self.time_left > 0 and not self.solved_puzzle:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.window.after(1000, self.start_timer)
        elif self.time_left <= 0 and not self.solved_puzzle:
            self.on_timeout()

    def handle_ai_puzzle(self):
        self.status_label.config(
            text=f"AI ({self.player_color}) is solving {self.selected_puzzle}..."
        )
        thinking_time = random.randint(3000, 5000)
        success = random.random() < 0.75
        self.window.after(
            thinking_time,
            lambda: self.close_puzzle(success, ai_success=success)
        )

    def on_timeout(self):
        if not self.solved_puzzle:
            self.close_puzzle(False, ai_success=False)

def movecheck(r, rh, rb, la):
    global rolls, nc
    if len(rolls) >= 3 and rolls[-3:] == [6, 6, 6] and la == "BLUE":
        return False
    # Check for win condition
    win = True
    for j in range(len(r)):
        if r[j].num != 57:
            win = False
            break
    if win:
        L2 = Label(root, text=(la + " Wins"), fg='Black', background='green', font=("Arial", 24, "bold"))
        L2.place(x=770, y=500)
        return False
    if not rolls or nc >= len(rolls):
        return False
    current_roll = rolls[nc]
    # Check if a piece can move out of home
    for piece in r:
        if piece.num == -1 and current_roll == 6:
            return True
    # Check if a piece can move on the board
    for piece in r:
        if piece.num != -1 and piece.num != 57:
            new_pos = piece.num + current_roll
            if new_pos <= 57 and (new_pos < 50 or piece.kills > 0):
                return True
    return False

def turn():
    global RED, BLUE, GREEN, YELLOW
    turn_label = Label(dashboard, text="Current Turn:", fg="white", bg="#34495E", font=("Arial", 14, "bold"))
    turn_label.place(x=10, y=50)
    player_label = Label(dashboard, text="", fg="white", bg="#34495E", font=("Arial", 14))
    player_label.place(x=10, y=80)
    if RED:
        player_label.config(text="Red's Turn", fg=COLORS["red_player"])
    elif BLUE:
        player_label.config(text="Blue's Turn", fg=COLORS["blue_player"])
    elif YELLOW:
        player_label.config(text="Yellow's Turn", fg=COLORS["yellow_player"])
    elif GREEN:
        player_label.config(text="Green's Turn", fg=COLORS["green_player"])

def roll():
    global dice, rolls, rollc, TURN
    if TURN and not puzzle_active:
        rollc += 1
        dice = random.randint(1, 6)
        rolls.append(dice)
        highlight_dice(nc)
        if dice == 6 and rollc < 3:
            TURN = True
        else:
            TURN = False
        if len(rolls) >= 3 and rolls[-3:] == [6, 6, 6] and BLUE:
            print("Blue rolled three sixes, skipping turn")
            BLUE = False
            YELLOW = True
            clear()

def click(event):
    global cx, cy, c
    cx = event.x
    cy = event.y
    c += 1
    main()

def handle_ai_turn():
    global TURN, RED, BLUE, GREEN, YELLOW, ai_timer, rollc
    cancel_ai_timer()
    if not any([RED, BLUE, GREEN, YELLOW]):
        return
    current_color = ""
    if RED:
        current_color = "RED"
    elif BLUE:
        current_color = "BLUE"
    elif GREEN:
        current_color = "GREEN"
    elif YELLOW:
        current_color = "YELLOW"
    if PLAYER_TYPES[current_color] == PlayerType.HUMAN:
        return
    if TURN:
        roll()
        if rolls and rolls[-1] == 6 and rollc < 2:
            ai_timer = root.after(int(AI_ROLL_DELAY * 1000), handle_ai_turn)
        else:
            ai_timer = root.after(int(AI_ROLL_DELAY * 1000), 
                                  lambda: handle_ai_move(current_color))
    else:
        handle_ai_move(current_color)

def handle_ai_move(color):
    """Handle AI's move, ensuring position updates correctly."""
    global nc, rolls, ai_timer, RED, BLUE, GREEN, YELLOW, puzzle_active
    if not rolls or nc >= len(rolls):
        print(f"{color} has no rolls or nc={nc} >= len(rolls)={len(rolls)}, proceeding to next turn")
        next_turn()
        return
    pieces = None
    board = None
    home = None
    if color == "RED":
        pieces = red
        board = redbox
        home = redhome
    elif color == "BLUE":
        pieces = blue
        board = bluebox
        home = bluehome
    elif color == "GREEN":
        pieces = green
        board = greenbox
        home = greenhome
    elif color == "YELLOW":
        pieces = yellow
        board = yellowbox
        home = yellowhome
    if not pieces:
        print(f"No pieces found for {color}, proceeding to next turn")
        next_turn()
        return
    highlight_dice(nc)
    current_dice = rolls[nc]
    ai = blue_ai if color == "BLUE" else AIPlayer(color)
    move_idx = ai.get_best_move(pieces, home, board, current_dice)
    if move_idx is not None and move_idx < len(pieces):
        piece = pieces[move_idx]
        print(f"AI {color} chose piece {move_idx}: num={piece.num}, x0={piece.x0}, y0={piece.y0}")
        if piece.num == -1 and current_dice == 6:
            print(f"Moving {color} piece {move_idx} from home to board[0]: x={board[0].x}, y={board[0].y}")
            animate_move(piece, board[0].x, board[0].y)
            piece.x0 = board[0].x
            piece.y0 = board[0].y
            piece.x = board[0].x + 25
            piece.y = board[0].y + 25
            piece.num = 0
            piece.swap()
            nc += 1
            doublecheck_all()
            assign_power_to_player(color, 0)
            print(f"After move: num={piece.num}, x0={piece.x0}, y0={piece.y0}")
        elif piece.num != -1:
            new_pos = piece.num + current_dice
            if new_pos <= 57 and (new_pos < 50 or piece.kills > 0):
                print(f"Moving {color} piece {move_idx} to new_pos={new_pos}: x={board[new_pos].x}, y={board[new_pos].y}")
                kill(board, new_pos, *([red, yellow, green] if color == "BLUE" else 
                                      [blue, yellow, green] if color == "RED" else 
                                      [blue, red, green] if color == "YELLOW" else 
                                      [blue, yellow, red]), 
                     *(redhome, yellowhome, greenhome) if color == "BLUE" else 
                      (bluehome, yellowhome, greenhome) if color == "RED" else 
                      (bluehome, redhome, greenhome) if color == "YELLOW" else 
                      (bluehome, yellowhome, redhome), pieces, move_idx)
                if not puzzle_active:
                    animate_move(piece, board[new_pos].x, board[new_pos].y)
                    piece.x0 = board[new_pos].x
                    piece.y0 = board[new_pos].y
                    piece.x = board[new_pos].x + 25
                    piece.y = board[new_pos].y + 25
                    piece.num = new_pos
                    piece.swap()
                    nc += 1
                    print(f"After move: num={piece.num}, x0={piece.x0}, y0={piece.y0}")
                    if new_pos == 57:
                        pieces.remove(piece)
        doublecheck(pieces)
        doublecheck_all()
        if nc < len(rolls) and not puzzle_active:
            ai_timer = root.after(int(AI_MOVE_DELAY * 1000), 
                                  lambda: handle_ai_move(color))
        else:
            if rolls and rolls[-1] == 6 and rollc < 2 and not puzzle_active:
                ai_timer = root.after(int(AI_TURN_DELAY * 1000), handle_ai_turn)
            else:
                ai_timer = root.after(int(AI_TURN_DELAY * 1000), next_turn)
    else:
        print(f"No valid move for {color} with dice={current_dice}, nc={nc}")
        nc += 1
        if nc < len(rolls) and not puzzle_active:
            ai_timer = root.after(int(AI_MOVE_DELAY * 1000), 
                                  lambda: handle_ai_move(color))
        else:
            if rolls and rolls[-1] == 6 and rollc < 2 and not puzzle_active:
                ai_timer = root.after(int(AI_TURN_DELAY * 1000), handle_ai_turn)
            else:
                ai_timer = root.after(int(AI_TURN_DELAY * 1000), next_turn)


def show_instructions():
    instructions = (
        "Yo, welcome to *PowerLudo*! 🎲\n\n"
        "🔥 Quick Rundown:\n"
        "- 4 players (Red, Blue, Green, Yellow). Blue’s an AI, others are you (or friends)!\n"
        "- Goal: Get all 4 tokens from home to the center (pos 57).\n"
        "- Roll the dice, move tokens. Roll a 6? Extra roll, buddy (But 3 sixes = skip for Blue.)\n"
        "- Click tokens to move ‘em. Need a 6 to leave home.\n"
        "- Land on enemies to send ‘em home, but first kill needs a puzzle (Sudoku, Word Scramble, or Boggle). 60 secs to solve!\n"
        "- Power Tiles (5, 18, 31, 44): Grab cool powers!\n"
        "  - *Skip Turn*: Next player’s out for a round.\n"
        "  - *Instant Capture*: First kill, no puzzle.\n"
        "  - *Immunity*: Save your token from a beatdown.\n"
        "- Safe spots (1, 9, 14, 22, 27, 35, 40, 48) = no captures.\n"
        "- Last token to 57? Solve a puzzle to win!\n\n"
        "🏆 First to get all tokens home wins! Click OK to roll, or X to bail. Let’s vibe! 😎"
    )
    messagebox.showinfo("PowerLudo - Let’s Roll!", instructions) 
 
def main():
    global box, redbox, bluebox, greenbox, yellowbox, redhome, bluehome, yellowhome, greenhome
    global red, blue, yellow, green, RED, BLUE, GREEN, YELLOW, dice, nc, TURN, bb, c, cx, cy
    global puzzle_active, first_kill_tracker,SKIPPED_PLAYER
    if c == 0:
        show_instructions()
        puzzle_active = False
        first_kill_tracker = {"RED": False, "BLUE": False, "GREEN": False, "YELLOW": False}
        SKIPPED_PLAYER = None
        # Initialize power tiles
        initialize_power_tiles()
        
        box = [Box() for i in range(52)]
        redbox = [Box() for i in range(57)]
        bluebox = [BBox() for i in range(57)]
        greenbox = [GBox() for i in range(57)]
        yellowbox = [YBox() for i in range(57)]
        redhome = [Box() for i in range(4)]
        bluehome = [BBox() for i in range(4)]
        greenhome = [GBox() for i in range(4)]
        yellowhome = [YBox() for i in range(4)]
        red = [Box() for i in range(4)]
        blue = [BBox() for i in range(4)]
        green = [GBox() for i in range(4)]
        yellow = [YBox() for i in range(4)]
        for i in range(4):
            red[i].kills = 0
            blue[i].kills = 0
            green[i].kills = 0
            yellow[i].kills = 0
        for i in range(2):
            redhome[i].x = (100 + (100 * i))
            redhome[i].y = 100
            red[i].x0 = redhome[i].x
            red[i].y0 = redhome[i].y
            red[i].x = (red[i].x0) + 25
            red[i].y = (red[i].y0) + 25
            bluehome[i].x = (100 + (100 * i))
            bluehome[i].y = (550)
            blue[i].x0 = bluehome[i].x
            blue[i].y0 = bluehome[i].y
            blue[i].x = (blue[i].x0) + 25
            blue[i].y = (blue[i].y0) + 25
            yellowhome[i].x = (550 + (100 * i))
            yellowhome[i].y = (550)
            yellow[i].x0 = yellowhome[i].x
            yellow[i].y0 = yellowhome[i].y
            yellow[i].x = (yellow[i].x0) + 25
            yellow[i].y = (yellow[i].y0) + 25
            greenhome[i].x = (550 + (100 * i))
            greenhome[i].y = (100)
            green[i].x0 = greenhome[i].x
            green[i].y0 = greenhome[i].y
            green[i].x = (green[i].x0) + 25
            green[i].y = (green[i].y0) + 25
        for i in range(2, 4):
            redhome[i].x = (100 + (100 * (i - 2)))
            redhome[i].y = 200
            red[i].x0 = redhome[i].x
            red[i].y0 = redhome[i].y
            red[i].x = (red[i].x0) + 25
            red[i].y = (red[i].y0) + 25
            bluehome[i].x = (100 + (100 * (i - 2)))
            bluehome[i].y = (650)
            blue[i].x0 = bluehome[i].x
            blue[i].y0 = bluehome[i].y
            blue[i].x = (blue[i].x0) + 25
            blue[i].y = (blue[i].y0) + 25
            yellowhome[i].x = (550 + (100 * (i - 2)))
            yellowhome[i].y = (650)
            yellow[i].x0 = yellowhome[i].x
            yellow[i].y0 = yellowhome[i].y
            yellow[i].x = (yellow[i].x0) + 25
            yellow[i].y = (yellow[i].y0) + 25
            greenhome[i].x = (550 + (100 * (i - 2)))
            greenhome[i].y = 200
            green[i].x0 = greenhome[i].x
            green[i].y0 = greenhome[i].y
            green[i].x = (green[i].x0) + 25
            green[i].y = (green[i].y0) + 25
        for i in range(6):
            box[i].x = 300
            box[i].y = (700 - (50 * i))
        for i in range(6, 12):
            box[i].x = (250 - (50 * (i - 6)))
            box[i].y = (400)
        box[12].x = 0
        box[12].y = 350
        for i in range(13, 19):
            box[i].x = (0 + (50 * (i - 13)))
            box[i].y = (300)
        for i in range(19, 25):
            box[i].x = (300)
            box[i].y = (250 - (50 * (i - 19)))
        box[25].x = 350
        box[25].y = 0
        for i in range(26, 32):
            box[i].x = (400)
            box[i].y = (0 + (50 * (i - 26)))
        for i in range(32, 38):
            box[i].x = (450 + (50 * (i - 32)))
            box[i].y = (300)
        box[38].x = 700
        box[38].y = 350
        for i in range(39, 45):
            box[i].x = (700 - (50 * (i - 39)))
            box[i].y = (400)
        for i in range(45, 51):
            box[i].x = (400)
            box[i].y = (450 + (50 * (i - 45)))
        box[51].x = 350
        box[51].y = 700
        lx = 14
        for i in range(52):
            redbox[i].x = box[lx].x
            redbox[i].y = box[lx].y
            lx = lx + 1
            if lx > 51:
                lx = 0
        lx = 50
        for i in range(7):
            redbox[lx].x = (0 + (50 * i))
            redbox[lx].y = 350
            lx = lx + 1
        lx = 1
        for i in range(52):
            bluebox[i].x = box[lx].x
            bluebox[i].y = box[lx].y
            lx = lx + 1
            if lx > 51:
                lx = 0
        lx = 50
        for i in range(7):
            bluebox[lx].x = 350
            bluebox[lx].y = (700 - (50 * i))
            lx = lx + 1
        lx = 40
        for i in range(52):
            yellowbox[i].x = box[lx].x
            yellowbox[i].y = box[lx].y
            lx = lx + 1
            if lx > 51:
                lx = 0
        lx = 50
        for i in range(7):
            yellowbox[lx].x = (700 - (50 * i))
            yellowbox[lx].y = (350)
            lx = lx + 1
        lx = 27
        for i in range(52):
            greenbox[i].x = box[lx].x
            greenbox[i].y = box[lx].y
            lx = lx + 1
            if lx > 51:
                lx = 0
        lx = 50
        for i in range(7):
            greenbox[lx].x = 350
            greenbox[lx].y = (0 + (50 * i))
            lx = lx + 1
        for i in range(4):
            red[i].swap()
            blue[i].swap()
            green[i].swap()
            yellow[i].swap()
        board()   
    else:
        if c >= 1:
            if RED == True and TURN == False:
                print("Red's Turn")
                print("moves available: ", rolls)
                la = "RED"
                if not movecheck(red, redhome, redbox, la):
                    BLUE = True
                    RED = False
                    clear()
                if RED == True and PLAYER_TYPES["RED"] == PlayerType.HUMAN:
                    for i in range(len(red)):
                        if (abs(cx - (red[i].x0 + 25)) < 25 and 
                            abs(cy - (red[i].y0 + 25)) < 25) and (
                            red[i].x0 == redhome[i].x) and (red[i].y0 == redhome[i].y):
                            print("woila red home")
                            if nc < len(rolls) and rolls[nc] == 6:
                                animate_move(red[i], redbox[0].x, redbox[0].y)
                                red[i].x0 = redbox[0].x
                                red[i].y0 = redbox[0].y
                                red[i].x = redbox[0].x + 25
                                red[i].y = redbox[0].y + 25
                                red[i].num = 0
                                red[i].swap()
                                nc = nc + 1
                                doublecheck_all()
                                # Assign power if landing on a power tile
                                assign_power_to_player("RED", 0)
                                if nc > len(rolls) - 1:
                                    BLUE = True
                                    RED = False
                                    clear()
                                break
                        if (abs(cx - (red[i].x0 + 25)) < 25 and 
                            abs(cy - (red[i].y0 + 25)) < 25) and (
                            red[i].num != -1):
                            print(f"woila red board, piece {i}, num={red[i].num}, x0={red[i].x0}, y0={red[i].y0}")
                            bb = ((red[i].num) + rolls[nc]) if nc < len(rolls) else red[i].num
                            if bb > 57 or (bb >= 50 and red[i].kills == 0):
                                print(f"Invalid move: bb={bb}, kills={red[i].kills}")
                                break
                            kill(redbox, bb, blue, yellow, green, bluehome, yellowhome, greenhome, red, i)
                            if not puzzle_active:
                                animate_move(red[i], redbox[bb].x, redbox[bb].y)
                                red[i].x0 = redbox[bb].x
                                red[i].y0 = redbox[bb].y
                                red[i].x = redbox[bb].x + 25
                                red[i].y = redbox[bb].y + 25
                                red[i].num = bb
                                red[i].swap()
                                nc += 1
                                if bb == 57:
                                    red.remove(red[i])
                            doublecheck(red)
                            doublecheck_all()
                            if nc > len(rolls) - 1:
                                BLUE = True
                                RED = False
                                clear()
                            break
            if BLUE == True and TURN == False:
                print("Blue's Turn")
                print("moves available: ", rolls)
                la = "BLUE"
                if rolls == [6, 6, 6]:
                    print("Blue rolled three sixes, skipping turn")
                    BLUE = False
                    YELLOW = True
                    clear()
                elif not movecheck(blue, bluehome, bluebox, la):
                    print("No moves available")
                    BLUE = False
                    YELLOW = True
                    clear()
                else:
                    if PLAYER_TYPES["BLUE"] == PlayerType.AI and not puzzle_active:
                        dice_value = rolls[nc] if nc < len(rolls) else None
                        move_idx = blue_ai.get_best_move(blue, bluehome, bluebox, dice_value)
                        if move_idx is not None:
                            print(f"AI chose piece {move_idx}, current num={blue[move_idx].num}")
                            if blue[move_idx].num == -1 and dice_value == 6:
                                animate_move(blue[move_idx], bluebox[0].x, bluebox[0].y)
                                blue[move_idx].x0 = bluebox[0].x
                                blue[move_idx].y0 = bluebox[0].y
                                blue[move_idx].x = bluebox[0].x + 25
                                blue[move_idx].y = bluebox[0].y + 25
                                blue[move_idx].num = 0
                                blue[move_idx].swap()
                                nc += 1
                                doublecheck_all()
                                # Assign power if landing on a power tile
                                assign_power_to_player("BLUE", 0)
                            elif blue[move_idx].num != -1:
                                bb = blue[move_idx].num + dice_value
                                if bb <= 57 and (bb < 50 or blue[move_idx].kills > 0):
                                    kill(bluebox, bb, red, yellow, green, redhome, yellowhome, greenhome, blue, move_idx)
                                    if not puzzle_active:
                                        animate_move(blue[move_idx], bluebox[bb].x, bluebox[bb].y)
                                        blue[move_idx].x0 = bluebox[bb].x
                                        blue[move_idx].y0 = bluebox[bb].y
                                        blue[move_idx].x = bluebox[bb].x + 25
                                        blue[move_idx].y = bluebox[bb].y + 25
                                        blue[move_idx].num = bb
                                        blue[move_idx].swap()
                                        nc += 1
                                        if bb == 57:
                                            blue.remove(blue[move_idx])
                                    doublecheck(blue)
                                    doublecheck_all()
                            if nc >= len(rolls) or puzzle_active:
                                if rolls and rolls[-1] == 6 and rollc < 2 and not puzzle_active:
                                    handle_ai_turn()
                                else:
                                    BLUE = False
                                    YELLOW = True
                                    clear()
            if YELLOW == True and TURN == False:
                print("Yellow's Turn")
                print("moves available: ", rolls)
                la = "YELLOW"
                if not movecheck(yellow, yellowhome, yellowbox, la):
                    YELLOW = False
                    GREEN = True
                    clear()
                if YELLOW == True and PLAYER_TYPES["YELLOW"] == PlayerType.HUMAN:
                    for i in range(len(yellow)):
                        if (abs(cx - (yellow[i].x0 + 25)) < 25 and 
                            abs(cy - (yellow[i].y0 + 25)) < 25) and (
                            yellow[i].x0 == yellowhome[i].x) and (yellow[i].y0 == yellowhome[i].y):
                            print("woila yellow home")
                            if nc < len(rolls) and rolls[nc] == 6:
                                animate_move(yellow[i], yellowbox[0].x, yellowbox[0].y)
                                yellow[i].x0 = yellowbox[0].x
                                yellow[i].y0 = yellowbox[0].y
                                yellow[i].x = yellowbox[0].x + 25
                                yellow[i].y = yellowbox[0].y + 25
                                yellow[i].num = 0
                                yellow[i].swap()
                                nc += 1
                                doublecheck_all()
                                # Assign power if landing on a power tile
                                assign_power_to_player("YELLOW", 0)
                                if nc > len(rolls) - 1:
                                    YELLOW = False
                                    GREEN = True
                                    clear()
                                break
                        if (abs(cx - (yellow[i].x0 + 25)) < 25 and 
                            abs(cy - (yellow[i].y0 + 25)) < 25) and (
                            yellow[i].num != -1):
                            print(f"woila yellow board, piece {i}, num={yellow[i].num}, x0={yellow[i].x0}, y0={yellow[i].y0}")
                            bb = ((yellow[i].num) + rolls[nc]) if nc < len(rolls) else yellow[i].num
                            if bb > 57 or (bb >= 50 and yellow[i].kills == 0):
                                print(f"Invalid move: bb={bb}, kills={yellow[i].kills}")
                                break
                            kill(yellowbox, bb, red, blue, green, redhome, bluehome, greenhome, yellow, i)
                            if not puzzle_active:
                                animate_move(yellow[i], yellowbox[bb].x, yellowbox[bb].y)
                                yellow[i].x0 = yellowbox[bb].x
                                yellow[i].y0 = yellowbox[bb].y
                                yellow[i].x = yellowbox[bb].x + 25
                                yellow[i].y = yellowbox[bb].y + 25
                                yellow[i].num = bb
                                yellow[i].swap()
                                nc += 1
                                if bb == 57:
                                    yellow.remove(yellow[i])
                            doublecheck(yellow)
                            doublecheck_all()
                            if nc > len(rolls) - 1:
                                YELLOW = False
                                GREEN = True
                                clear()
                            break
            if GREEN == True and TURN == False:
                print("Green's Turn")
                print("moves available: ", rolls)
                la = "GREEN"
                if not movecheck(green, greenhome, greenbox, la):
                    print("NO MOVES SIR JEE")
                    GREEN = False
                    RED = True
                    clear()
                if GREEN == True and PLAYER_TYPES["GREEN"] == PlayerType.HUMAN:
                    for i in range(len(green)):
                        if (((cx > green[i].x0 + 13) and (cx < green[i].x + 13)) and (
                                (cy > green[i].y0 + 14) and (cy < green[i].y + 14))) and (
                                green[i].x0 == greenhome[i].x) and (green[i].y0 == greenhome[i].y):
                            print("woila green home")
                            if rolls[0 + nc] == 6:
                                animate_move(green[i], greenbox[0].x, greenbox[0].y)
                                green[i].x0 = greenbox[0].x
                                green[i].y0 = greenbox[0].y
                                green[i].x = greenbox[0].x + 25
                                green[i].y = greenbox[0].y + 25
                                green[i].num = 0
                                green[i].swap()
                                nc = nc + 1
                                doublecheck_all()
                                # Assign power if landing on a power tile
                                assign_power_to_player("GREEN", 0)
                                print("green x.y: ", green[i].x0, green[i].y0)
                                if nc > len(rolls) - 1:
                                    GREEN = False
                                    RED = True
                                    clear()
                                break
                            else:
                                print("Invalid move: Need a 6 to move from home")
                                break
                        if (((cx > green[i].x0 + 13) and (cx < green[i].x + 13)) and (
                                (cy > green[i].y0 + 14) and (cy < green[i].y + 14))) and (
                                green[i].num != -1):
                            print(f"woila green board, piece {i}, num={green[i].num}, x0={green[i].x0}, y0={green[i].y0}")
                            bb = ((green[i].num) + rolls[0 + nc])
                            if bb > 57:
                                print(f"Invalid move: bb={bb}")
                                break
                            kill(greenbox, bb, blue, yellow, red, bluehome, yellowhome, redhome, green, i)
                            if not puzzle_active:
                                animate_move(green[i], greenbox[bb].x, greenbox[bb].y)
                                green[i].x0 = greenbox[bb].x
                                green[i].y0 = greenbox[bb].y
                                green[i].x = greenbox[bb].x + 25
                                green[i].y = greenbox[bb].y + 25
                                green[i].num = bb
                                green[i].swap()
                                nc += 1
                                if bb == 57:
                                    green.remove(green[i])
                            doublecheck(green)
                            doublecheck_all()
                            if nc > len(rolls) - 1:
                                GREEN = False
                                RED = True
                                clear()
                            break
    handle_ai_turn()


def leftClick(event):
    global c, cx, cy, RED, YELLOW
    c = c + 1
    cx = root.winfo_pointerx() - root.winfo_rootx()
    cy = root.winfo_pointery() - root.winfo_rooty()
    print("Click at: ", cx, cy)
    main()

root.bind("<Button-1>", leftClick)


# Modified UI setup to remove extra_roll_button
power_labels = {}  # Store power image labels
player_frames = []
for i, color in enumerate(["RED", "BLUE", "GREEN", "YELLOW"]):
    player_frame = Frame(dashboard, bg="#2C3E50", width=230, height=100)
    player_frame.place(x=10, y=10 + i*110)
    player_frames.append(player_frame)
    Label(player_frame, text=f"{color}", fg=COLORS[color.lower()+"_player"], 
          bg="#2C3E50", font=("Arial", 14, "bold")).place(x=10, y=10)
    status = Label(player_frame, text="", bg="#2C3E50", width=20)
    status.place(x=10, y=40)
    power_label = Label(player_frame, bg="#2C3E50")
    power_label.place(x=180, y=40)
    power_labels[color] = power_label


turn_label = Label(root, text="", fg="white", background=COLORS["board_bg"], font=("Arial", 24, "bold"))
turn_label.place(x=770, y=50)
# Function to update power indicators
def update_power_indicators(color):
    """Update the power image for the player based on active powers."""
    if color in power_labels:
        power_label = power_labels[color]
        active_powers = [p for p in PLAYER_POWERS[color] if p not in POWER_USED[color]]
        if active_powers:
            # Show the first unused power
            power_label.config(image=power_images[active_powers[0]])
        else:
            # Clear image if no unused powers
            power_label.config(image="")


def turn():
    global turn_label
    for frame in player_frames:
        for widget in frame.winfo_children():
            if isinstance(widget, Label) and widget.cget("text") == "ACTIVE":
                widget.destroy()
    active_color = ""
    if RED:
        active_color = "RED"
    elif BLUE:
        active_color = "BLUE"
    elif GREEN:
        active_color = "GREEN"
    elif YELLOW:
        active_color = "YELLOW"
    active_index = ["RED", "BLUE", "GREEN", "YELLOW"].index(active_color)
    status_label = Label(player_frames[active_index], text="ACTIVE",
                         fg="white", bg=COLORS[active_color.lower()+"_player"],
                         font=("Arial", 10, "bold"))
    status_label.place(x=10, y=40)
    if PLAYER_TYPES[active_color] == PlayerType.AI:
        roll_button.config(state="disabled")
    else:
        roll_button.config(state="normal")

dice_frame = Frame(dashboard, bg="#2C3E50", width=100, height=100)
dice_frame.place(x=75, y=450)

def roll():
    global rollc, dice, dice1, dice2, TURN, rolls, puzzle_active
    if puzzle_active:
        print("Roll blocked: puzzle active")
        return
    if TURN:
        rollc = rollc + 1
        print(f"Rolling, rollc={rollc}")
        if rollc == 1:
            dice = random.randint(1, 6)
            display_dice(dice)
            print(f"dice: {dice}")
            rolls.append(dice)
            if dice != 6:
                rollc = 0
                TURN = False
        elif rollc == 2:
            if dice == 6:
                dice1 = random.randint(1, 6)
                display_dice(dice1)
                rolls.append(dice1)
                print(f"dice1: {dice1}")
                if dice1 != 6:
                    rollc = 0
                    TURN = False
        elif rollc == 3:
            if dice1 == 6:
                dice2 = random.randint(1, 6)
                display_dice(dice2)
                rolls.append(dice2)
                print(f"dice2: {dice2}")
                if dice2 == 6:
                    print("Three sixes rolled, turn ends")
                    rolls = []
                    rollc = 0
                    TURN = False
                else:
                    rollc = 0
                    TURN = False
        print(f"Roll complete, rolls={rolls}, TURN={TURN}")

        
def display_dice(value):
    global current_dice_value
    current_dice_value = value
    for widget in dice_frame.winfo_children():
        widget.destroy()
    dice_bg = Label(dice_frame, text=str(value), bg="white", fg="#2C3E50",
                    width=3, height=1, font=("Arial", 24, "bold"))
    dice_bg.place(x=25, y=25)
    dice_value = Label(dashboard, text=f"Rolled: {value}", fg="white",
                       bg="#34495E", font=("Arial", 14))
    dice_value.place(x=75, y=560)
    update_dice_history()

def update_dice_history():
    if not hasattr(update_dice_history, 'dice_history_labels'):
        update_dice_history.dice_history_labels = []
    for label in update_dice_history.dice_history_labels:
        label.destroy()
    update_dice_history.dice_history_labels = []
    history_frame = Frame(dashboard, bg="#34495E", width=80, height=80)
    history_frame.place(x=160, y=450)
    history_title = Label(history_frame, text="History:", bg="#34495E", fg="white", 
                         font=("Arial", 10))
    history_title.pack(anchor="w", padx=2, pady=2)
    if rolls:
        history_text = " → ".join([str(r) for r in rolls])
    else:
        history_text = " -"
    history_label = Label(history_frame, text=history_text, bg="#34495E", fg="yellow", 
                         font=("Arial", 10, "bold"))
    history_label.pack(anchor="w", padx=5)
    update_dice_history.dice_history_labels.append(history_title)
    update_dice_history.dice_history_labels.append(history_label)

from tkinter import ttk
current_dice_value = 1
dice_frame = Frame(dashboard, bg="#2C3E50", width=100, height=100)
dice_frame.place(x=75, y=450)

style = ttk.Style()
style.configure("TButton", 
                font=("Arial", 14, "bold"),
                padding=10)

roll_button = ttk.Button(root, text="ROLL", style="TButton", command=roll)
roll_button.place(x=800, y=610)
main()
root.mainloop()