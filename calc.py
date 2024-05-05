class Calculator:
    def __init__(self):
        self.money_in = []
        self.money_out = []
        self.total_money_in = 0
        self.total_money_out = 0
        self.total_money_summary = 0
        

    def input_money_in(self):
        amount = int(input("Masukkan nominal uang:"))
        self.money_in.append(amount)
        self.total_money_in += amount
        self.total_money_summary += amount

    
    def input_money_out(self):
        amount = int(input("Masukkan uang nominal keluar: "))
        self.money_out.append(amount)
        self.total_money_out += amount
        self.total_money_summary -= amount
        
    def total_money_in_summarize(self):
        print(f">>>> 💸 Total Jumlah Uang Masuk 💸: {self.total_money_in}")

    def total_money_out_summarize(self):
        print(f">>>> 💸 Total Jumlah Uang Keluar 💸: {self.total_money_out}")

    def total_money(self):
        print(f">>>> 💸 Total uang sekarang 💸: {self.total_money_summary}")


    def run(self):
        while True:
            print("Simple Machine Calculate Money")
            print("1. Input Uang Masuk")
            print("2. Input Uang Keluar")
            print("3. Total Uang Masuk")
            print("4. Total Uang Keluar")
            print("5. Sisa Uang")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.input_money_in()
            if choice == "2":
                self.input_money_out()
            if choice == "3":
                self.total_money_in_summarize()
            if choice == "4":
                self.total_money_out_summarize()
            if choice == "5":
                self.total_money()
            if choice == "6":
                break

if __name__ == "__main__":
    cashier_machine = Calculator();
    cashier_machine.run();



