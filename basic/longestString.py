def length_of_longest_substring(s: str) -> int:
    # 문자들이 저장될 set (중복 확인용)
    char_set = set()

    # 왼쪽 포인터 (슬라이딩 윈도우의 시작)
    left = 0
    max_length = 0

    # 오른쪽 포인터는 반복문으로 이동
    for right in range(len(s)):
        # 중복이 있는 경우, 왼쪽 포인터를 옮기면서 중복 제거
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # 중복이 없으면 set에 추가하고 최대 길이 갱신
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length