import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
import base64


st.set_page_config(
    page_title="Doodles",
    page_icon = ":brain:",
    layout="wide",
    menu_items=dict(About="made by ALI and AUstin"))

#-------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------

# background color 
st.markdown("""<style>.main {background-color: #C8D3E0;color:#010101}</style>""",unsafe_allow_html=True)
hi = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/premium-vector/blue-white-gray-turquoise-background-gradient-wallpaper-background-vector-illustration_172010-1295.jpg?w=360");
background-size: 450%;
background-position: top right;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://img.freepik.com/premium-vector/blue-white-gray-turquoise-background-gradient-wallpaper-background-vector-illustration_172010-1295.jpg?w=360"); 
background-position: center; 
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
#url("data:image/png;base64,{img}");
st.markdown(hi, unsafe_allow_html=True)


st.image('https://images.squarespace-cdn.com/content/v1/61ac9cf1e52ca44ca9f17a09/d842d9d8-8abc-433b-a435-f3f309cf12b5/Doodles+1.png')
st.info('')
st.header('Trader Part')


response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/2ef56ea7-f34f-460e-94a1-2985174f9b7f/data/latest")

x = response.json()
y = response.json()



for i in range (len(x)) :
  x[i] = ((x[i]['AVG (USD_PROFIT)']) )
  y[i] = ((y[i]['AVG (ETH_PROFIT)']) )



col1, col2,col3, col4 = st.columns([ 0.5, 0.5, 0.5, 0.5])
with col1 : 
  st.markdown('')
with col2 : 
  st.metric("Average NET USD Profit / Loss Per Traders", x[0])
with col3 : 
  st.metric("Average NET ETH Profit / Loss Per Traders", y[0])
with col4 : 
  st.markdown('')
st.info('')

