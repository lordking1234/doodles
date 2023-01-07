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
# header  

st.header("")
tab1, tab2, tab3 = st.tabs(
    [
        "📊 General Metrics",
        "Full detialed Table",
        "💡About Snapshot",
    ]
)


#-------------------------------------------------------------------------------------------------
# background color 
st.markdown("""<style>.main {background-color: #C8D3E0;color:#010101}</style>""",unsafe_allow_html=True)


# background pucture  
#@st.experimental_memo
#def get_img_as_base64(file):
#    with open(file, "rb") as f:
#        data = f.read()
#    return base64.b64encode(data).decode()



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
with tab1 :


  st.title("Doodles & Snapshot")
  st.image("https://media.discordapp.net/attachments/906600867698991105/1054035614095388702/02285da3-9816-460a-b264-db388c46d238.png?width=837&height=837")    
  st.header("Community Voting")  
  st.markdown("The entire Doodles ecosystem is basically one DAO, and each and every Doodles owner has a say in what that DAO does. Early on, Keast laid out how the DoodleDAO treasury would work, stating that 1 Doodle = 1 Vote towards any and all decisions regarding the DoodleBank.")
  st.markdown("So far, Doodles members have been able to vote on proposals for Doodles team scaling, Doodles live events, funding a 3D Doodles project, and much more. The Doodles Forum and Doodles Discord allow an extra level of discourse to take place for each proposal. ")


  #-------------------------------------------------------------------------------------------------
  # general metrics  
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/1ee36154-ff5d-41ef-82ac-2aca716b553d/data/latest")
  x = response.json()
  y = response.json()
  z = response.json()
  w = response.json()

  for i in range (len(x)) :
   x[i] = ((x[i]['TRANSACTIONS']) )
   y[i] = ((y[i]['PROPOSAL_IDS']) )
   z[i] = ((z[i]['VOTERS']) )
   w[i] = ((w[i]['PROPOSAL_AUTHORS']) )

  with open('model1.css') as f:
      st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

  col1, col2, col3,col4 = st.columns([0.5, 0.5, 0.5, 0.5])
  col1.metric("Number Of Total Vote", x[0])
  col2.metric("Number of Total Proposals", y[0])
  col3.metric("Number Of Total Voters", z[0])
  col4.metric("Number Of Total Authors", w[0])

  col12, col13 = st.columns (2)
  col12.info('')
  col13.info('')
  #-------------------------------------------------------------------------------------------------

  col12, col13 = st.columns ([2,0.5])
  with col12  :
    st.markdown('* **New and Total Voters**')
    #erea 
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/bb30a268-3b61-434e-abb1-9db32aed64f8/data/latest")

    x = response.json()
    y = response.json()
    z = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['FIRST_VOTE']) )
      y[i] = ((y[i]['DAILY_NEW_VOTER']) )
      z[i] = ((z[i]['TOTAL_NEW_VOTER']) )


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
            "data": ['Total Voters', 'Daily New Voters']
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
              "name": 'Daily New Voters',
              "type": 'line',
              "stack": 'Total',
              "areaStyle": {},
              "emphasis": {
                "focus": 'series'
              },
              "data": y
            },
            {
              "name": 'Total Voters',
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
    st_echarts( option)

  with col13  :
    st.info('')

  #-------------------------------------------------------------------------------------------------
  # erea-chart 1

  col12, col13 = st.columns (2)
  with col12  :
    st.markdown('* **Proposals based on # Voters**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/81a9de08-ccc5-4440-886b-5c29ad44616a/data/latest")

    x = response.json()
    y = response.json()
    z = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['PROPOSAL_START_TIME']) )
      y[i] = ((y[i]['VOTERS']) )
      z[i] = ((z[i]['POPULARITY']) )


    option2 = {
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
            "data": ['Voters', 'Popularity']
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
              "name": 'Voters',
              "type": 'line',
              "stack": 'Total',
              "areaStyle": {},
              "emphasis": {
                "focus": 'series'
              },
              "data": y
            },
            {
              "name": 'Popularity',
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
    st_echarts(option2)
    st.image('https://www.psyop.com/wp-content/uploads/2022/07/doodles-4.gif')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')



  # erea-chart 2
  
  with col13  : 
    st.markdown('* **Proposals based on # Votes**')
  
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/81a9de08-ccc5-4440-886b-5c29ad44616a/data/latest")

    x = response.json()
    y = response.json()
    z = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['PROPOSAL_START_TIME']) )
      y[i] = ((y[i]['VOTE']) )
      z[i] = ((z[i]['POPULARITY']) )


    option1 = {
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
            "data": ['Votes', 'Popularity']
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
              "name": 'Votes',
              "type": 'line',
              "stack": 'Total',
              "areaStyle": {},
              "emphasis": {
                "focus": 'series'
              },
              "data": y
            },
            {
              "name": 'Popularity',
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
    st_echarts(option1)

    # erea- chart 3
    st.markdown('* **Proposals based on Voting Ratio**')
  
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/81a9de08-ccc5-4440-886b-5c29ad44616a/data/latest")

    x = response.json()
    y = response.json()
    z = response.json()

    for i in range (len(x)) :
      x[i] = ((x[i]['PROPOSAL_START_TIME']) )
      y[i] = ((y[i]['VOTING_POWERS_RATIO']) )
      z[i] = ((z[i]['VOTING_POWERS']) )


    option3 = {
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
            "data": ['Voting Pow Ratio', 'Voting Pow']
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
              "name": 'Voting Pow Ratio',
              "type": 'line',
              "stack": 'Total',
              "areaStyle": {},
              "emphasis": {
                "focus": 'series'
              },
              "data": y
            },
            {
              "name": 'Voting Pow',
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
    st_echarts(option3)
  #-------------------------------------------------------------------------------------------------
  # pie chart 

  col12, col13 = st.columns (2)
  with col12  :
    st.markdown('* **Distribution of Voters based on # Votes**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/165032d4-9ea9-44c4-92bd-278d1bb5b501/data/latest")
    x = response.json()

    bar_options = {
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
                  "shadowBlur": '10',
                  "shadowOffsetX": '0',
                  "shadowColor": 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
          }
    st_echarts(bar_options)

  #-------------------------------------------------------------------------------------------------
  #table 
  with col13  :
    st.markdown('* **Top Voters over Time**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/8fa8dde0-15e9-4447-b784-2912937bb80d/data/latest")
    x = response.json()

    def load_data() : 
        return pd.DataFrame(response.json())
    x = load_data()
    x

  #-------------------------------------------------------------------------------------------------
  col12, col13 = st.columns (2)
  with col12  : 
      st.markdown("")
  with col13  : 
      st.info("")

  #-------------------------------------------------------------------------------------------------
  # bar chart 

  with col12  :
    st.markdown('* **Proposals Based on Voting Period**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/f7e1589c-5285-4222-a423-909ebc2355d6/data/latest")
    x = response.json()
    y = response.json()


    for i in range (len(x)) :
      x[i] = ((x[i]['DIF']) )
      y[i] = ((y[i]['PROPOSALS']) )


    option = {
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
                  {"value":y[0], "itemStyle":{"color":"#0000FF"}}, 
                  {"value":y[1], "itemStyle":{"color":"#00FFFF"}},

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
    st_echarts( option)

  with col13  : 
    st.markdown("")


  st.markdown('* **Full detailed Table**')
  response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/8fa8dde0-15e9-4447-b784-2912937bb80d/data/latest")
  x = response.json()
  y = response.json()

  for i in range (len(x)) :
    x[i] = ((x[i]['VOTER']) )
    y[i] = ((y[i]['VOTE']) )




  bar_options =  {
    "dataset": {
      "source": [
        ['score', 'amount', 'product'],
        [89.3, y[0], x[0]],
        [57.1, y[1], x[1]],
        [74.4, y[2], x[2]],
        [50.1, y[3], x[3]],
        [89.7, y[4], x[4]],
        [68.1, y[5], x[5]],
        [19.6, y[6], x[6]],
        [10.6, y[7], x[7]],
        [32.7, y[8], x[8]],
        [10.6, y[9], x[9]]

      ]
    },
    "grid": { "containLabel": "true" },
    "xAxis": { "name": 'amount' },
    "yAxis": { "type": 'category' },
    "visualMap": {
      "orient": 'horizontal',
      "left": 'center',
      "min": 10,
      "max": 100,
      "text": ['High Score', 'Low Score'],
      # Map the score column to color
      "dimension": 0,
      "inRange": {
        "color": ['#65B581', '#FFCE34', '#FD665F']
      }
    },
    "series": [
      {
        "type": 'bar',
        "encode": {
          # Map the "amount" column to X axis.
          "x": 'amount',
          # Map the "product" column to Y axis
          "y": 'product'
        }
      }
    ]
  }
  st_echarts(bar_options)

  
  
  
  
  #-------------------------------------------------------------------------------------------------
  # full_detailed tablel
with tab2 :
    st.markdown('* **Top Voters over Time**')
    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/8feecb1d-4b13-42e3-bb6c-c23c92bf84ad/data/latest")
    x = response.json()
    def load_data() : 
          return pd.DataFrame(response.json())
    load_data()
    x = load_data()
    x

#-------------------------------------------------------------------------------------------------
with tab3 :
    st.image("https://img.decrypt.co/insecure/rs:fit:1536:0:0:0/plain/https://cdn.decrypt.co/wp-content/uploads/2021/06/image0-1-gID_5-pID_2.png@webp")    
    st.subheader("What is Snapshot?  The Decentralized Voting System")
    st.markdown("""Snapshot is a voting tool based on the IPFS decentralized storage system, used by many crypto projects to poll their user bases""")
    st.info("In brief Snapshot is a decentralized voting system.It's used by several companies in the DeFi space to help survey users.The project uses 'off-chain' signing techniques to make voting fee less.")
    st.markdown("Snapshot is a place where projects can create proposals for people to vote on using cryptocurrency. In the industry, this process is called ‘vote signaling’. Traditionally, to vote using cryptocurrency would normally incur fees to process the movement of currency from one wallet to another. ")
    st.markdown("But on Snapshot, that doesn’t happen, thanks to the clever use of the decentralized storage network called IPFS. Because Snapshot doesn’t use ‘on-chain’ verification, any votes are essentially fee-less.  ")
    st.info("Did you know?     There are more than 1,000 project proposals on Snapshot.")
    st.markdown("It’s a popular tool for decentralized organizations (DAOs) looking to query what their audiences think using blockchain technology. ")
    st.subheader("How do you use Snapshot? ")
    st.markdown("For companies looking to use Snapshot, they need to have an existing profile on the Ethereal Naming Service, or ENS. Once they have that, they then add a record on ENS to allow votes to be viewable at that address. ")
    st.markdown("Users, meanwhile, need a wallet address with the required cryptocurrency in order to take part in a poll. On Decrypt’s Snapshot page, for example, users holding one of our NFTs in a wallet like MetaMask would be eligible to vote. ")
    st.subheader("What makes Snapshot so special?")
    st.markdown("Users simply connect their wallet to Snapshot's website and it will allow a vote to be cast on any open proposals on the site.")
    st.markdown("Cryptocurrency projects traditionally have to create the infrastructure themselves to conduct this sort of polling or use other methods that aren’t decentralized. These methods are both time-consuming and can be taken over by parties who may not have the project’s best interests at heart to skew the votes. ")
    
    col12, col13 = st.columns (2)
    with col12 :
        st.markdown("Where Snapshot differs is that it allows projects to seek out their most committed members who hold their chosen cryptocurrency and ask them to make decisions. It does this by not sending the transactions to a blockchain.  Instead, it uses the IPFS network (read here to learn more about IPFS) to create and store the votes. This allows Snapshot to use a blockchain to register how people reacted to a poll, without incurring the usual fees. ")
    with col13 :
        st.image("https://352593183-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/spaces%2F-MG4Ulnnabb2Xz3Lei9_%2Favatar-1602311890000.png?generation=1602311890284612&alt=media")
    
    col12, col13 = st.columns (2)
    with col12  :
        st.empty()
        st.markdown("Reference : [[decrypt Website]](https://decrypt.co/resources/what-is-snapshot-the-decentralized-voting-system)")
        st.markdown("Reference : [[Snapshot Website]](https://snapshot.org/#/)")
        st.markdown("Reference : [[Snapshot Doodles]](https://snapshot.org/#/doodles.eth)")
    with col13 :
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeCkE_SoRHS2KfufYt8OTsRWvh7rpo-a9DKhfABCWCPSLxYfnUjo7KM0eACIhCHN-CrKg&usqp=CAU")

  #-------------------------------------------------------------------------------------------------




