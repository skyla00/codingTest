# 첫째 줄 n과 x 가 주어짐.
# map(int, ["10", "20"])  →  [10, 20] (이터레이터 형태)
# map 결과를 N, X 두 변수에 언패킹(분해)
N, X = map(int, input().split())

# 둘째 줄 수열 a 를 이루는 정수 n개가 주어짐.
number = list(map(int, input().split()))

# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력.
for i in number:
    if i < X:
        print(i, end = " " )