## 샘플 데이터 만들기
import random

word = ["안녕", "고양이", "사과", "커피", "나무", "케이크", "쥐"]

n = 0
for i in range(50):
    if i < 8:
        n = 4
    elif i < 16:
        n = 5
    elif i<24:
        n = 6
    elif i<32:
        n = 7
    elif i<40:
        n = 8
    elif i<48:
        n = 9
    else:
        n=10

    arr = []

    for _ in range(n):
        for _ in range(n):
            arr.append(word[random.randrange(0, len(word))])
    d = {}

    for a in arr:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    result = sorted(d.items(), key=(lambda x: -x[1]))
    # print(result)

    print(n)
    for i in range(n):
        for j in range(n):
            print(arr[i*n+j], end=" ")
        print()
    # print()


## 검산, 중복 개수 확인
# for _ in range(int(input())):
#     n=int(input())
#
#     arr=[]
#     for _ in range(n):
#         ar=input().split()
#         for a in ar:
#             arr.append(a)
#     print(arr)
#     d = {}
#
#     for a in arr:
#         if a in d:
#             d[a] += 1
#         else:
#             d[a] = 1
#
#     result = sorted(d.items(), key=(lambda x: -x[1]))
#     print(result)
