import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

def get_bible_text(book, chapter, verse, version):
    url = f"https://www.biblegateway.com/passage/?search={book}+{chapter}%3A{verse}&version={version}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find("div", {"class": "passage-text"}).text.strip()
    result = re.sub(r"Read full chapter", "", result)
    result = re.sub(r"in all English translations", "", result)
    return result

def main():
    st.title("성경 검색기")
    
    book = st.text_input("성경 책 이름을 입력하세요: 창세기, 요한복음...", on_change=st.session_state.update)
    chapter = st.text_input("성경 장을 입력하세요: 숫자입력", on_change=st.session_state.update)
    verse = st.text_input("성경 절을 입력하세요: 1-10 1절부터10절까지 검색됨") # 1-10 1절부터10절까지 검색됨

    books_list = ['NIV','NIRV','NLT','KJV','KLB']

    if st.button('검색') or book and chapter and verse:
        for i in books_list:
            result = get_bible_text(book, chapter, verse, i)
            st.write('------') 
            st.write(i)
            st.write(result)
            st.write('------')

if __name__ == "__main__":
    main()
