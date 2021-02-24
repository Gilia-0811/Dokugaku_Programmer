# http://tinyurl.com/z2m2115

numbers = [3, 5]

while True :
    answer = input("1～10の数字を1つ、もしくは'q'を入力してください。：")
    if answer == "q" :
        break
    try :
        answer = int(answer)
    except ValueError :
        print("入力方法が間違っています。")
    if answer in numbers :
        print("正解です。")
    else :
        print("不正解です。")
