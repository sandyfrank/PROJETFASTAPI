import streamlit as st

def main():
    """ Deploying streamlit with docker """
    
    st.title("Sandy Frank streamlit App")
    st.header("Deploying streamlit with docker")
    
    activities = ["EDA", "Plots"]
    
    age = ["25-35", "36-45"]
    
    choices1 = st.sidebar.selectbox('Select Activities',activities)
    
    choices2 = st.sidebar.selectbox('Select Age',age)
    
    if choices1 == "EDA":
        st.subheader("EDA")
    elif choices1 == "Plots":
        st.subheader('Visualization')
        
    if choices2 == "25-35":
        st.subheader('what can a young man do')
    else:
        st.subheader('You are already old')
        
        
        
if __name__ == '__main__':
    main()