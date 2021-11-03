from PyInquirer import prompt
from csv import writer
from user import getUsersList
expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "list",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": getUsersList()
    },
    {
        "type": "checkbox",
        "name": "involved",
        "message": "New Expense - Involved People : ",
        "choices": getUsersList(),
    }
]


def new_expense(*args):
    infos = prompt(expense_questions)
    expenseFileName = open("expense_report.csv", "a+")
    expenseFile = writer(expenseFileName)
    # Test if spender is user
    amount = 0
    spender = infos["spender"]
    # Test Valid Amount
    try:
        amount = float(infos["amount"])
    except:
        print("Invalid Amount")
        expenseFileName.close()
        return False
    # Check Involved People
    involved = infos["involved"]
    # No Body is involved
    if (not involved):
        print("Invalid Involved people selection")
        expenseFileName.close()
        return False
    # Spender not involved
    if not spender in involved:
        ask = "Is this expense also for you ? [y/n]"
        if (ask.lower() == "y"):
            involved.append(spender)
    involvedString = ""
    for i in involved:
        if not involvedString:
            involvedString = i
        else:
            involvedString = involvedString + ' ' + i
    expenseFile.writerow([amount, infos["label"], spender, involvedString])
    # Closing files
    expenseFileName.close()
    print("Expense Added !")
    return True
