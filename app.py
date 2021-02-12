#Copyright [2020] [EXCISION LIMITED]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import streamlit as st
import pandas as pd
pd.options.display.max_colwidth = 1000000
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotly
import plotly.express as px          
import plotly.graph_objects as go    
import plotly.figure_factory as ff
import io
import requests

#@st.cache(suppress_st_warning=True)

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Main                                                                                           #
# ::: Handles the navigation / routing and data loading / caching                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#

def main():    
    st.sidebar.subheader('Navigator')
    page = st.sidebar.radio('Go to',
                            ["Registrar Toolkit",
                             "Excision Ltd Team",])

    if page ==   "Registrar Toolkit":       show_explore()
    elif page == "Excision Ltd Team":                   show_the_app_team()

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About the team                                                                                 #
# :::                                                                                             #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_the_app_team():
    st.title("App Design Team")
    st.markdown('''The team consists of a group of General Surgeons based in Edinburgh who are
                motivated to develop software to improve surgical **data systems**,
                **research** and **education**.''')
    st.markdown('''To meet these aims, a company called **Excision** was founded in 2020, and
                **SurgicalEps** Web App was the first major project.''',unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info('''Get in touch with any comments, queries or suggestions about this
                    App:surgicaleponyms@gmail.com''')
    
    st.subheader("App Developer")
    about1 = st.checkbox("Alastair Hayes")
    if about1:
        st.markdown('''Alastair is a Specialty Training Registrar in Edinburgh with interests
                    in Upper GI, Endocrine and Emergency General Surgery. His qualifications
                    include FRCSEd (Gen Surg) & PhD.''')
        st.markdown('''He is working to develop data science and software solutions for clinical
                    data systems, research and education in surgical practice.''')

    st.subheader("Associate App Developer")
    about2 = st.checkbox('''Anne Ewing''')
    if about2:
        st.markdown('''Anne is Specialty Training Registrar in Edinburgh with interests in Upper
                    GI, Hernias and Emergency General Surgery. She is passionate about surgical
                    teaching and outside work Anne is a competitive triathlete.''')

    st.subheader("Surgical Registrar ToolKit App - Coordinator")
    about2 = st.checkbox('''Maria Boland''')
    if about2:
        st.markdown('''Maria is awesome too...detail....:)....''')

    st.subheader("Acknowledgements")
    st.markdown('''[Google](https://www.google.com/search/howsearchworks/?fg=1),
                   [Mapbox](https://www.mapbox.com),
                   [Pandas](https://pandas.pydata.org), [Plotly](https://plotly.com/python/),
                   [PubMed&reg;](http://www.ncbi.nlm.nih.gov/pubmed),
                   [Streamlit](https://www.streamlit.io)''')

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Explorer                                                                                       #
# ::: Handles the navigation                                                                      #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_explore():
    st.markdown('''# General Surgical Registrar ToolKit''')
    st.write('''_UNDER CONSTRUCTION_''')
    exp = st.radio('Go to',
                                ["About this App",
                                 "Lothian Hospitals",
                                 "UGI / General Surgery Dept",
                                 "Emergency Teams (ET1/ET2)",
                                 "Elective",
                                 "Rotas",
                                 "Useful info for work",
                                 "Useful info for outside work",
                                 "Tips & tricks from previous fellows",
                                 ])
    if   exp == "About this App":                       exp_about()             #1
    elif exp == "Lothian Hospitals":                    exp_Lothian()           #2
    elif exp == "UGI / General Surgery Dept":           exp_UGI()               #3
    elif exp == "Emergency Teams (ET1/ET2)":            exp_ET()                #4
    elif exp == "Elective":                             exp_Elective()          #5
    elif exp == "Rotas":                                exp_Rotas()             #6
    elif exp == "Useful info for work":                 exp_InWork()            #7
    elif exp == "Useful info for outside work":         exp_OutWork()           #8
    elif exp == "Tips & tricks from previous fellows":  exp_Tips()              #9 

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About (1)                                                                                      #
# ::: Handles                                                                                     #                                                                                              
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_about():

#Page
    st.write('''_UNDER CONSTRUCTION_''')
    
    st.markdown('''_A Web App from Excision Ltd_''')
    st.subheader('Introduction')
    st.markdown(' ')
    #st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:
                   #underline;">Introduction</span>''', unsafe_allow_html=True)
    st.write('''About.''')
    st.subheader('Using This App')
    st.write(' ')
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Lothian Hospitals:</span>
                   <span style="font-size:12pt;color:black;"> Maps and info.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">UGI / General Surgery Dept at RIE:</span>
                   <span style="font-size:12pt;color:black;"> Detail about our unit.</span>''',
                   unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Emergency Teams:</span>
                   <span style="font-size:12pt;color:black;"> How these work.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Elective:</span>
                   <span style="font-size:12pt;color:black;"> Days surgery, Cancer, Bariatrics, Benign Hiatal, Hernia work these work.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Rotas:</span>
                   <span style="font-size:12pt;color:black;"> How these work.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Useful info for work:</span>
                   <span style="font-size:12pt;color:black;"> Summary.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Useful info for outside work:</span>
                   <span style="font-size:12pt;color:black;"> GPs, School, Sports, Bars, Restaurants, Churches/Worship, Nightclubs, Guitar shops, Food shops, Renting.</span>''',unsafe_allow_html=True)

    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Tips & tricks:</span>
                   <span style="font-size:12pt;color:black;">Barbora, Gustav, Adam, Maria, Matteo and others.</span>''',unsafe_allow_html=True)

    st.subheader('Who Is This App For?')
    st.markdown(' ')
    st.write('''Registrars.''')
    st.subheader('Disclaimer')
    st.markdown(' ')
    st.write('''Educational purposes.''')
    st.sidebar.markdown('''**Latest News**''')
    st.sidebar.info("App will be launched March 2021")

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Lothian (2)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Lothian():
    st.markdown('''### Regional Hospitals''')
    types = st.radio('Hospital:',["Royal Infirmary of Edinburgh",
                                  "St. John's Hospital",
                                  "Western General Hospital",
                                  "Astlie Ainslee",
                                  "Borders General",])

    if types == "Royal Infirmary of Edinburgh":
        
        url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalRegToolKit/main/Lothian4python_Lite.csv'
        df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
        df2 = df1.sort_values(by=['Eponym'],ascending=True)
        st.write(df2)


    
