import streamlit as st
import pandas as pd
import requests
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html


st.set_page_config(page_title="App Template", layout="wide")



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


loti1 = 'https://lottie.host/cf12dbd5-1b73-4f28-9b21-c7cbe4f458c0/6BbHPnunDG.json'
lot1 = load_lottieurl(loti1)
 

loti2= "https://assets1.lottiefiles.com/private_files/lf30_m075yjya.json"
lot2= load_lottieurl(loti2)




def main():
    col1 = st.sidebar
    col2, col3 = st.columns((4, 1))

    with col1:      
        st_lottie(lot2, key="lol",height=180, width=280)      
        with st.sidebar:
            selected = option_menu("Main Menu", ["Home", 'Página 1', 'Página 2', 'Página 3', 'Página 4'],
                               icons=['house', 'bi bi-upload', 'bi bi-file-bar-graph', 'bi bi-download', 'bi bi-arrow-right-circle'],
                               menu_icon="cast", default_index=0)


        

        add_vertical_space(3)
        st.write('Made with ❤️ by [Criss](https://github.com/cristian-data-science)')

    col2.title("App Template")
    col2.markdown("""
    Esta es una plantilla de aplicación con un menú lateral y páginas vacías.
    """)
    

        


    

    

    if selected == "Home":
        show_home(col1, col2)
    elif selected == "Página 1":
        show_empty_page(col2, "Página 1")
    elif selected == "Página 2":
        show_empty_page(col2, "Página 2")
    elif selected == "Página 3":
        show_empty_page(col2, "Página 3")
    elif selected == "Página 4":
        show_empty_page(col2, "Página 4")

def show_home(col1, col2):
    with col2:  
        st_lottie(lot1, key="loti1", height=700, width=780)

    

def show_empty_page(col2, page_name):
    with col2:
        st.markdown(f"### {page_name}")
        st.write("Esta es una página vacía.")


if __name__ == "__main__":
    main()
