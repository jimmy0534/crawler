import requests
from bs4 import BeautifulSoup
commentlist=[]
for i in range(1,170):
    url2 = "https://movie.daum.net/moviedb/grade?movieId=93004&type=netizen&page="+str(i)
    html2 = requests.get(url2).text
    soup2 = BeautifulSoup(html2,'html.parser')
    comment2 = soup2.find_all("p",{'class':'desc_review'})
    for comment in comment2:
        commentlist.append(comment.text.strip())

print(commentlist)
with open("movie.txt","w") as f:
    f.write(str(commentlist))
