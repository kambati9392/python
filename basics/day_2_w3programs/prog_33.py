month=input("Enter the month name").lower().strip()
match "month":
    case "jan":
        print(31)
    case "feb":
        print(28/29)
    case "mar":
        print(31)
    case "april":
        print(30)
    case "may":
        print(31)
    case "june":
        print(30)
    case "july" | "august":
            print(31)
    # case "august":
    #     print(31)
    case "sep":
        print(30)
    case "oct":
        print(31)
    case "nov":
        print(30)
    case "dec":
        print(31)
    case _:
        print("not valid month name")