# 1-1 Output Function
a = 123
b = 123.456
c = 'Python'
# Print
print(a)
print(b)
print(c)
# , 連接字串
print('a=',a)
print('b=',b)
print('c=',c)
# end = , 不跳行
print(a , end = ' 不跳行 ')
print()
# 格式化輸出 format(變數,'格式化字符') 靠左 < , 靠右 > , 置中 ^ , 
# 整數 d , 浮點數 f , 字串 s
print("==格式化輸出 format(變數,'格式化字符')==")
print(format(a,'5d'))
print(format(b,'15f'))
print(format(c,'20s'))

print(format(a,'<5d'))
print(format(b,'<15f'))
print(format(c,'^20s'))
print(format(c,'>20s'))

# 格式化輸出 '%格式化字符'%(變數清單) 預設均靠右 , 靠左要加上 - 負號 , 
print("==格式化輸出 '%格式化字符'%(變數清單) ==")
print('%10d'%(a))
print('%15.5f'%(b)) #15.5f 總長度為15(含小數點及小數),小數位數保留5位
print('%15f'%(b)) #15f 總長度為15(含小數點及小數),變數長度不足則小數位數補0
print('%10s'%(c))

print('%-10d'%(a))
print('%-15.5f'%(b)) #15.5f 總長度為15(含小數點及小數),小數位數保留5位
print('%-15f'%(b)) #15f 總長度為15(含小數點及小數),變數長度不足則小數位數補0
print('%-10s'%(c))

# 預設 整數採 10進位輸出 , 轉16進位 加上 x , 轉8進位 加上 o , 轉2進位 加上 b
print("==整數轉換(format) ==")
print(format(a,'5d'))
print(format(a,'5x'))
print(format(a,'5o'))
print(format(a,'5b'))

# 預設 整數採 10進位輸出 , 可轉16進位 加上 x , 可轉8進位 加上 o , 不能轉2進位
print("==整數轉換('%'%()) ==")
print('%5d'%(a))
print('%5x'%(a))
print('%5o'%(a))
# print('%5b'%(a)) # %% 不支援 2進位轉換

# 字串的轉義字元 \\ = (印出\) , \n =(跳行) , \t=(跳8格) , \'=(印出') , \"=(印出")
print('K\\L')
print('K\nL')
print('KL\tC')
print('K\'L\'C')
print('K\"L\'C')


# CH1-2 輸入函式 eval , int
# s = input()
a , b = eval(input('two numbers(以逗號分隔): ')) 
#要用eval,才能抓出多個值 ;使用int()轉型,只能對單一值
#輸入數值時,要用逗號分隔 ex.1 ,4
#輸入多值時,不能輸入字串
print(a , b)

# CH1-3 算術運算式
# / 浮點數 ; // 整數 ; % 餘數 ; ** 次方
a = 5 / 3  #a = 1.67
b = 5 // 3 #b = 1
c = 5 % 3 #c = 2
d = 5 ** 3 #d = 125
print('a=%5f b=%d c=%d d=%d '%(a,b,c,d))

# CH1-4 算術指定運算子
a = 100
a += 100
print(a) #200
a -= 1
print(a) #199
a *= 3
print(a) #199 * 3 = 600 -3 = 597
a /= 2
print(a) #597 / 2 = 298.5
a //= 2
print(a) #298.5 // 2 = 149.0
a %= 2
print(a) # 149.0 % 2 = 1.0
a **= 2
print(a) # 1.0 ** 2 = 1.0

# CH1-5 math數字模組下的函式
import math
print('pi=',math.pi)
print('e=',math.e)

# ceil(x) , 取天花板整數
print(math.ceil(3.2)) # 4
# floor(x) , 取地板整數
print(math.floor(3.2)) # 3
# fabs(x) , 取絶對值
print(math.fabs(-34.56)) #34.56
# ex
print(math.exp(2))
# loge(x)
print(math.log(10))
# logbase(x)
print(math.log(100,10))
# 取平方根
print(math.sqrt(100))

# CH1-6 python 內建函式
# 取絕對值 , abs
print(abs(-897))
# 取數列最大值 , max(1,2,5,6,22,-1)
print(max(1,2,5,6,22,-1))
# 取數列最小值 , min(-1,44,55,23)
print(min(-1,44,55,23))
# 計算次方 , x的y次方 , pow(x,y)
print(pow(2,3))
# 取最接近x的整數 , round(x)
print(round(2.11)) # 2
print(round(2.87)) # 3
print(round(2.5)) # 2 , 注意這不是4捨5入哦
print(round(2.4)) # 2
# 取4捨5入至小數點後n位的浮點數 , round(x,n)
print(round(1.483728374829,3)) #1.483


310314
