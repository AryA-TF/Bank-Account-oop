from Bank_accs import * 

Dave = Bank_accs(1000, "Dave")
Sara = Bank_accs(2000, "Sara")

Dave.get_balance()
Sara.get_balance()

Sara.deposit(500)


Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)