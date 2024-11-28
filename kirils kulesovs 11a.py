import random


class Casino:
        def __init__(self):
            self.balance = 1000
            self.running = True

        def display_menu(self):
            print("\n Laipni lūdzam Popova vārzā nosauktajā kazino!")
            print("Jūsu bilance", self.balance)
            print("1. Spēle rulete.")
            print("2. Papildinat savu bilancu.")
            print("3. Iziet.")

        def add_balance(self):
            try:
                amount = int(input("Ievadiet numuru: "))
                if amount > 0:
                    self.balance += amount
                    print("Bilance veiksmīgi papildinata!")
                else:
                    print("Ievadiet pareizo numuru!")
            except ValueError:
                ("Ievadiet pareizo numuru!")

        def play_roulette(self):
            if self.balance <= 0:
                print("Nevar spēlet ruletu, jūsu bilance ir 0 vai mazāk!")
                return

            print("\n Laipni lūdzam rulete!")
            print("Jūsu opcijas ir: ")
            print("1. Numura (0-36) - x35")
            print("2. Krasa (Red/Black) - x2")
            print("3. Pāra/Nepāra - x2")

            choice = int(input("Jūsu izvēle ir:  "))
            if choice not in [1, 2, 3]:
                print("Izvēlieties vienu no iespējām!")
                return

            try:
                bet = int(input("Summa ir: "))
                if bet <= 0:
                    print("Likme nevar būt mazaka par nulli!")
                elif bet > self.balance:
                    print("Likme nevar būt lielak par jūsu bilance!")
                    return

                if choice == 1:
                    number = int(input("Izvēle numuru (0-36): "))
                    if number < 0 or number > 36:
                        print("Ievadiet pareizo numuru!")
                        return
                    self.spin_roulette(bet, "number", number)

                elif choice == 2:
                    color = input("Izvēle krāsu (Sarkans/melns): ").lower()
                    if color not in ["Sarkans", "Melns"]:
                        print("Ievadiet pareizo krāsu!")
                        return
                    self.spin_roulette(bet, "color", color)

                elif choice == 3:
                    parity = input("Izvēle paritāte (Pāra/nepāra): ").lower()
                    if parity not in ["pāra", "nepāra"]:
                        print("Ievadiet pareizu pāritatu!")
                        return
                    self.spin_roulette(bet, "parity", parity)

            except ValueError:
                print("Nepareizi!")

        def spin_roulette(self, bet, bet_type, bet_value):
            print("Rulete griežas....")
            winning_number = random.randint(0, 36)
            winning_color = "Sarkans" if winning_number % 2 == 0 else "Melns"
            winning_parity = "Pāra" if winning_number % 2 == 0 else "Nepāra"

            print(f"Numurs ir: {winning_number} ({winning_color})")

            if bet_type == "number":
                if bet_value == winning_number:
                    winnings = bet * 35
                    self.balance += winnings
                    print("Apsveicam! Tu uzvarēsi!")
                else:
                    self.balance -= bet
                    print("Tu zaudēji!")

            elif bet_type == "color":
                if bet_value == winning_color:
                    winnings = bet * 2
                    self.balance += winnings
                    print("Apsveicam! Tu uzvarēsi!")
                else:
                    self.balance -= bet
                    print("Tu zaudēji!")

            elif bet_type == "parity":
                if bet_value == winning_parity:
                    winnings = bet * 2
                    self.balance += winnings
                    print("Apsveicam! Tu uzvarēsi!")
                else:
                    self.balance -= bet
                    print("Tu zaudēji!")

        def start(self):
            while self.running:
                self.display_menu()
                try:
                    choice = int(input("Jūsu izvēle ir: "))
                    if choice == 1:
                        self.play_roulette()
                    elif choice == 2:
                        self.add_balance()
                    elif choice == 3:
                        print("Paldies par piedalīšanos!")
                        self.running = False
                    else:
                        print("Izvēlieties vienu no iespējām!")
                except ValueError:
                    print("Izvēlieties vienu no iespējām!")


if __name__ == "__main__":
    casino = Casino()
    casino.start()