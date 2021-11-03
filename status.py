from csv import reader


def handle_line(line, debts):
    spender = line[2]
    amount = float(line[0])
    involved = line[3].split(" ")
    toPay = amount / len(involved)
    for user in involved:
        if (user == spender):
            continue
        debts.append([user, spender, toPay])


def printDebt(debt):
    print(debt[0] + " owes " + str(debt[2]) + " to " + debt[1])


def get_status(*args):
    with open("expense_report.csv", 'r') as csv:
        expenses = reader(csv)
        debts = []
        # Parcours des dettes
        for expense in expenses:
            handle_line(expense, debts)
        finalDebts = []
        for i in debts:
            isPresent = False
            for j in finalDebts:
                if i[0] == j[0] and i[1] == j[1]:
                    isPresent = True
                    j[2] = i[2] + j[2]
                # if i[0] == j[1] and i[1] == j[0]:
                #     isPresent = True
                #     if (j[2] - i[2] > 0):
                #         j[2] = j[2] - i[2]
                #     elif (j[2] - i[2] == 0):
                #         finalDebts.remove(j)
                #     else:
                #         toPay = i[2] - j[2]
                #         j[0] = i[0]
                #         j[1] = i[1]
                #         j[2] = toPay
            if not isPresent:
                finalDebts.append(i)
        # Affichage des dettes
        for debt in finalDebts:
            printDebt(debt)
    return True
