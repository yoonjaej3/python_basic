def convert(num):
    return ((9/5)*num)+32

print("변환하고 싶은 섭씨 온도를 입력해 주세요")
value2 = float(input())
print("섭씨온도 : ", value2)
print("화씨온도 : ", round(convert(value2),2))