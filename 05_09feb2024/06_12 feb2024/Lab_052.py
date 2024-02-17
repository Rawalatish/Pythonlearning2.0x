browser = input("Enter the browser name")  # or browser = str(input("Enter the browser name"))
                                            # browser = browser.lower()   |
match browser:
    case "chrome":
        print("chrome code executed")
    case "firefox":
        print("firefox code executed")
    case _:
        print("no browser found")