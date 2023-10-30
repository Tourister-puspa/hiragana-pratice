import random
import pykakasi
import jpconvert
import time

i = 45
start = time.time()
text = ["あ","い","う","え","お","か","さ","た","な","は","ま","や","ら","わ","き","し","ち","に","ひ","み","り","く","す","つ","ぬ","ふ","む","ゆ","る","け","せ","て","ね","へ","め","れ","こ","そ","と","の","ほ","も","よ","ろ","を","ん"]
faute = []
while i >0 :
    kks = pykakasi.kakasi()
    question = random.choice(text)
    result = kks.convert(question)
    answer = input("Quel est la prononciation de "+ question + "?")
    for item in result:
        print("{}[{}]".format(item['orig'],item['hepburn'].capitalize()), end='')
        print()
    if item['hepburn'] == answer:print("Correct"), text.remove(question) 
    else: print("Incorrect" + "," + " " + "vous avez épelé", jpconvert.romajiToJapanese(answer)), faute.append(question), faute.append(item['hepburn'])
    i = i - 1
    print("Plus que", i, "caractères")


end = time.time()
final = end - start
print("Voici vos fautes",faute)
print("Vous avez terminé cette série en ", final//60, "minutes", "et", float(final%60), "secondes")






    





