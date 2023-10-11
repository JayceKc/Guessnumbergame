# guessing number

secret_num = 50
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while secret_num != guess and not (out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = int(input("請輸入第一個數字："))
        if guess < secret_num:
            print("大一點")

        elif guess > secret_num:
            print("小一點")
    else:
        out_of_limit = True

if out_of_limit:
    print("you fuck up")

else:
    print("win")