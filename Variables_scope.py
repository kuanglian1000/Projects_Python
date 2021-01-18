
#1.Convert "8.8" to a float.
a = "8.8"
print(float(a)/2)

#2.Convert 8.8 to an integer (with rounding).
b = 8.8
c = int(b)
print(c)

#3.Convert "8.8" to an integer (with rounding).
d = int(float("8.8")) #string -> float -> int , 有浮點數的string無法直接轉成integer
print(d)

#4.Convert 8.8 to a string.
e = str(8.8)
print(e)

#5.Convert 8 to a string.
f = str(8)
print(f)

#6.Convert 8 to a float.
g = float(8)
print(g)

#7.Convert 8 to a boolean.
h = bool(8)
print(h)

# 檢查資料型態是否正確
def typeTest():    
    correct_input = False #boolean value

    while not correct_input:
        try:
            height = int(input("Enter height of rectangle:"))
            width = int(input("Enter width of rectangle:"))
        except ValueError:
            print("Please enter valid intgers for the height or width")
        else:
            correct_input = True

    print("Your height is %d and width is %d" % (height , width))