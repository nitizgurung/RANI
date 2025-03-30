try:
    print("This is try")
    try:
        print("New try")
    except Exception as e:
        print(e)
except Exception as e:
    print("Next catch")
