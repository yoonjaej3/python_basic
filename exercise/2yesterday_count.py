file = open('yesterday.txt', 'r')
yesterday_lyric = file.read()
print("YESTERDAY라는 단어가",yesterday_lyric.upper().count('YESTERDAY'),"번 나왔습니다.")
print("Yesterday라는 단어가",yesterday_lyric.count('Yesterday'),"번 나왔습니다.")
print("yesterday라는 단어가",yesterday_lyric.count('yesterday'),"번 나왔습니다.")
file.close()