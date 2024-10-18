# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止

import random
# 1.告訴使用者需要輸入的數字範圍 input()
guess_number_max = int (input("請輸入猜測範圍(最大值)："))
guess_number_min = int (input("請輸入猜測範圍(最小值)："))
guess_limit = int(input("請輸入限制猜測次數："))
answer_number = int(random.randint(guess_number_min,guess_number_max))
# 2.使用者猜對要回傳「恭喜中獎」，並結束迴圈的執行
while guess_limit >= 0:
    print(f"猜測範圍為{guess_number_min} ~ {guess_number_max}，剩餘猜測次數為{guess_limit}")
    user_guess_number = int (input("請輸入猜測的數字："))
    guess_limit -= 1
    if user_guess_number < guess_number_min or user_guess_number > guess_number_max:
        print(f"超出猜測範圍，請重新猜測，猜測範圍為{guess_number_min} ~ {guess_number_max}")
    elif user_guess_number < answer_number:
        guess_number_min = user_guess_number
        print(f"猜錯了，請重新猜測，猜測範圍為{guess_number_min} ~ {guess_number_max}")
    elif user_guess_number > answer_number:
        guess_number_max = user_guess_number
        print(f"猜錯了，請重新猜測，猜測範圍為{guess_number_min} ~ {guess_number_max}")
    elif user_guess_number == answer_number:
        print("恭喜答對了")
        break
if(guess_limit == 0):
    print(f"你失敗了，正確答案為{answer_number}")
# 3.超出範圍要顯示「超出範圍請重新輸入」


# 4.數字太大 要提示「請輸入更小的數字」


# 5.數字太小 要提示「請輸入更大的數字」


