#攝氏('C') 轉換成 華氏('F') 程式

#讓使用者輸入 攝氏溫度
#然後印出華氏溫度
#＋ - * /

c = input('請輸入攝氏溫度：')
c = float(c) #int是整數；float是點數
f = c * 9 / 5 + 32 #好的寫法有空格
print('華氏溫度： ', f)
