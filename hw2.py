str = "My name is Jaehyeok Lim"

# 1. 문자열의 문자수를 출력하라.
print(len(str))

# 2. 문자열을 10번 반복한 문자열을 출력하라.
print(str * 10)

# 3. 문자열의 첫 번째 문자를 출력하라.
print(str[0])

# 4. 문자열에서 처음 4문자를 출력하라
print(str[:3])

# 5. 문자열에서 마지막 4문자를 출력하라.
print(str[-4:])

# 6-1. 문자열의 문자를 거꾸로 출력하라.
print(str[::-1])
# 6-2. 다른 방법
outStr = ""
count, i = 0, 0

count = len(str)

for i in range(0, count):
    outStr += str[count - (i + 1)]
print(outStr)

# 7. 문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라.
print(str[1:-1])

# 8. 문자를 모두 대문자로 변경하려 출력하라.
print(str.upper())

# 9. 문자를 모두 소문자로 변경하여 출력하라.
print(str.lower())

# 10. 문자열에서 'a'를 'e'로 대체하여 출력하라.
print(str.replace('a', 'e'))