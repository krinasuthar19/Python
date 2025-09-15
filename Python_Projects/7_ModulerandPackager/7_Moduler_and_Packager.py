import datetime, time, math, random, uuid, importlib, file_ops

# ================= Datetime & Time =================
def datetime_menu():
    while True:
        print("\nDatetime & Time Ops:")
        print("1. Current date & time")
        print("2. Date difference")
        print("3. Custom format")
        print("4. Stopwatch")
        print("5. Countdown")
        print("6. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            print("Current:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif ch == "2":
            try:
                d1 = input("Enter first date (dd/mm/yyyy): ")
                d2 = input("Enter second date (dd/mm/yyyy): ")

                # ✅ Strict format check
                date1 = datetime.strptime(d1, "%d/%m/%Y")
                date2 = datetime.strptime(d2, "%d/%m/%Y")

                diff = abs((date2 - date1).days)
                print("Difference:", diff, "days")
                break   # ✅ exit loop if success

            except ValueError:
                print("Wrong format! Try again with right format (dd/mm/yyyy)")
        elif ch == "3":
            d = datetime.datetime.now()
            print("Formatted:", d.strftime("%A, %d %B %Y"))
        elif ch == "4":
            input("Press Enter to start...")
            start = time.time()
            input("Press Enter to stop...")
            end = time.time()
            print("Elapsed:", round(end - start, 2), "secs")
        elif ch == "5":
            sec = int(input("Enter seconds: "))
            while sec > 0:
                print(sec, end="\r")
                time.sleep(1)
                sec -= 1
            print("Time up!")
        elif ch == "6":
            return
        else:
            print("Invalid choice")

# ================= Math =================
def math_menu():
    while True:
        print("\nMath Ops:")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Circle")
        print("5. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))
        elif ch == "2":
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))
            ci = p * ((1 + r / 100) ** t)
            print("Compound Interest:", round(ci, 2))
        elif ch == "3":
            ang = math.radians(float(input("Enter angle: ")))
            print("sin:", round(math.sin(ang), 4), "cos:", round(math.cos(ang), 4))
        elif ch == "4":
            r = float(input("Radius: "))
            print("Area:", round(math.pi * r * r, 2))
        elif ch == "5":
            return
        else:
            print("Invalid choice")

# ================= Random =================
def random_menu():
    while True:
        print("\nRandom Ops:")
        print("1. Random number")
        print("2. Random list")
        print("3. Random password")
        print("4. Random OTP")
        print("5. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            print("Number:", random.randint(1, 100))
        elif ch == "2":
            lst = random.sample(range(1, 50), 5)
            print("List:", lst)
        elif ch == "3":
            ln = int(input("Password length: "))
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%"
            pw = "".join(random.choice(chars) for _ in range(ln))
            print("Password:", pw)
        elif ch == "4":
            otp = "".join(str(random.randint(0, 9)) for _ in range(6))
            print("OTP:", otp)
        elif ch == "5":
            return
        else:
            print("Invalid choice")

# ================= UUID =================
def uuid_menu():
    print("\nGenerated UUID:", uuid.uuid4())

# ================= File Ops (Custom Module) =================
def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        fch = input("Enter choice: ")

        if fch == "1":
            fname = input("Enter file name: ")
            file_ops.create_file(fname)

        elif fch == "2":
            fname = input("Enter file name: ")
            data = input("Enter data: ")
            file_ops.write_file(fname, data)

        elif fch == "3":
            fname = input("Enter file name: ")
            file_ops.read_file(fname)

        elif fch == "4":
            fname = input("Enter file name: ")
            data = input("Enter data to append: ")
            file_ops.append_file(fname, data)

        else:
            print("Back to Main Menu")

# ================= Explore dir() =================
def explore_dir():
    mod = input("Enter module name: ")
    try:
        m = importlib.import_module(mod)
        print("Attributes:\n", dir(m))
    except:
        print("Module not found")

# ================= Main Menu =================
print("Welcome to Multi-Utility Toolkit!")
while True:
    print("\nMenu:")
    print("1. Datetime & Time")
    print("2. Math")
    print("3. Random")
    print("4. UUID")
    print("5. File Ops")
    print("6. Explore dir()")
    print("7. Exit")
    c = input("Enter choice: ")

    if c == "1":
        datetime_menu()
    elif c == "2":
        math_menu()
    elif c == "3":
        random_menu()
    elif c == "4":
        uuid_menu()
    elif c == "5":
        file_menu()
    elif c == "6":
        explore_dir()
    elif c == "7":
        print("Thanks for using Toolkit!")
        break
    else:
        print("Invalid choice")
