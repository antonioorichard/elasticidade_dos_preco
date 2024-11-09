# Libre
import os 

import pandas as pd 
from matplotlib import pyplot as plt

import streamlit as st
import seaborn as sns

# code
home_path  = os.getcwd()
df_business_performance_path = os.path.join( home_path, "data", "business_performance.csv")
df_crossprice_path           = os.path.join( home_path, "data", "crossprice.csv")
df_elasticity_path           = os.path.join( home_path, "data", "df_elasticity.csv")

# Carregar os dataframes
df_business      = pd.read_csv( df_business_performance_path)
df_crossprice    = pd.read_csv( df_crossprice_path)
df_elasticity    = pd.read_csv( df_elasticity_path)

# Layout Streamlit
st.set_page_config( layout = "wide")
st.header( "Elasticidade referente aos Preços dos Produtos")

tab1, tab2, tab3 = st.tabs(
    [
                    "Elasticidade de Preços dos Produtos", 
                    "Business Performances", 
                    "Elasticidade Cruzada de Preços", 
    ])




with tab1:
    tab4, tab5 = st.tabs(
        ["Elasticidade de Preços - Gráfico", "Elasticidade de Preços - DataFrame"]
    )
    with tab4: 
        # Apresentar a elasticidade dos preços graficamente
        st.header("Elasticidade de Preços - Gráfico")
        df_elasticity["ranking"] = (
            df_elasticity.loc[:, "price_elasticity"].rank( ascending = True).astype( int )
        )
        df_elasticity = df_elasticity.reset_index(drop = True)

        fig, ax       = plt.subplots( figsize = ( 12, 4))
        
        ax.hlines(
            y         = df_elasticity["ranking"], 
            xmin      = 0,
            xmax      = df_elasticity["price_elasticity"], 
            alpha     = 0.5, 
            linewidth = 10 ,
        )
        for name, p in zip(df_elasticity["name"], df_elasticity["ranking"]):
            ax.text(4, p, name)

        for x, y, s in zip(df_elasticity["price_elasticity"], df_elasticity["ranking"], df_elasticity["price_elasticity"]):
            ax.text(
                x + 22 if ( x < 20)  else x - 0.5, 
                y, 
                round(s, 2), 
                horizontalalignment = "right" if x < 0 else "left",
                verticalalignment   = "center", 
                fontdict            = { "color": "red" if x < 0 else "green", "size" :10}
                
                    )
        plt.gca().set( ylabel = "Ranking Number", xlabel = "Price Elasticity")
        plt.title("Price Elasticity")
        ax.grid(linestyle = "--")
        st.pyplot(fig)
# outro gráfico
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x='name', y='price_elasticity', data=dfe)

        # Adicionar os valores nas barras
        for index, row in dfe.iterrows():
            ax.text(
                index, 
                row.price_elasticity, 
                round(row.price_elasticity, 2), 
                color='black', 
                ha="center"
            )
        
        plt.xticks(rotation=60)
        plt.xlabel('Name')
        plt.ylabel('Price Elasticity')
        plt.title('Price Elasticity of Different Products')
        plt.show()
    
    with tab5: 
        # Apresentar elasticidade de preços datagrame
        st.header("Elasticidade de Preços - DataFrame")
        df_order_elasticity = (df_elasticity[["ranking", "name", "price_elasticity"]].
                               sort_values(by = "price_elasticity", ascending =False)
                              )
        st.dataframe(df_order_elasticity, use_container_width = True )

with tab2:
    # apresentar business performance
    st.header("Business Performance")
    df_business = df_business.set_index("name")
    st.dataframe( df_business, use_container_width = True )

with tab3:
    # apresentar elasticidade cruzada de preços 
    st.header("Elasticidade Cruzada de Preços")
    df_crossprice = df_crossprice.set_index("name")
    st.dataframe(df_crossprice, use_container_width = True)