#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  UGI (3)                                                                                        #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_UGI():
    st.subheader("The UGI / General Surgery Dept") 
    

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  ET (4)                                                                                         #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_ET():
    #st.markdown('''[Advert space for Google AdSense4]''')
    st.subheader("Emergency Take") 
    ScreenSize = st.radio('1st) Select screen size:',
                          options=['Desktop / Laptop / Tablet'],index=0)

  

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Elective (5)                                                                                   #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Elective():
    
    st.subheader("Elective - UGI / General Surgery") 
   


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Rotas (6)                                                                                      #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Rotas():
    st.subheader("Rotas - Link to latest version - upload into Github") 
   




#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  In Work Info (8)                                                                               #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_InWork():
    st.markdown('''### Helpful info for in work''')
    ScreenSize = st.radio('1st) Select screen size:',
                     options=['Smartphone',
                              'Desktop / Laptop / Tablet',],index=0)

   


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Outside Work (9)                                                                               #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_OutWork():
    st.subheader("Helpful info for Outside Work")
    exp = st.radio('1st) Choose your setting:',#'Select',
                                ['Leisure',        # - Scars, Signs, Diseases & Severity Scores",
                                 'Medical Care',   # - History of Surgery',
                                 'Child Care',     #- Incisions
                                 'Places of Worship',
                                 'Best Bars'
                                 ])

    if   exp == "Leisure":           out_leisure()       #T1 #- Scars, Signs, Severity Scores
    elif exp == 'Medical Care':      out_medical()   #T2 #- History
    elif exp == "Child Care":        out_child()        #T3 #- Incisions, Instruments & Operations
    elif exp == "Places of Worship": out_worship()
    elif exp == "Best Bars":         out_bars()




#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Tips (9)                                                                                   #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Tips():
    st.subheader("Tips from our previous fellows")
    exp = st.radio('Topics:',#'Select',
                                ['Things I wish someone had told me',        # - ,
                                 ])



#-------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    main()
