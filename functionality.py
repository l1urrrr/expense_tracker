from expense import Expense
budget = 0
expense = Expense


def write2file(input):
    with open("expenses.csv", "a") as file:
        text =" ||name :{}\ncategory :{}\namount :{}\n ||".format(
            input.name,input.category,input.amount)
        file.write(text)
