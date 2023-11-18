# while running this program use a pin for login is "abc1234"
import tkinter as tk
from tkinter import messagebox, simpledialog

class ATM_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Interface")

        # Initialize account balance and PIN (you might want to fetch this from a database)
        self.balance = 0.0
        # This is my own pin if you can change then enter your pin in code
        self.pin = "abc1234"
        self.transaction_history = []

        # Entry widget for PIN
        self.pin_entry = tk.Entry(self.root, show="*", width=20)
        self.pin_entry.pack(pady=10)

        # Button for login
        self.login_button = tk.Button(self.root, text="PIN for login", command=self.login)
        self.login_button.pack(pady=5)

    def login(self):
       entered_pin = self.pin_entry.get()
       if entered_pin == self.pin:
           self.show_menu()
       else:
           messagebox.showerror("Login Error", "Incorrect PIN. Please try again.")

    def show_menu(self):
        #Destroy login widgets
        self.pin_entry.destroy()
        self.login_button.destroy()

        # Create new widgets for the main menu
        self.label_balance = tk.Label(self.root, text=f"Balance: Rs.{self.balance:.2f}")
        self.label_balance.pack(pady=10)

        self.amount_entry = tk.Entry(self.root, width=20)
        self.amount_entry.pack(pady=5)

        self.check_balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack(pady=5)

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.transfer_button = tk.Button(self.root, text="Transfer", command=self.transfer)
        self.transfer_button.pack(pady=5)

        self.history_button = tk.Button(self.root, text="Transaction History", command=self.show_history)
        self.history_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack(pady=5)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is: Rs.{self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Invalid amount. Please enter a positive value.")

            self.balance += amount
            self.transaction_history.append(f"Deposited Rs.{amount:.2f}")
            self.update_balance_label()
            messagebox.showinfo("Deposit", f"Deposited Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.amount_entry.delete(0, tk.END)

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Invalid amount. Please enter a positive value.")

            if amount > self.balance:
                raise ValueError("Insufficient funds.")

            self.balance -= amount
            self.transaction_history.append(f"Withdrawn Rs.{amount:.2f}")
            self.update_balance_label()
            messagebox.showinfo("Withdraw", f"Withdrawn Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.amount_entry.delete(0, tk.END)

    def transfer(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Invalid amount. Please enter a positive value.")

            recipient = simpledialog.askstring("Transfer", "Enter recipient's account number:")
            if recipient:
                self.balance -= amount
                self.transaction_history.append(f"Transferred Rs.{amount:.2f} to account No: {recipient}")
                self.update_balance_label()
                messagebox.showinfo("Transfer", f"Transferred Rs.{amount:.2f} to account No: {recipient}. New balance: Rs.{self.balance:.2f}")
            else:
                messagebox.showinfo("Transfer", "Transfer canceled.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.amount_entry.delete(0, tk.END)

    def show_history(self):
        history_text = "\n".join(self.transaction_history)
        if history_text:
            messagebox.showinfo("Transaction History", history_text)
        else:
            messagebox.showinfo("Transaction History", "No transactions yet.")

    def update_balance_label(self):
        self.label_balance.config(text=f"Balance: Rs.{self.balance:.2f}")


def main():
    root = tk.Tk()
    app = ATM_GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
