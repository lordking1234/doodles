import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
import base64

st.set_page_config(layout="wide")
  


#-------------------------------------------------------------------------------------------------
# header  

st.header("")
tab1, tab2 = st.tabs(
    [
        "🪙 Mint Process",
        "💡 About Mint"
        
    ]
)

#-------------------------------------------------------------------------------------------------


# background color 
st.markdown("""<style>.main {background-color: #C8D3E0;}</style>""",unsafe_allow_html=True)

# background pucture  
#@st.experimental_memo
#def get_img_as_base64(file):
#    with open(file, "rb") as f:
#        data = f.read()
#    return base64.b64encode(data).decode()


#img = get_img_as_base64("image.jpg")

#page_bg_img = f"""
#<style>
#[data-testid="stAppViewContainer"] > .main {{
#background-image: url("https://htmlcolorcodes.com/assets/images/html-color-codes-color-tutorials-hero.jpg");
#background-size: 180%;
#background-position: top left;
#background-repeat: no-repeat;
#background-attachment: local;
#}}
#[data-testid="stSidebar"] > div:first-child {{
#background-image: url("https://htmlcolorcodes.com/assets/images/html-color-codes-color-tutorials-hero.jpg"); 
#background-position: center; 
#background-repeat: no-repeat;
#background-attachment: fixed;
#}}
#[data-testid="stHeader"] {{
#background: rgba(0,0,0,0);
#}}
#[data-testid="stToolbar"] {{
#right: 2rem;
#}}
#</style>
#"""
#url("data:image/png;base64,{img}");
#st.markdown(page_bg_img, unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------



  #-------------------------------------------------------------------------------------------------

