import requests
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
def chatbot_response(message):
    str1=message
    tokens=word_tokenize(str1)
    dis=tokens[len(tokens)-1]
    link='https://disease-info-api.herokuapp.com/diseases/'+dis
    page = requests.get(link)
    a=page.json()
    a=a['disease']
    if "symptoms" in str1:
        x=a['symptoms']
        return x
    elif "prevention" in str1:
        x=a['prevention']
        return x
    elif "treatment" in str1:
        x=a['treatment']
        return x
    elif "diagnosis" in str1:
        x=a['diagnosis']
        return x
    else:
        link1='https://medlineplus.gov/'+dis+'.html'
        page1=requests.get(link1)
        soup=BeautifulSoup(page1.content,'html.parser')
        data=soup.find_all('p')
        x=data[3].get_text()
        return x
if __name__=='__main__':
    print("Type EXIT to QUIT")