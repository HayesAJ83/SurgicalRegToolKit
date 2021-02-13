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
    page = st.sidebar.radio('Go to:',
                            ["Registrar Toolkit",
                             "Excision Ltd Team",])

    if page ==   "Registrar Toolkit":       show_explore()
    elif page == "Excision Ltd Team":       show_the_app_team()

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
    st.write('''_# UNDER CONSTRUCTION # UNDER CONSTRUCTION # UNDER CONSTRUCTION #_''')
    st.markdown('''# RIE General Surgery Registrar ToolKit''')
    exp = st.radio('Go to:',
                                ["About",
                                 "Regional Hospitals",
                                 "UGI / General Surgery Dept at RIE",
                                 "Emergency Teams (ET1/ET2)",
                                 "Elective Work",
                                 "Reg Rota",
                                 "Useful info at work",
                                 "Useful info for Edinburgh",
                                 "Tips from ex-Fellows",
                                 ])
    
    if   exp == "About":                                exp_about()             #1
    elif exp == "Regional Hospitals":                   exp_Lothian()           #2
    elif exp == "UGI / Gen Surg Dept at RIE":           exp_UGI()               #3
    elif exp == "Emergency Teams (ET1/ET2)":            exp_ET()                #4
    elif exp == "Elective Work":                        exp_Elective()          #5
    elif exp == "Reg Rota":                             exp_Rotas()             #6
    elif exp == "Useful info at work":                  exp_InWork()            #7
    elif exp == "Useful info for Edinburgh":            exp_OutWork()           #8
    elif exp == "Tips from ex-Fellows":                 exp_Tips()              #9 

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About (1)                                                                                      #
# ::: Handles                                                                                     #                                                                                              
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_about():
#Page
    st.markdown("---")
    st.subheader('Who is this App for?')
    st.write('''We designed this App to help visiting Fellows settle into the local Department of surgery and
                living in Edinburgh.''')
    st.subheader('How to use this App?')
    st.write('Select from options above to access different types of helpful information. Below is a summary of the different options.')
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Regional Hospitals:</span>
                   <span style="font-size:12pt;color:black;"> Maps and info from NHS Lothian and neighboring health boards
                   (eg. Fife, Borders, Forth Valley).</span>''',unsafe_allow_html=True)
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


    st.sidebar.markdown('''**Contribute**''')
    st.sidebar.info("Contact Maria Boland or Alastair Hayes to add useful info.")

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Lothian (2)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Lothian():
    st.markdown("---")
    st.subheader('''Regional Hospitals''')
    st.write(' ')
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalRegToolKit/main/Lothian4python_Lite.csv'
    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df2 = df1.sort_values(by=['Place'],ascending=True)
    mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
    site_lat = df2['Lat_A1']                          
    site_lon = df2['Long_A1']           
    text = df2['Place'].astype(str)
    locations_name = df2['Place']
    color= df2['Colour'].astype(str)

    types = st.radio('Hospitals:',
                     options=["Astley Ainslie Hospital",
                              "Borders General Hospital - BGH",
                              "Forth Valley Hospital",
                              "Royal Edinburgh Hospital",
                              "Royal Infirmary of Edinburgh - RIE",
                              "Spire Murrayfield",
                              "St. John's Hospital - SJH",
                              "Victoria Hospital - VHK",
                              "Western General Hospital - WGH",], index=3)
    st.markdown("---")
    figG3 = go.Figure()
    figG3.add_trace(go.Scattermapbox(lat=site_lat,lon=site_lon,mode='markers+text',
                marker=go.scattermapbox.Marker(size=12,color=color,opacity=0.8),
                text=text,hoverinfo='text',))

    if types == "Astley Ainslie Hospital":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.92982,lon=-3.19899),
                pitch=5,zoom=9.5,style='satellite-streets'))

    if types == "Borders General Hospital - BGH":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.59573,lon=-2.74245),
                pitch=5,zoom=7.0,style='satellite-streets'))

    if types == "Forth Valley Hospital":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=56.02526,lon=-3.84879),
                pitch=5,zoom=7.0,style='satellite-streets'))

    if types == "Royal Edinburgh Hospital":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.92760,lon=-3.21384),
                pitch=5,zoom=9.5,style='satellite-streets'))

    if types == "Royal Infirmary of Edinburgh - RIE":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.92137,lon=-3.13415),
                pitch=5,zoom=9.5,style='satellite-streets'))

    if types == "Spire Murrayfield":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.94431,lon=-3.26628),
                pitch=5,zoom=10,style='satellite-streets'))

    if types == "St. John's Hospital - SJH":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.89211,lon=-3.52319),
                pitch=5,zoom=8.5,style='satellite-streets'))
        
    if types == "Victoria Hospital - VHK":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=56.12519,lon=-3.15814),
                pitch=5,zoom=8.5,style='satellite-streets'))

    if types == "Western General Hospital - WGH":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.9634,lon=-3.23521),
                pitch=5,zoom=10,style='satellite-streets'))
        


    figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
    st.write(figG3)
    st.markdown('''<span style="font-size:10pt;color:black;">**Zoom** into map using **touchscreen**.</span>''', unsafe_allow_html=True)

    
#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  UGI (3)                                                                                        #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_UGI():
    st.markdown("---")
    st.subheader("The UGI / General Surgery Dept") 
    

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  ET (4)                                                                                         #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_ET():
    st.markdown("---")
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
    st.markdown("---")
    
    st.subheader("Elective - UGI / General Surgery") 
   


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Rotas (6)                                                                                      #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Rotas():
    st.markdown("---")
    st.subheader("Rotas - Link to latest version - upload into Github") 
   




#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  In Work Info (8)                                                                               #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_InWork():
    st.markdown("---")
    st.markdown('''### Helpful info for at work''')
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
    st.markdown("---")
    st.subheader("Helpful info for Edinburgh Life")
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
    st.markdown("---")
    st.subheader("Tips from our previous fellows")
    exp = st.radio('Topics:',#'Select',
                                ['Things I wish someone had told me',        # - ,
                                 ])



#-------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    main()
