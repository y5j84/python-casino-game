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
        
        # Game buttons
        button_frame = tk.Frame(self.root, bg='#2C3E50')
        button_frame.pack(pady=20)
        
        # High Roller button
        self.high_roller_btn = tk.Button(
            button_frame,
            text="🎯 HIGH ROLLER\nBeat the Dealer\nPayout: 2x",
            font=('Arial', 12, 'bold'),
            bg='#E74C3C',
            fg='white',
            width=15,
            height=3,
            command=self.play_high_roller
        )
        self.high_roller_btn.grid(row=0, column=0, padx=10, pady=5)
        
        # Lucky 7 button
        self.lucky7_btn = tk.Button(
            button_frame,
            text="🍀 LUCKY 7\nRoll Exactly 7\nPayout: 4x", 
            font=('Arial', 12, 'bold'),
            bg='#9B59B6',
            fg='white',
            width=15,
            height=3,
            command=self.play_lucky7
        )
        self.lucky7_btn.grid(row=0, column=1, padx=10, pady=5)
        
        # Double Trouble button
        self.double_btn = tk.Button(
            button_frame,
            text="🎲 DOUBLE TROUBLE\nRoll Matching Dice\nPayout: 3x",
            font=('Arial', 12, 'bold'), 
            bg='#3498DB',
            fg='white',
            width=15,
            height=3,
            command=self.play_double_trouble
        )
        self.double_btn.grid(row=0, column=2, padx=10, pady=5)
        
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
        
        self.update_buttons_state()
    
    def get_bet_amount(self):
        try:
            bet = int(self.bet_var.get())
            if bet < 5:
                messagebox.showwarning("Invalid Bet", "Minimum bet is $5!")
                return None
            if bet > self.balance:
                messagebox.showwarning("Insufficient Funds", "You don't have enough balance!")
                return None
            return bet
        except ValueError:
            messagebox.showerror("Invalid Bet", "Please enter a valid bet amount!")
            return None
    
    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)
    
    def update_dice_display(self, dice1, dice2):
        # Unicode dice characters
        dice_chars = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
        
        # Animate dice roll
        for i in range(8):
            temp1 = random.randint(1, 6)
            temp2 = random.randint(1, 6)
            self.dice_label1.config(text=dice_chars[temp1-1])
            self.dice_label2.config(text=dice_chars[temp2-1])
            self.root.update()
            time.sleep(0.1)
        
        # Show final result
        self.dice_label1.config(text=dice_chars[dice1-1])
        self.dice_label2.config(text=dice_chars[dice2-1])
        total = dice1 + dice2
        self.dice_total_label.config(text=f"Total: {total}")
        
        return total
    
    def play_high_roller(self):
        bet = self.get_bet_amount()
        if bet is None:
            return
        
        self.disable_buttons()
        self.result_label.config(text="Rolling against the dealer...")
        
        # Player roll
        player_dice = self.roll_dice()
        player_total = self.update_dice_display(player_dice[0], player_dice[1])
        
        time.sleep(1)
        
        # Dealer roll
        self.result_label.config(text="Dealer is rolling...")
        dealer_dice = self.roll_dice()
        dealer_total = self.update_dice_display(dealer_dice[0], dealer_dice[1])
        
        # Determine result
        if player_total > dealer_total:
            winnings = bet * 2
            self.balance += winnings
            result = f"🎉 YOU WIN! You {player_total} vs Dealer {dealer_total}\nYou win ${winnings}!"
            color = '#2ECC71'
        elif player_total < dealer_total:
            self.balance -= bet
            result = f"😞 YOU LOSE! You {player_total} vs Dealer {dealer_total}\nYou lose ${bet}."
            color = '#E74C3C'
        else:
            result = f"🤝 TIE! Both rolled {player_total}. Your bet is returned."
            color = '#F1C40F'
        
        self.result_label.config(text=result, fg=color)
        self.update_display()
        self.enable_buttons()
    
    def play_lucky7(self):
        bet = self.get_bet_amount()
        if bet is None:
            return
        
        self.disable_buttons()
        self.result_label.config(text="Rolling for Lucky 7...")
        
        dice1, dice2 = self.roll_dice()
        total = self.update_dice_display(dice1, dice2)
        
        if total == 7:
            winnings = bet * 4
            self.balance += winnings
            result = f"🎉 JACKPOT! LUCKY 7! 🎉\nYou win ${winnings}!"
            color = '#2ECC71'
        else:
            self.balance -= bet
            result = f"😞 No luck! Rolled {total}, needed 7.\nYou lose ${bet}."
            color = '#E74C3C'
        
        self.result_label.config(text=result, fg=color)
        self.update_display()
        self.enable_buttons()
    
    def play_double_trouble(self):
        bet = self.get_bet_amount()
        if bet is None:
            return
        
        self.disable_buttons()
        self.result_label.config(text="Rolling for doubles...")
        
        dice1, dice2 = self.roll_dice()
        total = self.update_dice_display(dice1, dice2)
        
        if dice1 == dice2:
            winnings = bet * 3
            self.balance += winnings
            result = f"🎉 DOUBLE {dice1}s! 🎉\nYou win ${winnings}!"
            color = '#2ECC71'
        else:
            self.balance -= bet
            result = f"😞 No doubles! Rolled {dice1} and {dice2}.\nYou lose ${bet}."
            color = '#E74C3C'
        
        self.result_label.config(text=result, fg=color)
        self.update_display()
        self.enable_buttons()
    
    def update_display(self):
        self.balance_label.config(text=f"💰 BALANCE: ${self.balance}")
        self.update_buttons_state()
        
        # Check if game over
        if self.balance <= 0:
            messagebox.showinfo("Game Over", "You've run out of money! Game reset.")
            self.reset_game()
    
    def update_buttons_state(self):
        # Enable/disable buttons based on balance
        state = 'normal' if self.balance >= 5 else 'disabled'
        self.high_roller_btn.config(state=state)
        self.lucky7_btn.config(state=state)
        self.double_btn.config(state=state)
    
    def disable_buttons(self):
        self.high_roller_btn.config(state='disabled')
        self.lucky7_btn.config(state='disabled')
        self.double_btn.config(state='disabled')
    
    def enable_buttons(self):
        if self.balance >= 5:
            self.high_roller_btn.config(state='normal')
            self.lucky7_btn.config(state='normal')
            self.double_btn.config(state='normal')
    
    def reset_game(self):
        self.balance = 100
        self.bet_var.set("10")
        self.dice_label1.config(text="⚀")
        self.dice_label2.config(text="⚀")
        self.dice_total_label.config(text="Total: 0")
        self.result_label.config(
            text="Place your bet and choose a game!", 
            fg='#ECF0F1'
        )
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceCasinoGUI(root)
    root.mainloop()