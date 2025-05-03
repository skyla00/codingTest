# 마름모 찍기
# 윗 부분, 아랫 부분 나눠서 찍기.
# 윗 부분은 정삼각형 처럼.
# 아랫 부분은 역삼각형.
# 0, 1, 2, 3, 4 까지 찍혀 있으니.
# 아랫 부분은 3, 2, 1, 0 인덱스를 가져야 함.
# range(start, stop, step)
# start : 시작 값
# stop : 끝 값
# step : 증가 또는 감소 폭
# 0까지 출력 하려면 -1 로 해야 함.
# range(a-2, -1, -1)
# reversed(range(0, a - 1))

a = int(input())

for i in range(a):
    print(" " * (a-(i+1)), end="")
    print("*" * (i*2+1))
for i in range(a-2, -1, -1):
    print(" " * (a - i - 1), end="")
    print("*" * (i * 2 + 1))
