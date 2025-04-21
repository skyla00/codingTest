# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
chess = [1, 1, 2, 2, 2, 8]

# 예제 입력 : 0 1 2 2 2 7
# split()으로 하나씩 list 로 만들기
# input = list(input().split())
# 문자열로 만들어짐. > 숫자로 바꿔서 계산해야 함.
# map() 사용해서 숫자로 바꾸기
input = list(map(int, input().split()))

# end = ' ' 기본적으로 줄바꿈 되어 출력 > 줄바꿈 안 하고 공백으로 이어서 출력.
for i in range(len(chess)) :
    print(chess[i]-input[i], end = ' ')