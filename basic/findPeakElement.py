# 1. nums = [1, 2, 3, 1] >> 출력: 2
# 2. nums = [1, 2, 1, 3, 5, 6, 4] >> 출력: 5 (nums[5] = 6, nums[1] = 2
# 이진 탐색으로 풀이

from typing import List
def findPeakElement(nums: List[int]) -> int:
    # 가장 왼쪽, 오른족 인덱스 설정
    left = 0
    right = len(nums) - 1

    # 이진 탐색 시작
    while left < right:
        # 가운데 값 저장
        mid = (left + right) // 2
        # mid가 오른쪽 값보다 작으면, 피크는 오른쪽에.
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            # mid가 오른쪽보다 크면, 피크는 왼쪽에 존재하거나 mid일 수 있음
            right = mid
    # left == right가 되는 순간이 피크 요소
    return left