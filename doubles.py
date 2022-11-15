def doubles(s: str) -> int:
    double = 0
    for i in range(len(s)):
        if s[i] == s[i+1] and s[i] == len(s):
            double += 1
    if double > 0:
        return double


print(doubles('collision'))
print(doubles('off road iss funn'))
print(doubles('ccddeeff'))
print(doubles('ccdd eeff'))
print(doubles(''))

# assert doubles('collision') == 1
# assert doubles('off road iss funn') == 3
# assert doubles('ccddeeff') == 4
# assert doubles('ccdd eeff') == 4
# assert doubles('') == 0
