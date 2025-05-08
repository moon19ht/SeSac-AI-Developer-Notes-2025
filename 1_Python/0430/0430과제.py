
words = ["assembly", "java", "rain", "notebook", "north", 
            "south", "hospital", "programming", "house", "hour"]

#TODO 문제1. filter를 사용해서 글자수가 6글자 이상인 단어만 출력하기 (컴프리핸션X)

long_words = list(filter(lambda word: len(word) >= 6, words))
print("문제1 결과:", long_words)

#TODO 문제2. map함수를 사용해서 글자를 대문자로 바꾸어서 출력하기  (컴프리핸션X)

upper_words = list(map(str.upper, words))
print("문제2 결과:", upper_words)

#TODO 문제3. sorted 함수를 사용하여 단어들의 길이순으로 오름차순 정렬하여 출력하기

sorted_by_length = sorted(words, key=len)
print("문제3 결과:", sorted_by_length)

#TODO 문제4. sorted 함수를 사용하여 알파벳 순으로 내림차순으로 정렬하여 출력하기 

sorted_reverse_alpha = sorted(words, reverse=True)
print("문제4 결과:", sorted_reverse_alpha)

#TODO 문제5. 단어중에 o가 포함되는 단어가 모두 몇개인지 카운트하기 (힌트,filter를 사용)     

words_with_o = list(filter(lambda word: 'o' in word, words))
print("문제5 결과: {}개".format(len(words_with_o)))

# zip함수 => 파이썬만 제공한다. 리스트가 2개이상 있는데 이걸 조합해서 새로운 형태로 만든다.
# ["a", b, c]와 [1, 2, 3]을 zip하면 [('a', 1), ('b', 2), ('c', 3)]로 만들어준다.