with tab1 :
  # general metrics  #mint process 
  st.info('Since this is a popular project in cryptocurrency, we decided to check the mint process of this project .pay attention that this project was launched on the Ethereum network and the contract address of this NFT collection is 0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e .')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/e83574aa-1661-4f64-94c0-27a7c9f4094b/data/latest")

  x = response.json()
  y = response.json()
  z = response.json()
  w = response.json()
  c = response.json()
  b = response.json()
  v = response.json()
  n = response.json()
  m = response.json()

  for i in range (len(x)) :
   x[i] = ((x[i]['MINTERS']) )
   y[i] = ((y[i]['TXHASH']) )
   z[i] = ((z[i]['NFT_MINTED']) )
   w[i] = ((w[i]['ETH']) )
   c[i] = ((c[i]['USD']) )
   b[i] = ((b[i]['AVGETH']) )
   v[i] = ((v[i]['FEE']) )
   n[i] = ((n[i]['AVGUSD']) )
   m[i] = ((m[i]['AVGFEE']) )

 
  with open('model1.css') as f:
      st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

  col1, col2 ,col3, col4 = st.columns([0.5, 0.5,0.5, 0.5])
  col1.metric("Number of Minters", x[0])
  col2.metric("Number of Mint transactions", y[0])
  col3.metric("Number of NFT Minted (Total supply)", z[0])
  col4.metric("Volume of ETH paid for mint", w[0])


  col1, col2, col3,col4 = st.columns([0.5, 0.5, 0.5, 0.5])
  col1.metric("Volume of USD paid for mint", c[0])
  col2.metric("Volume of ETH paid for Fee in Average", b[0])
  col3.metric("Volume of ETH paid for Fee", v[0])
  col4.metric("Volume of USD paid for mint in Average", n[0])


  #-------------------------------------------------------------------------------------------------


  col1, col2 = st.columns([0.5, 1.5])
  with col1 :
    st.metric("Volume of ETH paid for Fee in Average", m[0])
  with col2 : 
    st.markdown('')
  st.info('As we can see, Nearly 1852 people have minted these NFTs with nearly 2148 transactions  . nearly 18k ETH have been paid as transaction fees Which is a huge number compared to the 1174 ETH paid for minting .Out Of the 10,000 unique tokens to this project, all of them have been minted by the community. Each minter paid 0.1174 ETH in Average for minting but it seems they paid 1.79 ETH just for Network fee in Average .')

  #-------------------------------------------------------------------------------------------------
  col1, col2 = st.columns([0.5, 0.5])
  with col1 :
    st.markdown('* **Cumulative of Minters , Mint transactions and NFT minted Hourly**')
    #erea 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/dc5f4907-8bc1-4a88-93f0-2ef4c495d170/data/latest")

    x = response.json()
    y = response.json()
    z = response.json()
    w = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['DATE']) )
      y[i] = ((y[i]['CUM_NFT_MINTED']) )
      z[i] = ((z[i]['CUM_TXHASH']) )
      w[i] = ((w[i]['CUM_MINTERS']) )
    
    option = {
        "title": {
          "text": ''
        },
        "tooltip": {
          "trigger": 'axis',
          "axisPointer": {
            "type": 'cross',
            "label": {
              "backgroundColor": '#6a7985'
            }
          }
        },
        "legend": {
          "data": ['Cum of Minters', 'Cum of Mint transactions','Cum of NFT minted']
        },
        "toolbox": {
          "feature": {
            "saveAsImage": {}
          }
        },
        "grid": {
          "left": '15%',
          "right": '15%',
          "bottom": '15%',
          "containLabel": "true"
        },
        "xAxis": [
          {
            "type": 'category',
            "boundaryGap": "false",
            "data": x
          }
        ],
        "yAxis": [
          {
            "type": 'value'
          }
        ],
        "series": [
        
          {
            "name": 'Cum of Minters',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": y
          },
          {
            "name": 'Cum of Mint transactions',
            "type": 'line',
            "stack": 'Total',
            "label": {
              "show": "true",
              "position": 'top'
            },
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": z
          
          },
          {
            "name": 'Cum of NFT minted',
            "type": 'line',
            "stack": 'Total',
            "label": {
              "show": "true",
              "position": 'top'
            },
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": w
          
          }
        ]
      }
    st_echarts(option)
    
    #-------------------------------------------------------------------------------------------------
    st.markdown('* **Cumulative Mint Price and Fee In ETH**')
    #erea 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/dc5f4907-8bc1-4a88-93f0-2ef4c495d170/data/latest")
    x = response.json()
    y = response.json()
    z = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['DATE']) )
      y[i] = ((y[i]['CUM_FEE']) )
      z[i] = ((z[i]['CUM_ETH']) )
    
    option = {
        "title": {
          "text": ''
        },
        "tooltip": {
          "trigger": 'axis',
          "axisPointer": {
            "type": 'cross',
            "label": {
              "backgroundColor": '#6a7985'
            }
          }
        },
        "legend": {
          "data": ['Cumulative Fee', 'Cumulative Mint Price']
        },
        "toolbox": {
          "feature": {
            "saveAsImage": {}
          }
        },
        "grid": {
          "left": '15%',
          "right": '15%',
          "bottom": '15%',
          "containLabel": "true"
        },
        "xAxis": [
          {
            "type": 'category',
            "boundaryGap": "false",
            "data": x
          }
        ],
        "yAxis": [
          {
            "type": 'value'
          }
        ],
        "series": [
        
          {
            "name": 'Cumulative Fee',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": y
          },
          {
            "name": 'Cumulative Mint Price',
            "type": 'line',
            "stack": 'Total',
            "label": {
              "show": "true",
              "position": 'top'
            },
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": z
          
          }
        ]
      }
    st_echarts(option)
    
      #-------------------------------------------------------------------------------------------------
    st.markdown('* **Cumulative Minters, Mint transactions and NFT minted Hourly**')    
    #erea 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/dc5f4907-8bc1-4a88-93f0-2ef4c495d170/data/latest")
    x = response.json()
    y = response.json()
    z = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['DATE']) )
      y[i] = ((y[i]['NFT_MINTEDS']) )
      z[i] = ((z[i]['CUM_NFT_MINTED']) )
    
    option = {
        "title": {
          "text": ''
        },
        "tooltip": {
          "trigger": 'axis',
          "axisPointer": {
            "type": 'cross',
            "label": {
              "backgroundColor": '#6a7985'
            }
          }
        },
        "legend": {
          "data": ['NFT Minted', 'Cum NFT Minted']
        },
        "toolbox": {
          "feature": {
            "saveAsImage": {}
          }
        },
        "grid": {
          "left": '15%',
          "right": '15%',
          "bottom": '15%',
          "containLabel": "true"
        },
        "xAxis": [
          {
            "type": 'category',
            "boundaryGap": "false",
            "data": x
          }
        ],
        "yAxis": [
          {
            "type": 'value'
          }
        ],
        "series": [
        
          {
            "name": 'NFT Minted',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": y
          },
          {
            "name": 'Cum NFT Minted',
            "type": 'line',
            "stack": 'Total',
            "label": {
              "show": "true",
              "position": 'top'
            },
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": z
          
          }
        ]
        }
    st_echarts(option)
    st.info('* **111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111**')    
  #----------------------------------------------------
    st.markdown('* **Distribution of Number of Mint Transactions per Minter**')    
    #pie - chart left 1
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/e1e3ecd3-e3f4-44d2-9fbd-9a9436f66ee9/data/latest")
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

    st.markdown('* **Distribution of Number of Tokens Minted per Minter**')    
    #pie - chart left 2
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/a7b45f97-e031-472b-978c-e49eb8cca699/data/latest")
    x = response.json()
    option16 = {
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
    st_echarts(option16)
  #----------------------------------------------------

    st.markdown('* **Distribution of USD Paid for Mint per Minters**')    
    #pie - chart left 3 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/cbae09f4-c9cf-4edc-b095-6a2f313a7f80/data/latest")
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
#----------------------------------------------------------------------------------------------

    st.markdown('* **Top 10 Minter based on Transaction Number**')    
    #bar - chart left 1 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/77e4c9f2-c74d-47b8-a449-2d385e8a66b3/data/latest")
    x = response.json()
    y = response.json()
    for i in range (len(x)) :
      x[i] = ((x[i]['MINTER']) )
      y[i] = ((y[i]['transactions']) )

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

#--------------------------------------------------------------------------

    st.markdown('* **Top 10 Minter based on Tokens Number**')    
    #bar - chart left 2 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/60e86b08-b17c-49cd-98f2-25812e55c923/data/latest")
    x = response.json()
    y = response.json()
    for i in range (len(x)) :
      x[i] = ((x[i]['NFT minted']) )
      y[i] = ((y[i]['transactions']) )

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

#--------------------------------------------------------------------------

    st.markdown('* **Top 10 minter based on Transactions Volume In USD**')    
    #bar - chart left 3 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/3ae433b4-8e69-4108-abf7-a1e06a19fa68/data/latest")
    x = response.json()
    y = response.json()
    for i in range (len(x)) :
      x[i] = ((x[i]['MINTER']) )
      y[i] = ((y[i]['USD paid']) )

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


#----------------------------------------------------------------------------------------------

    # full_detailed tablel left 4
    st.markdown('* **Top 10 minter based on Transactions Volume in ETH**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/6fb02099-0e69-4eee-9e60-de97c44d8aa0/data/latest")
    x = response.json()
    def load_data() : 
          return pd.DataFrame(response.json())
    load_data()
    x = load_data()
    x
#----------------------------------------------------------------------------------------------
    # full_detailed tablel left 5
    st.markdown('* **Top 10 minter based on Transactions Fee in ETH**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/8ec6646f-1368-4839-82ed-99037e103446/data/latest")
    x = response.json()
    def load_data() : 
          return pd.DataFrame(response.json())
    load_data()
    x = load_data()
    x
    st.info('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  #----------------------------------------------------------------------------------------------
  #---------------------------------------------------------------------------------------------
  with col2 :
    st.markdown('* **Number of Minters , Mint transactions and NFT minted Hourly**')
    #erea 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/dc5f4907-8bc1-4a88-93f0-2ef4c495d170/data/latest")

    x = response.json()
    y = response.json()
    z = response.json()
    w = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['DATE']) )
      y[i] = ((y[i]['MINTERS']) )
      z[i] = ((z[i]['TXHASH']) )
      w[i] = ((w[i]['NFT_MINTED']) )
    
    option12 = {
        "title": {
          "text": ''
        },
        "tooltip": {
          "trigger": 'axis',
          "axisPointer": {
            "type": 'cross',
            "label": {
              "backgroundColor": '#6a7985'
            }
          }
        },
        "legend": {
          "data": ['# Minters', '# Mint transactions','# NFT minted Hourly']
        },
        "toolbox": {
          "feature": {
            "saveAsImage": {}
          }
        },
        "grid": {
          "left": '15%',
          "right": '15%',
          "bottom": '15%',
          "containLabel": "true"
        },
        "xAxis": [
          {
            "type": 'category',
            "boundaryGap": "false",
            "data": x
          }
        ],
        "yAxis": [
          {
            "type": 'value'
          }
        ],
        "series": [
        
          {
            "name": '# Minters',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": y
          },
          {
            "name": '# Mint transactions',
            "type": 'line',
            "stack": 'Total',
            "label": {
              "show": "true",
              "position": 'top'
            },
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": z
          
          },
          {
            "name": '# NFT minted Hourly',
            "type": 'line',
            "stack": 'Total',
            "label": {
              "show": "true",
              "position": 'top'
            },
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": w
          
          }
        ]
      }
    st_echarts(option12)
    
    #-------------------------------------------------------------------------------------------------
    st.markdown('* **Volume Mint Price and Fee In ETH**')
    #erea 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/dc5f4907-8bc1-4a88-93f0-2ef4c495d170/data/latest")
    x = response.json()
    y = response.json()
    z = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['DATE']) )
      y[i] = ((y[i]['ETH']) )
      z[i] = ((z[i]['FEE']) )
    
    option13 = {
        "title": {
          "text": ''
        },
        "tooltip": {
          "trigger": 'axis',
          "axisPointer": {
            "type": 'cross',
            "label": {
              "backgroundColor": '#6a7985'
            }
          }
        },
        "legend": {
          "data": ['Mint Price Volume in ETH', 'Mint Fee Volume in ETH']
        },
        "toolbox": {
          "feature": {
            "saveAsImage": {}
          }
        },
        "grid": {
          "left": '15%',
          "right": '15%',
          "bottom": '15%',
          "containLabel": "true"
        },
        "xAxis": [
          {
            "type": 'category',
            "boundaryGap": "false",
            "data": x
          }
        ],
        "yAxis": [
          {
            "type": 'value'
          }
        ],
        "series": [
        
          {
            "name": 'Mint Price Volume in ETH',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": y
          },
          {
            "name": 'Mint Fee Volume in ETH',
            "type": 'line',
            "stack": 'Total',
            "label": {
              "show": "true",
              "position": 'top'
            },
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": z
          
          }
        ]
      }
    st_echarts(option13)
    
      #-------------------------------------------------------------------------------------------------
    st.markdown('* **Volume Mint Price In USD & Cumulative volume**')    
    #erea 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/dc5f4907-8bc1-4a88-93f0-2ef4c495d170/data/latest")
    x = response.json()
    y = response.json()
    z = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['DATE']) )
      y[i] = ((y[i]['USD']) )
      z[i] = ((z[i]['CUM_USD']) )
    
    option14 = {
        "title": {
          "text": ''
        },
        "tooltip": {
          "trigger": 'axis',
          "axisPointer": {
            "type": 'cross',
            "label": {
              "backgroundColor": '#6a7985'
            }
          }
        },
        "legend": {
          "data": ['Volume Mint Price In USD', 'Cum volume In USD']
        },
        "toolbox": {
          "feature": {
            "saveAsImage": {}
          }
        },
        "grid": {
          "left": '15%',
          "right": '15%',
          "bottom": '15%',
          "containLabel": "true"
        },
        "xAxis": [
          {
            "type": 'category',
            "boundaryGap": "false",
            "data": x
          }
        ],
        "yAxis": [
          {
            "type": 'value'
          }
        ],
        "series": [
        
          {
            "name": 'Volume Mint Price In USD',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": y
          },
          {
            "name": 'Cum volume In USD',
            "type": 'line',
            "stack": 'Total',
            "label": {
              "show": "true",
              "position": 'top'
            },
            "areaStyle": {},
            "emphasis": {
              "focus": 'series'
            },
            "data": z
          
          }
        ]
        }
    st_echarts(option14) 
    st.info('* **111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111**')    
