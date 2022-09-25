def ask():
    while True:
        try:
            numb = int(input('pls give me integer'))
        except:
            print('pls gimme right INTEgeR number, no othe rshit')
            continue
        else:
            print(numb**2)
            break
        finally:
            print("this is finally statement")

ask()

