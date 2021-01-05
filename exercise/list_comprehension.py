books = list()

books.append({'제목': '개발자의 코드', '출판연도': '2013.02.28', '출판사': 'A 출판', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B 출판 ', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A 출판 ', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B 출판 ', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'C 출판 ', '쪽수': 248, '추천유무': True})

result1 = [book['제목'] for book in books if book['쪽수'] > 250]
result2 = [book['제목'] for book in books if book['추천유무'] == True]
result3 = set([book['출판사'].strip() for book in books])
print(result1)
print(result2)
print(result3)
