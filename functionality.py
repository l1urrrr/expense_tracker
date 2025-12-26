from expense import Expense

def show_budget():
    inp_budget = float(input("Enter budget: "))
    return inp_budget

budget = show_budget()
expense = Expense



def write2file(expense):
    with open("expenses.txt", "a") as file:
        text ="  name :{}\ncategory :{}\namount :{}\n ||".format(
            expense.name,expense.category,expense.amount)
        file.write(text)
def readfile(): #might be redundant?
    with open("expenses.txt", "r") as file:
        text = file.read()
        return text
def sum_expenses():
    total = 0 # initialize total
    with open("expenses.txt", "r") as file: #open file and close it when done
        chunks  = file.read().split("||") # read each line and separate into
        # groups
        for y in chunks: #loop through each chunk
            if not chunks.strip():
                continue
            lines = y.split("\n")
            for line in lines:
                if line.startswith("amount"):
                    amount = float(line.split(":")[1])
                    total += amount
    return total

def rem_budget():
    global budget
    sum = sum_expenses()
    new_budget = float(budget-sum)
    return new_budget




#basic summary - shows total spent and how much budget left for the month
#customs - add percentages on what expenses they were spent on ? average
# spent per expense? median amount spent? average of each category?

