from konlpy.tag import Komoran 
komoran = Komoran() #꼬꼬마 형태소 분석기 
def morph(text):
     sentences = text.split('.') 
     for sentence in sentences: 
          print('=' * 50)
          print(sentence) 
          print('morphs : ', komoran.morphs(sentence)) 
          print('pos : ', komoran.pos(sentence)) 
          print('nouns : ', komoran.nouns(sentence))

while True: 
    text = input('문장을 입력하세요 : ') 
    if text == 'exit': 
        break 
    else: 
        morph(text)