with open('model1.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



#-------------------------------------------------------------------------------------------------

col11, col12 = st.columns([ 0.5, 0.5])
with col11 : 
  st.markdown('* **Top 10 profitable traders With Most Earned ETH**')    
  #pie - chart left 1
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/8a19280a-dd06-46b1-b89d-2d86de79b7ae/data/latest")
  x = response.json()
  option15 = {
      "title": {
      "text": '',
      "subtext": '',
      "left": 'center'
    },
    "tooltip": {
      "trigger": 'item'
    },
    "legend": {
      "orient": 'vertical',
      "left": 'up'
    },
    "series": [
      {
        "name": 'Access From',
        "type": 'pie',
        "radius": '50%',
        "data":  x,
        "emphasis": {
          "itemStyle": {
            "shadowBlur": 10,
            "shadowOffsetX": 0,
            "shadowColor": 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  }
  st_echarts(option15)


  st.markdown('* **Top 10 profitable traders With Most Earned ETH**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/657c139c-7aaa-4b5f-98aa-55d1c36ee35b/data/latest")
  rrr2233 = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  rrr2233 = load_data()
  rrr2233


  st.markdown('* **Top 10 Unprofitable traders With Most Lost ETH**')    
  #pie - chart left 1
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/c20379c2-d608-496d-841c-3eb15943d135/data/latest")
  x = response.json()
  option155 = {
      "title": {
      "text": '',
      "subtext": '',
      "left": 'center'
    },
    "tooltip": {
      "trigger": 'item'
    },
    "legend": {
      "orient": 'vertical',
      "left": 'left'
    },
    "series": [
      {
        "name": 'Access From',
        "type": 'pie',
        "radius": '50%',
        "data":  x,
        "emphasis": {
          "itemStyle": {
            "shadowBlur": 10,
            "shadowOffsetX": 0,
            "shadowColor": 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  }
  st_echarts(option155)

  st.markdown('* **Top 10 profitable traders With Most Earned ETH**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/9e89dba6-bbde-4c9a-b4d8-38e575b9a3d9/data/latest")
  rrr2 = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  rrr2 = load_data()
  rrr2
st.info('')

with col12 : 

  st.markdown('* **Top 10 profitable traders With Most Earned USD**')    
  #pie - chart left 1
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/17543921-caa6-4cb8-a3af-a63c9b57978b/data/latest")
  x = response.json()
  option15 = {
      "title": {
      "text": '',
      "subtext": '',
      "left": 'center'
    },
    "tooltip": {
      "trigger": 'item'
    },
    "legend": {
      "orient": 'vertical',
      "left": 'left'
    },
    "series": [
      {
        "name": 'Access From',
        "type": 'pie',
        "radius": '50%',
        "data":  x,
        "emphasis": {
          "itemStyle": {
            "shadowBlur": 10,
            "shadowOffsetX": 0,
            "shadowColor": 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  }
  st_echarts(option15)


  st.markdown('* **Top 10 profitable traders With Most Earned USD**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/d1afbdd5-224d-417c-bade-c06d65abcf58/data/latest")
  rrr22 = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  rrr22 = load_data()
  rrr22


  st.markdown('* **Top 10 Unprofitable traders With Most Lost USD**')    
  #pie - chart left 1
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/ffcd0266-e1d3-4849-b37e-fc4d4db0a34b/data/latest")
  x = response.json()
  option15 = {
      "title": {
      "text": '',
      "subtext": '',
      "left": 'center'
    },
    "tooltip": {
      "trigger": 'item'
    },
    "legend": {
      "orient": 'vertical',
      "left": 'left'
    },
    "series": [
      {
        "name": 'Access From',
        "type": 'pie',
        "radius": '50%',
        "data":  x,
        "emphasis": {
          "itemStyle": {
            "shadowBlur": 10,
            "shadowOffsetX": 0,
            "shadowColor": 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  }
  st_echarts(option15)
  st.markdown('* **Top 10 Unprofitable traders With Most Lost USD**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/6cb1b97c-4725-4a0b-aabe-9139893926bc/data/latest")
  rrr223 = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  rrr223 = load_data()
  rrr223

#-------------------------------------------------------------------------------------------------
col159, col259 = st.columns([0.5, 0.5])
with col159 :

  st.markdown('* **Total ETH Profits and Loss for all traders**')    
  #bar - chart left 1 
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/3b2ceccf-6a8a-4aed-9100-113c307e2fdb/data/latest")
  x = response.json()
  y = response.json()
  for i in range (len(x)) :
    x[i] = ((x[i]['name']) )
    y[i] = ((y[i]['value']) )

  option211 = {
        "toolbox": {
        "show": "true",
        "feature": {
          "dataZoom": {
            "yAxisIndex": "none"
          },
          "dataView": {
            "readOnly": "false"
          },
          "magicType": {
            "type": ["line", "bar"]
          },
          "restore": {"show":"true"},
        }
      },
        "xAxis": {
            "type": 'category',
            "data": x
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [
                {"value":y[0], "itemStyle":{"color":"#FF0000"}}, 
                {"value":y[1], "itemStyle":{"color":"#FF7D00"}},
                {"value":y[2], "itemStyle":{"color":"#FFFF00"}}
  

                ],
            "type": 'bar'

        }],
        "tooltip": {
                        "show": "true"
                    },
        "label": {
            "show":"true"
        },
        
                        
        }
  st_echarts( option211)



  st.markdown('* **Distribution of USD Profits and Loss Amount per trader**')    
  #pie - chart left 1
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/5e507085-9f01-4d73-a8d3-3fa58337d1f7/data/latest")
  x = response.json()
  option115 = {
      "title": {
      "text": '',
      "subtext": '',
      "left": 'center'
    },
    "tooltip": {
      "trigger": 'item'
    },
    "legend": {
      "orient": 'vertical',
      "left": 'left'
    },
    "series": [
      {
        "name": 'Access From',
        "type": 'pie',
        "radius": '50%',
        "data":  x,
        "emphasis": {
          "itemStyle": {
            "shadowBlur": 10,
            "shadowOffsetX": 0,
            "shadowColor": 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  }
  st_echarts(option115)

with col259 :
  st.markdown('* **Total USD Profits and Loss for all traders**')    
  #bar - chart left 1 
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/d4cb24dc-f834-4108-ba7e-1d7624774283/data/latest")
  x = response.json()
  y = response.json()
  for i in range (len(x)) :
    x[i] = ((x[i]['name']) )
    y[i] = ((y[i]['value']) )

  option220 = {
        "toolbox": {
        "show": "true",
        "feature": {
          "dataZoom": {
            "yAxisIndex": "none"
          },
          "dataView": {
            "readOnly": "false"
          },
          "magicType": {
            "type": ["line", "bar"]
          },
          "restore": {"show":"true"},
        }
      },
        "xAxis": {
            "type": 'category',
            "data": x
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [
                {"value":y[0], "itemStyle":{"color":"#FF0000"}}, 
                {"value":y[1], "itemStyle":{"color":"#FF7D00"}},
                {"value":y[2], "itemStyle":{"color":"#FFFF00"}}


                ],
            "type": 'bar'

        }],
        "tooltip": {
                        "show": "true"
                    },
        "label": {
            "show":"true"
        },
        
                        
        }
  st_echarts( option220)

  #----------------------------------------------------
  st.markdown('* **Distribution of ETH Profits and Loss Amount per trader**')    
  #pie - chart left 1
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/f6cf5fdd-351f-4341-9286-a7a4797d2505/data/latest")
  x = response.json()
  option1512 = {
      "title": {
      "text": '',
      "subtext": '',
      "right": 'right'
    },
    "tooltip": {
      "trigger": 'item'
    },
    "legend": {
      "orient": 'vertical',
      "left": 'left'
    },
    "series": [
      {
        "name": 'Access From',
        "type": 'pie',
        "radius": '50%',
        "data":  x,
        "emphasis": {
          "itemStyle": {
            "shadowBlur": 10,
            "shadowOffsetX": 0,
            "shadowColor": 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  }
  st_echarts(option1512)


#----------------------------------------------------
st.info('')
col1519, col2519 = st.columns([0.5, 0.5])
with col1519 :



  # full_detailed tablel right 1
  st.markdown('* **Top 10 profitable Tokens With Most Earned ETH for trader**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/0ec5e913-c7fb-4ba9-8f57-b46277ee7291/data/latest")
  r = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  r = load_data()
  r

  # full_detailed tablel right 1
  st.markdown('* **Top 10 UnProfitable Tokens With Most Lost ETH for trader**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/c7a42a1a-fd9f-4ff9-8a9c-5b7f786a6868/data/latest")
  rr = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  rr = load_data()
  rr
with col2519 :

#----------------------------------------------------
  # full_detailed tablel right 1
  st.markdown('* **Top 10 profitable Tokens With Most Earned USD for trader**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/b88458b4-26b2-48c6-b69a-dda8fb7defb2/data/latest")
  rrr = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  rrr = load_data()
  rrr


    # full_detailed tablel right 1
  st.markdown('* **Top 10 UnProfitable Tokens With Most Lost USD for trader**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/e8a1cb5b-87b2-404d-8612-d295acb6b7be/data/latest")
  r1 = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  r1 = load_data()
  r1
#---------------------------------------------------------------------------------------------
st.info('')