#----------------------------------------------------

    st.markdown('* **Distribution of ETH Paid for Mint Per Minters**')    
    #pie - chart right 1 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/df4d0a62-b518-4f8b-a942-2d6b8ec86d56/data/latest")
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

    st.markdown('* **Distribution of ETH Paid for Fee per Minters**')    
    #pie - chart right 2
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/212db31f-76ab-4355-b0a9-4eadb0bf621c/data/latest")
    x = response.json()
    option18 = {
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
    st_echarts(option18)
    st.info("sssssssssssssssssssssssssssssssssssssssddddddddddddddddsddddsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddsddddsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddddddddddddddddsddddsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddddddddddddddddsddddsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
#----------------------------------------------------------------------------------------------

    st.markdown('* **Top 10 minter based on Transactions Volume in ETH**')    
    #bar - chart right 4
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/6fb02099-0e69-4eee-9e60-de97c44d8aa0/data/latest")
    x = response.json()
    y = response.json()
    for i in range (len(x)) :
      x[i] = ((x[i]['MINTER']) )
      y[i] = ((y[i]['ETH paid']) )

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
#--------------------------------------------------------------------------

    st.markdown('* **Top 10 minter based on Transactions Fee in ETH**')    
    #bar - chart right 5 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/8ec6646f-1368-4839-82ed-99037e103446/data/latest")
    x = response.json()
    y = response.json()
    for i in range (len(x)) :
      x[i] = ((x[i]['MINTER']) )
      y[i] = ((y[i]['FEE paid in ETH']) )

    option25 = {
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
    st_echarts( option25)
    st.info("sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")


    # full_detailed tablel right 1
    st.markdown('* **Top 10 Minter based on Transaction Number**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/77e4c9f2-c74d-47b8-a449-2d385e8a66b3/data/latest")
    x = response.json()
    def load_data() : 
          return pd.DataFrame(response.json())
    load_data()
    x = load_data()
    x
#----------------------------------------------------------------------------------------------
    # full_detailed tablel right 2
    
    st.markdown('* **Top 10 minter based on Tokens Number**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/60e86b08-b17c-49cd-98f2-25812e55c923/data/latest")
    x = response.json()
    def load_data() : 
          return pd.DataFrame(response.json())
    load_data()
    x = load_data()
    x
#----------------------------------------------------------------------------------------------
    # full_detailed tablel right 3
    st.markdown('* **Top 10 minter based on Transactions Volume In USD**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/3ae433b4-8e69-4108-abf7-a1e06a19fa68/data/latest")
    x = response.json()
    def load_data() : 
          return pd.DataFrame(response.json())
    load_data()
    x = load_data()
    x
#--------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

with tab2 :
  
  st.title("It's summer!")

  
