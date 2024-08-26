#match statement
#ex-1
browser_name = input("What is your browser :\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":                 # It is case-sensitive
        print("Browser accepted")
    case "chrome":
        print("Browser accepted")
    case "edge":
        print("Browser accepted")
    case _:
        print("Browser not found")

#ex-2

browser_name = input("What is your browser :\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox" | "chrome" | "edge":                 # we can use | for multiple options.
        print("Browser accepted")
    case _:
        print("Browser not found")

