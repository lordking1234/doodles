import streamlit as st
#import requests
#from streamlit_echarts import st_echarts
#import pandas as pd
#import base64

st.set_page_config(layout="wide")
  

# background color 
st.markdown("""<style>.main {background-color: #C8D3E0;}</style>""",unsafe_allow_html=True)

# background pucture  
#@st.experimental_memo
#def get_img_as_base64(file):
#    with open(file, "rb") as f:
#        data = f.read()
#    return base64.b64encode(data).decode()


hi = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/premium-vector/blue-white-gray-turquoise-background-gradient-wallpaper-background-vector-illustration_172010-1295.jpg?w=360");
background-size: 180%;
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

#-------------------------------------------------------------------------------------------------
st.title("Doodles")
st.empty()
st.empty()
st.empty()
st.image("https://nftnow.com/wp-content/uploads/2022/02/Doodles-Grid-2048x998.png")  
st.empty()
st.subheader("What is the Doodles NFT collection?")
st.empty()
st.markdown("Doodles features original art that was created by Martin, who produced hundreds of unique visual traits for the collection. However, the project ultimately followed in the footsteps of predecessors like CryptoPunks, Bored Apes, and Cool Cats by randomly mixing and matching these individual traits to create the full Doodles collection.")
st.markdown("Within the Doodles ecosystem live humans, cats, pickles, apes, sentient flames, skeletons, aliens, and more. As is the case with nearly all generative avatar collections, Doodles NFTs come in varying degrees of rarity, which is defined by their traits. Although the Doodles team has never officially released a catalog of what traits are the rarest and most common — you can find RaritySniffer’s unofficial rankings here — skeletons, cats, aliens, apes, and mascots have continued to resell for the highest amounts.")
st.image("https://nftnow.com/wp-content/uploads/2021/12/Doodles-Featured-1200x449.jpg")  
st.empty()
st.empty()
st.markdown("Keast, Castro, and Martin launched Doodles on October 17, 2021, originally pricing their product at 0.123 ETH per mint. At the time, the mint price was considered relatively high. Prior to Doodles, most PFP projects implemented mint prices below 0.1 ETH; however, the Doodles founding team decided on this higher price point to ensure an initial treasury of ~420 ETH.")
st.empty()
st.markdown("During the rollout of the project, Doodles tried something that had seemingly never been executed by a PFP project previously. About a month before the project went live for minting, the Doodles team closed the Discord when membership numbers had reached just over 1,000. This made it so that no new members could join, creating an extra level of exclusivity within the project’s community.")
st.empty()
st.markdown("This decision received mixed reviews, as it effectively gave whitelist access (priority minting) to a select few. Yet, as the Doodles mint date drew closer, the project’s following continued to grow, and the decision to close the Discord started to be seen as an innovative way to reward early NFT project supporters.")
st.subheader("Building a community for Doodles NFTs")
st.markdown("Shortly after the full supply of Doodles sold out, the Discord server was reopened, bringing a slew of new collectors and enthusiasts into the community. In the months following, a wide variety of NFT influencers and big-name celebrities would join Doodles as collectors, further solidifying the project as one of the hottest PFP NFT communities around.")
st.markdown("While numerous avatar projects market themselves as community-centered projects, Doodles seems to have been all about empowering their community from the start. As stated on the Doodles website, owning a Doodle and voting on community proposals “makes the roadmap collaborative.” This facet of the project has become increasingly clear over the last few months alone, thanks largely to its voting system and anti-scam/pro-artist culture.")
st.subheader("Doodles Fundraise")
st.markdown("In summer 2022, it was announced that 776 Management, a venture capital firm created by Reddit co-founder Alexis Ohanian, would lead the first round of funding for Doodles. Although the amount of financing was not disclosed, the partnership inherently seemed robust as it was also announced that 776 Co-Founder Katelin Holloway would be joining the Doodles board of directors.")
st.markdown("And indeed it was. A September 2022 announcement made it clear that Doodles’ first funding round was a resounding success. Aside from 776, 10T Holdings, Acrew Capital, and FTX Ventures pooled $54 million in funding for Doodles. With this funding, Holloway believes that Doodles now has the tools to “[develop] the next digital frontier of how we experience and create content, unlocking the real value behind NFTs,” according to the September announcement.")
st.markdown("Following the close of its funding round, Doodles looks primed to develop itself into a truly global IP via “ventures in music, culture and entertainment industries.” Of course, the technology that made Doodles possible in the first place is still at the center of everything: the blockchain. “Reimagining storytelling through the blockchain, Doodles is changing the way the world connects and interacts,” Holloway said, in the release.")


col11, col12 ,col13, col14 = st.columns ([0.5,1.5,1.5,0.5])

with col11  :
    st.empty()

with col12  :
    st.markdown("* **Reference** : [Doodle](https://twitter.com/doodles)")
    st.markdown("* **Reference** : [Flipsidecrypto](https://flipsidecrypto.xyz/)")
    st.markdown("* **Reference** : [Metricsdao](https://metricsdao.xyz/)")
    st.markdown("* **Reference** : [nftnow](https://nftnow.com/guides/doodles-guide/)")

with col13 :
    st.image("https://nftnow.com/wp-content/uploads/2022/02/Doodles-Guide-Feature-Image.png")

with col14 :
    st.empty()
