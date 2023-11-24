import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.snow()
st.title("Shikhant Saini")
st.subheader("Bazinga!")

col1, col2=st.columns([3,1])
with col1:
    st.subheader("About Me")
    st.text("Always open to learn new skills. The world of data science \namuses me and I am curious to gain knowledge about various \ntechnologies we use to bring out insights.")
with col2:
    image=Image.open("me.jpg")
    st.image(image,width=350)

#Sidebar w/ Download
st.sidebar.caption("Wish to connect?")
st.sidebar.write("shikhantsaini89@gmail.com")

#rb means converting pdf to raw binary format
pdf_file=open("Resume.pdf","rb")
st.sidebar.download_button("Download Resume",pdf_file,file_name="Resume.pdf",mime="pdf")

tab_skills,tab_exp,tab_pro,tab_cont,tab_pic=st.tabs(['Skills','Experience','Projects','Contact Me','Take a picture'])

with tab_exp:
    #Experience
    st.subheader("Relevant Experience")
    experience_table=pd.DataFrame({
        "Job Title":["Role 1","Role 2","Role 3"],
        "Company":["Company 1","Company 2","Company 3"]
    })
    experience_table=experience_table.set_index("Job Title")
    st.table(experience_table)

with tab_pro:
    st.subheader("Projects")
    titanic_data = pd.read_csv('titanic.csv')
    interval = alt.selection_interval()
    bar_chart = alt.Chart(titanic_data).mark_bar().encode(
        x = 'sum(Survived):Q',
        y = 'Pclass:N',
        color = 'Pclass:N',
    ).properties(
        width = 300
    )
    scatter_plot = alt.Chart(titanic_data).mark_point().encode(
        x = 'Age:Q',
        y = 'Fare:Q',
        color = alt.condition(interval, 'Sex', alt.value('lightgray')),
    ).properties(
        width = 500,
        height = 400
    ).add_selection(
        interval
    ).interactive()
    # Define a selection to filter the scatter plot based on the selected passenger 
    selection = alt.selection_single(fields=['Pclass'], empty = 'none')
    bar_chart = bar_chart.add_selection(selection)
    scatter_plot = scatter_plot.transform_filter(selection)
    #put any jupiter chart in streamlit just add st.altair_chart()
    st.altair_chart(bar_chart | scatter_plot)

with tab_skills:
    #Skills section in the form of bar chart

    skill_data=pd.DataFrame(
        {
            "Skills level":[90,60,60,90],
            "Skills":["Python","Tableau","mySQL","Rstudio"]
        }
    )
    skill_data=skill_data.set_index('Skills')
    with st.container():
        st.subheader("Skills")
        st.bar_chart(skill_data)
    with st.expander("See More Skills"):
        st.write("...")

with tab_pic:
    #take a picture
    picture = st.camera_input("Take a picture with me")
    if picture:
        st.image(picture)