# 코드포스 281A Word Capitalization
import sys
put = sys.stdin.readline

word = put().strip()
print(word[0].upper() + word[1:])