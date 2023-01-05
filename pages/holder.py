import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
import base64


st.set_page_config(layout="wide")


#-------------------------------------------------------------------------------------------------
# header  

st.header("")
tab1 , tab2  = st.tabs(
    [
        "💲 Holder", 
        'Doodlebank'
        
    ]
)

#-------------------------------------------------------------------------------------------------


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
# background color 
st.markdown("""<style>.main {background-color: #C8D3E0;}</style>""",unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------


with tab1 :
    # general metrics  #hold 

        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/efd9fab6-99de-451c-97c5-d23efb396371/data/latest")
        x = response.json()

        for i in range (len(x)) :
            x[i] = ((x[i]['AVG(NFTS)']) )

        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/c062ecff-563d-498c-8e55-3e04b0af6d2a/data/latest")
        y = response.json()

        for i in range (len(x)) :
            y[i] = ((y[i]['COUNT(DISTINCT WALLETS)']) )


        with open('model1.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        col111, col112,col113, col114   = st.columns([0.5, 0.5,0.5, 0.5])
        with col111 : 
            st .image("https://pbs.twimg.com/media/FElf1zRXsAwlVBx?format=png&name=large")
        with col112 : 
            st .metric("Average NFT Holded", x[0])
        with col113 :
            st.metric("Number of Holders", y[0])
        with col114 : 
            st .image("https://blog.mexc.com/wp-content/uploads/2022/08/Doodles-NFT-1.png")
        
        
        col1, col2 = st.columns([1.25, 0.75])
        with col1 :

        # erea- chart 3
            st.markdown('* **Number of NFT owners**')
        
            response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/e83c756a-42c3-4e92-bd84-de868bd95279/data/latest")

            x = response.json()
            y = response.json()

            for i in range (len(x)) :
                x[i] = ((x[i]['DAY']) )
                y[i] = ((y[i]['TOTAL_OWNERS']) )


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
                    "data": ['Number of NFT owners']
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
                    "name": 'Number of NFT owners',
                    "type": 'line',
                    "stack": 'Total',
                    "areaStyle": {},
                    "emphasis": {
                        "focus": 'series'
                    },
                    "data": y
                    }
                ]
                }
            st_echarts(option14)



        with col2 : 
            #-------------------------------------------------------------------------------------------------
            # pie chart 

            st.markdown('* **Number of Holders based on Theirs NFT**')
            response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/a7b45f97-e031-472b-978c-e49eb8cca699/data/latest")
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




        st.markdown('* **Doodles Holders**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/a1c4c1d4-fc10-4a3f-beea-d9f084d3dd39/data/latest")
        x = response.json()

        def load_data() : 
            return pd.DataFrame(response.json())
        x = load_data()
        x

        # general metrics  #hold 

        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/a80e00cf-b183-422e-818f-45dc54371ce8/data/latest")
        x = response.json()

        for i in range (len(x)) :
            x[i] = ((x[i]['average hold time for traders in day']) )

        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/f2ad5e88-9406-4261-9474-fec665d8d2a0/data/latest")
        y = response.json()

        for i in range (len(x)) :
            y[i] = ((y[i]['average hold time for traders in day']) )


        col114, col115,col116, col117  = st.columns([0.5, 0.5,0.5, 0.5])
        with col114 : 
            st .image("https://pbs.twimg.com/media/FElf1zRXsAwlVBx?format=png&name=large")
        with col115 : 
            st .metric("Average Hold Time for Traders in day", y[0])
        with col116 :
            st.metric("Average Hold Time for Minters in day", x[0])
        with col117 : 
            st .image("https://blog.mexc.com/wp-content/uploads/2022/08/Doodles-NFT-1.png")
      
        col7, col77  = st.columns([0.5, 0.5])
        with col7 : 
            st.markdown('In this part, we want to find the Average Holding period of this NFT collection by its holders')
            st.markdown('In the charts below , the holding Period of this NFT collection was shown and is categorized by the holding time for those who bought this NFT and sold it  . (bought ->sell period )')
        with col77 : 
            st.markdown('we want to find the Average Holding period of this NFT collection by its holders')
            st.markdown('In the charts below , the holding Period of this NFT collection was shown and is categorized by the holding time for those who minted this NFT and sold it first . (mint ->first sell period )')

        col71, col78  = st.columns([0.5, 0.5])
        with col71 : 
            #-------------------------------------------------------------------------------------------------
            # pie chart 

            st.info('* **Number of Traders based on Average Trade Time**')
            st.markdown('* from buy time to sell time')
            response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/72d9b7ee-5900-410f-a101-ccc50f9c4b20/data/latest")
            x = response.json()

            bar_options1 = {
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
            st_echarts(bar_options1)            
        with col78 : 
            #-------------------------------------------------------------------------------------------------
            # pie chart 

            st.info('* **Number of Minters based on Average Trade Time**')
            st.markdown('* from mint till first sale')

            response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/00514343-0d86-453c-ae31-7c540e3bc6eb/data/latest")
            x = response.json()

            bar_options2 = {
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
            st_echarts(bar_options2)           
    
        col72, col73  = st.columns([0.5, 0.5])
        with col72 : 
            st.markdown('Here The two tables below show the shortest holding time of NFTs based on minutes And the longest holding time of NFTs is shown by day   for Traders')
        with col73 : 
            st.markdown('Here The two tables below show the shortest holding time of NFTs based on minutes And the longest holding time of NFTs is shown by day   for Minters')
        col75, col70  = st.columns([0.5, 0.5])
        with col75 : 
              #table 
            st.markdown('* **Quickest sale period -- Min Holding Time in minute**')
            response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/f43f1ee0-f095-492e-9dc1-047ac68530eb/data/latest")
            x = response.json()

            def load_data() : 
                return pd.DataFrame(response.json())
            x = load_data()
            x



        #table 

            st.markdown('* **Longest sale period-- Max Holding Time in day**')
            response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/62e6ac52-157d-43e2-b592-9c2a13b4bf10/data/latest")
            y = response.json()

            def load_data() : 
                return pd.DataFrame(response.json())
            y = load_data()
            y

        with col70 : 
              #table 
            st.markdown('* **Quickest Hold period (Minters) -- Min Holding Time in minute**')
            response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/a3f96ef5-f4ba-4cb2-bf5c-995c5d1a82b0/data/latest")
            z = response.json()

            def load_data() : 
                return pd.DataFrame(response.json())
            z = load_data()
            z



        #table 

            st.markdown('* **Longest Minter period -- Max Holding Time in day**')
            response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/7c2d72b7-1b89-49fc-a54b-c4aa8aa4563b/data/latest")
            e = response.json()

            def load_data() : 
                return pd.DataFrame(response.json())
            e = load_data()
            e

with tab2 :

    col50, col52  = st.columns([0.5, 0.5])
    with col50 : 
        st.markdown('**What is Treasury wallet?**')
        st.markdown('A treasury system is a community controlled and decentral- ized collaborative decision-making mechanism for sustainable funding of the blockchain development and maintenance. During each treasury period, project proposals are submitted, discussed, and voted for; top- ranked projects are funded from the treasury.')
        st.markdown('**Doodlebank**')
        st.markdown('is the treasury section for the Doodles community, which holds more than 650 ETH. There is a community structure for voting, and each Doodle equals one vote when it comes to voting matters that relate to treasury funding projects.')

        # erea- chart 3
        st.markdown('* **Creator Fee in ETH and Cumulative amount**')
    
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/ad9f41d8-5a94-4753-8e06-49a778474b59/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()

        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['CREATOR_FEES']) )
            z[i] = ((z[i]['cum CREATOR FEE ETH']) )


        option39 = {
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
            "data": ['Creator Fee (ETH)', 'Cum Creator Fee (ETH)']
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
              "name": 'Creator Fee (ETH)',
              "type": 'line',
              "stack": 'Total',
              "areaStyle": {},
              "emphasis": {
                "focus": 'series'
              },
              "data": y
            },
            {
              "name": 'Cum Creator Fee (ETH)',
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
        st_echarts(option39)





        # erea- chart 3
        st.markdown('* **Treasury Wallet Value in USD**')
    
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/46fe1f3a-fbf1-4b85-ab26-c48f40e91217/data/latest")

        x = response.json()
        y = response.json()

        for i in range (len(x)) :
            x[i] = ((x[i]['BALANCE_DATE']) )
            y[i] = ((y[i]['USD']) )


        option73 = {
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
            "data": ['Treasury Value (USD)']
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
            }
          ]
          }
        st_echarts(option73)

        #--------------------------------------------------------------------------
    with col52 : 
        st.markdown('**Creator fees**')
        st.markdown(' Creators can set a collection-level fee of up to 10%. This means creators can earn every time their NFT is sold . The creator can modify this fee percentage at any time and will receive creator earnings in real time. To learn how to set your creator earnings, you can read through our help center guide How do creator earnings work on OpenSea?')
        st.markdown('**Splitting creator fees**')
        st.markdown(' If you are creating a collection on behalf of someone or as part of a group, you can set up multiple payout addresses and specify the creator earnings per wallet in order to automatically split creator earnings.Each payout address added will count as a separate transaction, which can increase the gas prices your buyers pay.')

         # erea- chart 3
        st.markdown('* **Creator Fee in USD and Cumulative amount**')
    
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/ad9f41d8-5a94-4753-8e06-49a778474b59/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()

        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['CREATOR_FEE_USDS']) )
            z[i] = ((z[i]['cum CREATOR FEE USD']) )


        option399 = {
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
            "data": ['Creator Fee (USD)', 'Cum Creator Fee (USD)']
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
              "name": 'Creator Fee (USD)',
              "type": 'line',
              "stack": 'Total',
              "areaStyle": {},
              "emphasis": {
                "focus": 'series'
              },
              "data": y
            },
            {
              "name": 'Cum Creator Fee (USD)',
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
        st_echarts(option399)





        # erea- chart 3
        st.markdown('* **Treasury Wallet Value in ETH**')
    
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/9997be96-b55d-4cab-a8b3-7b8f81b45335/data/latest")

        x = response.json()
        y = response.json()

        for i in range (len(x)) :
            x[i] = ((x[i]['BALANCE_DATE']) )
            y[i] = ((y[i]['ETH']) )


        option733 = {
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
            "data": ['Treasury Value (ETH)']
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
            }
          ]
          }
        st_echarts(option733)
