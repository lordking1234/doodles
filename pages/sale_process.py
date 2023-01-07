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
        "💲 Sale Process",
        "💡 About Sale"
        
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
    # general metrics  #sale  process 

    response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/a9bef9b3-7108-4719-ad14-64b012aa97b8/data/latest")

    x = response.json()
    y = response.json()
    z = response.json()
    w = response.json()
    c = response.json()
    b = response.json()
    v = response.json()
    n = response.json()
    m = response.json()
    g = response.json()
    r = response.json()
    t = response.json()
    u = response.json()
    o = response.json()


    for i in range (len(x)) :
        x[i] = ((x[i]['seller']) )
        y[i] = ((y[i]['buyer']) )
        z[i] = ((z[i]['Number of TOKENID']) )
        w[i] = ((w[i]['sale_txs']) )
        c[i] = ((c[i]['volumes']) )
        b[i] = ((b[i]['PRICE_USDS']) )
        v[i] = ((v[i]['TOTAL_FEESS']) )
        n[i] = ((n[i]['PLATFORM_FEES']) )
        m[i] = ((m[i]['CREATOR_FEES']) )
        g[i] = ((g[i]['TOTAL_FEES_USDS']) )
        r[i] = ((r[i]['PLATFORM_FEE_USDS']) )
        t[i] = ((t[i]['CREATOR_FEE_USDS']) )
        u[i] = ((u[i]['TX_FEES']) )
        o[i] = ((o[i]['TX_FEE_USDS']) )

    with open('model1.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    col111, col112 ,col113, col114 = st.columns([0.5, 0.5,0.5, 0.5])
    with col111 : 
        st .metric("Number Of Total Sellers", x[0])
    with col112 :
        st.metric("Number of Total Buyers", y[0])
    with col113 :
        st.metric("Number of NFT sold", z[0]) 
    with col114 :
        st.metric("Number of sales transactions", w[0]) 

    col12, col13 = st.columns (2)
    with col12 :
        st.info('')
    with col13 :
        st.info('')

    col21, col22, col23,col24 = st.columns([0.5, 0.5, 0.5, 0.5])
    with col21 :
        st.metric("Volume of sale's transactions in ETH", c[0])
    with col22 :
        st.metric("Volume of sale's transactions in USD", b[0]) 
    with col23 :
        st.metric("Volume of Total Fee in ETH", v[0])
    with col24 :
        st.metric("Volume of Platform's Fee in ETH", n[0])

    col31, col32,col33,col34 = st.columns([0.5, 0.5,0.5, 0.5])
    with col31 :
        st.metric("Volume of Creator's Fee in ETH", m[0])
    with col32 : 
        st.image("https://ipfs.moralis.io:2053/ipfs/QmNu7RMnE5x6zMgBL5Xux8faQFCKNAYArtHwPnu4nV6Xti")
        #st.markdown("...................")
    with col33 : 
        st.image("https://pbs.twimg.com/media/FMvgnYWakAI_Qya.jpg")
        # st.markdown("...................")
    with col34 : 
        st.metric("Volume of Total Fee in USD", g[0])

    col41, col42, col43,col44 = st.columns([0.5, 0.5, 0.5, 0.5])
    with col41 :
        st.metric("Volume of Platform's Fee in USD", r[0])
    with col42 :
        st.metric("Volume of Creator's Fee in USD", t[0])
    with col43 :
        st.metric("Volume of Network's Fee in ETH", u[0]) 
    with col44 :
        st.metric("Volume of Network's Fee in USD", o[0]) 

    col53,col54 = st.columns([0.5, 0.5])
    with col53 :
        st.info("") 
    with col54 :
        st.info("") 


    col182, col183 = st.columns ([1,1])
    with col182 :

        st.markdown('* **Total different Fees in ETH (Network + Creator + Platform = Total )**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63331be5-f751-43bb-b6c2-7956893136eb/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()
        w = response.json()
        g = response.json()

        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['TX_FEES']) )
            z[i] = ((z[i]['CREATOR_FEES']) )
            w[i] = ((w[i]['PLATFORM_FEES']) )
            g[i] = ((g[i]['TOTAL_FEESS']) )


        option21 = {
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
            "data": ['Transaction Fee (ETH)', 'Creator Fee (ETH)','Platform Fee (ETH)','Total Fee (ETH)']
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
            "name": 'Transaction Fee (ETH)',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
            "focus": 'series'
            },
            "data": y
            },
            {
            "name": 'Creator Fee (ETH)',
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
            "name": 'Platform Fee (ETH)',
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
            },
            {
            "name": 'Total Fee (ETH)',
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
            "data": g
            }              
            ]
            }
        st_echarts(option21)





        st.markdown('* **Cumulative & daily Number of Buyers**')
        st.markdown('')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63331be5-f751-43bb-b6c2-7956893136eb/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()


        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['buyer']) )
            z[i] = ((z[i]['cum buyer']) )
 


        option30 = {
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
            "data": ['Daily Number of Buyers', 'Cum Number of Buyers']
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
            "name": 'Daily Number of Buyers',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
            "focus": 'series'
            },
            "data": y
            },
            {
            "name": 'Cum Number of Buyers',
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
        st_echarts(option30)


        st.markdown('* **Cumulative & daily Number of Sellers**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63331be5-f751-43bb-b6c2-7956893136eb/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()


        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['seller']) )
            z[i] = ((z[i]['cum sellers']) )
 


        option31 = {
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
            "data": ['Daily Number of seller', 'Cum Number of seller']
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
            "name": 'Daily Number of seller',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
            "focus": 'series'
            },
            "data": y
            },
            {
            "name": 'Cum Number of seller',
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
        st_echarts(option31)



        st.markdown('')
        st.markdown('* **Cumulative & daily Volume of Transaction in USD**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63331be5-f751-43bb-b6c2-7956893136eb/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()


        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['PRICE_USDS']) )
            z[i] = ((z[i]['cum PRICE_USDs']) )
 


        option24 = {
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
            "data": ['Daily Volume of Transaction (USD)', 'Cum Volume of Transaction (USD)']
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
            "name": 'Daily Volume of Transaction (USD)',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
            "focus": 'series'
            },
            "data": y
            },
            {
            "name": 'Cum Volume of Transaction (USD)',
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
        st_echarts(option24)

        #-------------------------------------------------------------------------------------------------
        #Platforms with most number of buyers
        # pie chart 

        st.markdown('* **Platforms with most number of buyers**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/dac2b82c-7034-4068-895f-8d1f360a12ef/data/latest")
        x = response.json()

        option = {
            "tooltip": {
            "trigger": 'item'
            },
            "legend": {
            "top": '5%',
            "left": 'center'
            },
            "series": [
            {
            "name": 'Buyers',
            "type": 'pie',
            "radius": ['40%', '70%'],
            "avoidLabelOverlap": "false",
            "itemStyle": {
            "borderRadius": "10",
            "borderColor": '#fff',
            "borderWidth": "2"
            },
            "label": {
            "show": "false",
            "position": 'center'
            },
            "emphasis": {
            "label": {
            "show": "true",
            "fontSize": '20',
            "fontWeight": 'bold'
            }
            },
            "labelLine": {
            "show": "true"
            },
            "data": x

            }
            ]
            }
        st_echarts(option)

#-------------------------------------------------------------------------------------------------
        #Platforms with most volume of transactions in ETH
        # pie chart 

        st.markdown('* **Platforms with most volume of transactions in ETH**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/5ecdf5cf-34b8-4512-af55-a78906997ff3/data/latest")
        x = response.json()

        option = {
            "tooltip": {
            "trigger": 'item'
            },
            "legend": {
            "top": '0%',
            "left": 'center'
            },
            "series": [
            {
            "name": 'ETH',
            "type": 'pie',
            "radius": ['40%', '75%'],
            "avoidLabelOverlap": "false",
            "itemStyle": {
            "borderRadius": "10",
            "borderColor": '#fff',
            "borderWidth": "2"
            },
            "label": {
            "show": "false",
            "position": 'center'
            },
            "emphasis": {
            "label": {
            "show": "true",
            "fontSize": '20',
            "fontWeight": 'bold'
            }
            },
            "labelLine": {
            "show": "true"
            },
            "data": x

            }
            ]
            }
        st_echarts(option)

        st.info('')
    #-------------------------------------------------------------------------------------------------
    with col183 :


 

        st.markdown('* **Total different Fees in USD (Network + Creator + Platform = Total )**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63331be5-f751-43bb-b6c2-7956893136eb/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()
        w = response.json()
        g = response.json()

        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['TX_FEE_USDS']) )
            z[i] = ((z[i]['CREATOR_FEE_USDS']) )
            w[i] = ((w[i]['PLATFORM_FEE_USDS']) )
            g[i] = ((g[i]['TOTAL_FEES_USDS']) )


        option22 = {
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
            "data": ['Transaction Fee (USD)', 'Creator Fee (USD)','Platform Fee (USD)','Total Fee (USD)']
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
            "name": 'Transaction Fee (USD)',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
            "focus": 'series'
            },
            "data": y
            },
            {
            "name": 'Creator Fee (USD)',
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
            "name": 'Platform Fee (USD)',
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
            },
            {
            "name": 'Total Fee (USD)',
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
            "data": g
            }              
            ]
            }
        st_echarts(option22)



        st.markdown('* **Cumulative & daily Number of Transaction**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63331be5-f751-43bb-b6c2-7956893136eb/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()


        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['sale_txs']) )
            z[i] = ((z[i]['cum sale_txs']) )
 


        option25 = {
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
            "data": ['Daily Number of Transaction', 'Cum Number of Transaction']
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
            "name": 'Daily Number of Transaction',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
            "focus": 'series'
            },
            "data": y
            },
            {
            "name": 'Cum Number of Transaction',
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
        st_echarts(option25)




        st.markdown('* **daily Number of Sellers & buyer**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63331be5-f751-43bb-b6c2-7956893136eb/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()


        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['seller']) )
            z[i] = ((z[i]['buyer']) )
 


        option33 = {
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
            "data": ['Daily Number of seller', 'Daily Number of Buyers']
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
            "name": 'Daily Number of seller',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
            "focus": 'series'
            },
            "data": y
            },
            {
            "name": 'Daily Number of Buyers',
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
        st_echarts(option33)


        st.markdown('* **Cumulative & daily Volume of Transaction in ETH**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/63331be5-f751-43bb-b6c2-7956893136eb/data/latest")

        x = response.json()
        y = response.json()
        z = response.json()


        for i in range (len(x)) :
            x[i] = ((x[i]['DATE']) )
            y[i] = ((y[i]['volumes']) )
            z[i] = ((z[i]['cum volumes']) )
 


        option23 = {
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
            "data": ['Daily Volume of Transaction (ETH)', 'Cum Volume of Transaction (ETH)']
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
            "name": 'Daily Volume of Transaction (ETH)',
            "type": 'line',
            "stack": 'Total',
            "areaStyle": {},
            "emphasis": {
            "focus": 'series'
            },
            "data": y
            },
            {
            "name": 'Cum Volume of Transaction (ETH)',
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
        st_echarts(option23)



   #-------------------------------------------------------------------------------------------------
        #Platforms with most number of sellers
        # pie chart 
        ##
        st.markdown('* **Platforms with most number of sellers**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/674171c9-90db-4978-ba8c-c9adfe59e829/data/latest")
        x = response.json()

        option = {
            "tooltip": {
            "trigger": 'item'
            },
            "legend": {
            "top": '5%',
            "left": 'center'
            },
            "series": [
            {
            "name": 'Sellers',
            "type": 'pie',
            "radius": ['40%', '75%'],
            "avoidLabelOverlap": "false",
            "itemStyle": {
            "borderRadius": "10",
            "borderColor": '#fff',
            "borderWidth": "2"
            },
            "label": {
            "show": "false",
            "position": 'center'
            },
            "emphasis": {
            "label": {
            "show": "true",
            "fontSize": '20',
            "fontWeight": 'bold'
            }
            },
            "labelLine": {
            "show": "true"
            },
            "data": x

            }
            ]
            }
        st_echarts(option)


    #Platforms with most volume of transactions in USD
    # pie chart 

        st.markdown('* **Platforms with most volume of transactions in USD**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/3cd4da83-6335-482b-9b80-6a04801571fc/data/latest")
        x = response.json()

        option = {
            "tooltip": {
            "trigger": 'item'
            },
            "legend": {
            "top": '5%',
            "left": 'center'
            },
            "series": [
            {
            "name": 'USD',
            "type": 'pie',
            "radius": ['40%', '75%'],
            "avoidLabelOverlap": "false",
            "itemStyle": {
            "borderRadius": "10",
            "borderColor": '#fff',
            "borderWidth": "2"
            },
            "label": {
            "show": "false",
            "position": 'center'
            },
            "emphasis": {
            "label": {
            "show": "true",
            "fontSize": '20',
            "fontWeight": 'bold'
            }
            },
            "labelLine": {
            "show": "true"
            },
            "data": x

            }
            ]
            }
        st_echarts(option)





#-------------------------------------------------------------------------------------------------
        #Platforms with most NUMBER of transactions
        # pie chart 
        st.markdown('* **Platforms with most NUMBER of transactions**')
        response = requests.get("https://node-api.flipsidecrypto.com/api/v2/queries/8507ec58-1154-4af4-aac0-2f078764e885/data/latest")
        x = response.json()

        option = {
            "tooltip": {
            "trigger": 'item'
            },
            "legend": {
            "top": '5%',
            "left": 'center'
            },
            "series": [
            {
            "name": 'Transactions',
            "type": 'pie',
            "radius": ['40%', '75%'],
            "avoidLabelOverlap": "false",
            "itemStyle": {
            "borderRadius": "10",
            "borderColor": '#fff',
            "borderWidth": "2"
            },
            "label": {
            "show": "false",
            "position": 'center'
            },
            "emphasis": {
            "label": {
            "show": "true",
            "fontSize": '20',
            "fontWeight": 'bold'
            }
            },
            "labelLine": {
            "show": "true"
            },
            "data": x

            }
            ]
            }
        st_echarts(option)



with tab2 : 
    st.subheader("How to Buy Doodles")
    st.markdown("Users who wish to purchase a Doodles NFT can do so in just a few steps:")
    st.markdown("* Go to an NFT marketplace like as OpenSea, LooksRare, and X2Y2.")
    st.markdown("* Search for the Doodles collection on the chosen marketplace.")
    st.markdown("* Find the Doodles NFT that you want to add to your collection. ")
    st.markdown("* Buy now! ")
    st.markdown("* After all of those steps have been completed, congratulations to the user as they now own their very own Doodles NFT.")
    st.subheader("How to Buy NFT ? Watch video below")
    st.video('https://youtu.be/ZrP0pGIu_rs')

    
