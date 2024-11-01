lst = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                x, y, z = date.split("/")
                if len(x) == 1:
                    x = "0" + x
                if len(x) > 2:
                    continue
                if len(y) == 1:
                    y = "0" + y
                if int(x) > 12:
                    continue
                if int(y) > 31:
                    continue
                new_date = [y, x, z]
                new_str = new_date[::-1]
                date = " ".join(new_str)
                print(date.replace(" ", "-"))
                break
            else:
                x, y, z = date.split(" ")
                if "," not in y:
                    continue
                else:
                    y = y.replace(",", "")
                for i in lst:
                    if x == i:
                        x = str(lst.index(i) + 1)
                if len(x) == 1:
                    x = "0" + x
                if len(y) == 1:
                    y = "0" + y
                if len(y) > 2:
                    continue
                if int(y) > 31:
                    continue
                new_date = [z, x, y]
                date = " ".join(new_date)
                print(date.replace(" ", "-"))
                break
        except ValueError:
            break
        except SyntaxError:
            break
        except NameError:
            break
        except MemoryError:
            break
        except KeyError:
            break
        except EOFError:
            break


main()
