# 코드포스 443A Anton and Letters
import sys
put = sys.stdin.readline

text = put().strip()[1:-1].split(', ')

print(len({i for i in text if i}))