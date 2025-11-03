"""
I acknowledge the use of ChatGPT (version GPT-4, OpenAI, https://chat.openai.com/) 
to create the game structure and GUI in this file.
"""

import random
import tkinter as tk
from tkinter import ttk, messagebox
import time

class DiceCasinoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Python Casino 🎰")
        self.root.geometry("600x700")
        self.root.configure(bg='#2C3E50')
        
        # Game state
        self.balance = 100
        self.current_bet = 10
        self.history = []
        
        self.setup_gui()
    
    def setup_gui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🎲 PYTHON CASINO 🎲", 
            font=('Arial', 20, 'bold'),
            fg='#F1C40F',
            bg='#2C3E50'
        )
        title_label.pack(pady=10)
        
        # Balance display
        self.balance_frame = tk.Frame(self.root, bg='#34495E', relief='raised', bd=2)
        self.balance_frame.pack(pady=10, padx=20, fill='x')
        
        self.balance_label = tk.Label(
            self.balance_frame,
            text=f"💰 BALANCE: ${self.balance}",
            font=('Arial', 16, 'bold'),
            fg='#2ECC71',
            bg='#34495E',
            pady=10
        )
        self.balance_label.pack()
        
        # Bet controls
        bet_frame = tk.Frame(self.root, bg='#2C3E50')
        bet_frame.pack(pady=10)
        
        tk.Label(
            bet_frame,
            text="Bet Amount:",
            font=('Arial', 12),
            fg='white',
            bg='#2C3E50'
        ).pack(side='left')
        
        self.bet_var = tk.StringVar(value="10")
        bet_spinbox = tk.Spinbox(
            bet_frame,
            from_=5,
            to=100,
            increment=5,
            textvariable=self.bet_var,
            width=10,
            font=('Arial', 12),
            justify='center'
        )
        bet_spinbox.pack(side='left', padx=10)
        
        # Dice display area
        self.dice_frame = tk.Frame(self.root, bg='#2C3E50')
        self.dice_frame.pack(pady=20)
        
        self.dice_label1 = tk.Label(
            self.dice_frame,
            text="⚀",
            font=('Arial', 80),
            bg='#2C3E50',
            fg='white'
        )
        self.dice_label1.grid(row=0, column=0, padx=20)
        
        self.dice_label2 = tk.Label(
            self.dice_frame,
            text="⚀", 
            font=('Arial', 80),
            bg='#2C3E50',
            fg='white'
        )
        self.dice_label2.grid(row=0, column=1, padx=20)
        
        self.dice_total_label = tk.Label(
            self.dice_frame,
            text="Total: 0",
            font=('Arial', 16, 'bold'),
            fg='#F1C40F',
            bg='#2C3E50'
        )
        self.dice_total_label.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Game buttons frame
        self.button_frame = tk.Frame(self.root, bg='#2C3E50')
        self.button_frame.pack(pady=20)
        
        # Result display
        self.result_label = tk.Label(
            self.root,
            text="Place your bet and choose a game!",
            font=('Arial', 14),
            fg='#ECF0F1',
            bg='#2C3E50',
            wraplength=500
        )
        self.result_label.pack(pady=10)
    
    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceCasinoGUI(root)
    root.mainloop()