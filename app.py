import pickle 
import streamlit as st 
import numpy as np 

st.header("Book Recommendation System")

model = pickle.load(open("artifacts/model.pkl", "rb"))
book_names = pickle.load(open("artifacts/book_names.pkl", "rb"))
final_rating = pickle.load(open("artifacts/final_rating.pkl", "rb"))
book_pivot = pickle.load(open("artifacts/book_pivot.pkl", "rb"))


def fetch_poster(suggestion):
    book_name = []
    idx = []
    poster_url = []

    for i in suggestion:
        book_name.append(book_pivot.index[i])
    
    for name in book_name[0]:
        id = np.where(final_rating['title'] == name)[0][0]
        idx.append(id)
    
    for i in idx:
        url = final_rating.iloc[i]['url']
        poster_url.append(url)
    
    return poster_url

def book_recommend(book_name):
    book_idx = np.where(book_pivot.index == book_name)[0][0]
    _, suggestion = model.kneighbors(book_pivot.iloc[book_idx, :].values.reshape(1,-1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]].tolist()
    
    return books, poster_url 

selected_books = st.selectbox(
    "Type or select a book",
    book_names
)

if st.button("Show Recommendation"):
    recs, poster_url = book_recommend(selected_books)
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.text(recs[1])
        st.image(poster_url[1])

    with c2:
        st.text(recs[2])
        st.image(poster_url[2])
    
    with c3:
        st.text(recs[3])
        st.image(poster_url[3])

    with c4:
        st.text(recs[4])
        st.image(poster_url[4])

    with c5:
        st.text(recs[5])
        st.image(poster_url[5])




    