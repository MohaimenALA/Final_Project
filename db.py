import csv

def read_money_amount():
    try:
        with open ('money.txt', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                return float(row[0])
    except FileNotFoundError:
        Max_Bet = 1000
        player_money = Max_Bet
        print("Data file not found.")
        return None

def write_money_amount(amount):
    try:
        with open('money.txt', 'w') as file:
            writer = csv.writer(file)
            writer.writerow([amount])
    except FileNotFoundError:
        print("Data file not found.")