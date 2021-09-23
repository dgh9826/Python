from wordcloud import WordCloud
from PIL import Image
import numpy as np
text = ''
with open("kakaopy.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[3:]:
        if '] [' in line:
            text+= line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('이모티콘\n','').replace('사진\n','')
# print(text)


wc = WordCloud(font_path='C:/Windows/Fonts/NanumGothicBold.TTF', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

mask = np.array(Image.open('Untitled.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/NanumGothicBold.TTF', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")

