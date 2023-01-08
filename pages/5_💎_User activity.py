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



response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/28af17d1-e325-450a-b634-7a65297c9076/data/latest")

x = response.json()
y = response.json()
z = response.json()
w = response.json()


for i in range (len(x)) :
  x[i] = ((x[i]['AVG(TX_COUNT)']) )
  y[i] = ((y[i]['AVG (TOKENS_COUNT)']) )
  z[i] = ((z[i]['AVG (USD_VALUE)']) )
  w[i] = ((w[i]['AVG (ETH_VALUE)']) )


# general metrics  #mint process 
response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63949aa0-5ece-44c9-978f-bce4f09a7fcb/data/latest")


c = response.json()
b = response.json()
v = response.json()
n = response.json()

for i in range (len(x)) :

  c[i] = ((c[i]['AVG(TX_COUNT)']) )
  b[i] = ((b[i]['AVG (TOKENS_COUNT)']) )
  v[i] = ((v[i]['AVG (USD_VALUE)']) )
  n[i] = ((n[i]['AVG (ETH_VALUE)']) )


with open('model1.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



col111, col1112 = st.columns([0.5, 0.5])
with col111 :
  st.info('')  
  st.markdown('* **Buyers info**')
with col1112 : 
  st.info('')
  st.markdown('* **Sellers info**')

col1, col2,col3, col4 = st.columns([0.5, 0.5, 0.5, 0.5])
with col1 : 
  st.metric("Average Number of Purchase Transactions Per User", x[0])
  st.metric("Average Number of NFT Purchase Per User", y[0])
with col2 : 
  st.metric("Average USD Volume of Purchase Per User", z[0])
  st.metric("Average ETH Volume of Purchase Per User", w[0])
with col3 : 
  st.metric("Average Number of Sale Transactions Per User", c[0])
  st.metric("Average Number of Sold NFT Per User", b[0])
with col4 : 
  st.metric("Average USD Volume of Sales Per User", v[0])
  st.metric("Average ETH Volume of Sales Per User", n[0])


#-------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------
col1, col2 = st.columns([0.5, 0.5])
with col1 :

  st.markdown('* **TOP 10 Buyers in terms of Volume Of Transactions in USD**')    
  #bar - chart left 1 
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/9b72833c-0842-47a0-bff7-3d8a67a23fdc/data/latest")
  x = response.json()
  y = response.json()
  for i in range (len(x)) :
    x[i] = ((x[i]['BUYER_ADDRESS']) )
    y[i] = ((y[i]['USD_VALUE']) )

  option21 = {
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
                {"value":y[2], "itemStyle":{"color":"#FFFF00"}},
                {"value":y[3], "itemStyle":{"color":"#00FF00"}},
                {"value":y[4], "itemStyle":{"color":"#0000FF"}},
                {"value":y[5], "itemStyle":{"color":"#00FFFF"}},
                {"value":y[6], "itemStyle":{"color":"#FF00FF"}},
                {"value":y[7], "itemStyle":{"color":"#00FFFF"}},
                {"value":y[8], "itemStyle":{"color":"#FF7D00"}},
                {"value":y[9], "itemStyle":{"color":"#FFFF00"}},

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
  st_echarts( option21)





  st.markdown('* **TOP 10 Buyers in terms of Volume Of Transactions in ETH**')    
  #bar - chart left 1 
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/afc30541-f8b1-4e37-875d-7d32b35884da/data/latest")
  x = response.json()
  y = response.json()
  for i in range (len(x)) :
    x[i] = ((x[i]['BUYER_ADDRESS']) )
    y[i] = ((y[i]['ETH_VALUE']) )

  option22 = {
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
                {"value":y[2], "itemStyle":{"color":"#FFFF00"}},
                {"value":y[3], "itemStyle":{"color":"#00FF00"}},
                {"value":y[4], "itemStyle":{"color":"#0000FF"}},
                {"value":y[5], "itemStyle":{"color":"#00FFFF"}},
                {"value":y[6], "itemStyle":{"color":"#FF00FF"}},
                {"value":y[7], "itemStyle":{"color":"#00FFFF"}},
                {"value":y[8], "itemStyle":{"color":"#FF7D00"}},
                {"value":y[9], "itemStyle":{"color":"#FFFF00"}},

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
  st_echarts( option22)

  #----------------------------------------------------
  st.markdown('* **Number of Buyers based on Theirs Transactions**')    
  #pie - chart left 1
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/84cc1765-845d-4240-9248-22d35befa407/data/latest")
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
#----------------------------------------------------
  # full_detailed tablel right 1
  st.markdown('* **TOP 5 Buyer in terms of Number of Transactions .**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/b1ff0098-7e73-45ef-a096-eb8872cee8d8/data/latest")
  r = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  r = load_data()
  r



#----------------------------------------------------

#---------------------------------------------------------------------------------------------
with col2 :


  st.markdown('* **TOP 10 Sellers in terms of Volume Of Transactions in USD**')    
  #bar - chart left 1 
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/b47a9aeb-469f-49e2-a507-27a8e4da223e/data/latest")
  x = response.json()
  y = response.json()
  for i in range (len(x)) :
    x[i] = ((x[i]['SELLER_ADDRESS']) )
    y[i] = ((y[i]['USD_VALUE']) )

  option23 = {
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
                {"value":y[2], "itemStyle":{"color":"#FFFF00"}},
                {"value":y[3], "itemStyle":{"color":"#00FF00"}},
                {"value":y[4], "itemStyle":{"color":"#0000FF"}},
                {"value":y[5], "itemStyle":{"color":"#00FFFF"}},
                {"value":y[6], "itemStyle":{"color":"#FF00FF"}},
                {"value":y[7], "itemStyle":{"color":"#00FFFF"}},
                {"value":y[8], "itemStyle":{"color":"#FF7D00"}},
                {"value":y[9], "itemStyle":{"color":"#FFFF00"}},

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
  st_echarts( option23)

  



  

  st.markdown('* **TOP 10 Sellers in terms of Volume Of Transactions in ETH**')    
  #bar - chart left 1 
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/6cc77e81-45a6-4be4-b93d-4fa4e3bd8823/data/latest")
  x = response.json()
  y = response.json()
  for i in range (len(x)) :
    x[i] = ((x[i]['SELLER_ADDRESS']) )
    y[i] = ((y[i]['ETH_VALUE']) )

  option24 = {
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
                {"value":y[2], "itemStyle":{"color":"#FFFF00"}},
                {"value":y[3], "itemStyle":{"color":"#00FF00"}},
                {"value":y[4], "itemStyle":{"color":"#0000FF"}},
                {"value":y[5], "itemStyle":{"color":"#00FFFF"}},
                {"value":y[6], "itemStyle":{"color":"#FF00FF"}},
                {"value":y[7], "itemStyle":{"color":"#00FFFF"}},
                {"value":y[8], "itemStyle":{"color":"#FF7D00"}},
                {"value":y[9], "itemStyle":{"color":"#FFFF00"}},

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
  st_echarts( option24)

  st.markdown('* **Number of Sellers based on Theirs Transactions**')    
  #pie - chart right 1 
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/dbed6614-925a-48b9-a759-8a4671be6dcf/data/latest")
  x = response.json()
  option17 = {
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
  st_echarts(option17)

#----------------------------------------------------
  # full_detailed tablel right 1
  st.markdown('* **TOP 5 Sellers in terms of Number of Transactions .**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/19ff9f12-506c-458f-a638-5ede7d4a17f6/data/latest")
  rr = response.json()
  def load_data() : 
        return pd.DataFrame(response.json())
  load_data()
  rr = load_data()
  rr

st.info('')
