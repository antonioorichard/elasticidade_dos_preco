 

![Analyzing customer groups](imagem/Ecommerce-Website.jpg) 

Este é um projeto fictício. Com dados públicos dos [E-commerce](https://billionaire365.com/2019/02/25/what-is-an-ecommerce-website/)
 das empresas Amazon, Bestbuy, barcodable , bhphotovideo, ebay, kmart e Walmart.
# 0 Resumo sobre o projeto

## 0.1 Modelo de Negócio

* E-commerce

## 0.2 Sede da empresa



1. **Amazon**
   - Sede: Seattle, Washington, EUA
   - Site: [Amazon](https://www.amazon.com)

2. **Best Buy**
   - Sede: Richfield, Minnesota, EUA
   - Site: [Best Buy](https://www.bestbuy.com)

3. **Barcodable**
   - Sede: Orlando, Florida, EUA
   - Site: [Barcodable](https://www.barcodable.com)

4. **B&H Photo Video**
   - Sede: Nova York, Nova York, EUA
   - Site: [B&H Photo Video](https://www.bhphotovideo.com)

5. **eBay**
   - Sede: San José, Califórnia, EUA
   - Site: [eBay](https://www.ebay.com)

6. **Kmart**
   - Sede: Hoffman Estates, Illinois, EUA
   - Site: [Kmart](https://www.kmart.com)

7. **Walmart**
   - Sede: Bentonville, Arkansas, EUA
   - Site: [Walmart](https://www.walmart.com)

## 0.3 Tipo de produto
 
* tv, television, video,
* laptop, computer
* speaker, portable, bluetooth
* camera, mirrorless, photo
* car, speaker e subwoofer
* receiver, amplifier, home
* camera, shoot
* drive, storage, hard
* drive, storage, internal
* car, receiver, dash
* player, home, audio
* headphone, earbud, ear
* headphone
* ipod, player
* ...

## 0.4 Problema

* Falta de conhecimento sobre como o aumento dos preços ou redução impacta as vendas (demanda pelo produto).
   * Decisões de Preço Inadequadas.
   * Perda de Clientes.
   * Gestão de Estoque Ineficiente.
   * Estratégia de Marketing Ineficaz.
   * Segmentação de Mercado Incorreta.
   * Problema de Competitividade.
   * Impacto nas Finanças.
   * Reputação da Marca.
 

## 0.5 Solução

* Calcular a elasticidade dos preços
  * Insights

## 0.6 Impacto da solução

* Personalizar a experiência ou adptar
  * Comunição.
  * Ofertas.
  * Recomendação.
* Segmentação de Marketing mais eficientes.
* Otimização do Estoque.

   ... 



*****************************************************************************************************************************************************************************



  

## 1. Problema de negócios 

### 1.1 Sobre a empresa 




### 1.2 Problema 

Uma empresa pretende alterar os preços dos produtos vendidos, mas tem receio dessa alteração impactar na demanda desses produtos e por consequência no faturamento. Essa demanda foi submetida para você e como analista/cientista de dados precisa determinar a elasticidade dos preços usando a metodologia científica embasado nos dados dos preços dos produtos vendidos pela empresa.

  

### 1.3 Motivação 

Maximizar o lucro por meio dos melhores ajustes dos preços. 

  

  

### 1.4 Demandas de negócio 

  

Produto de dados solicitado: 

* Estudo do impacto da alteração de preço sobre a vendas do produto, em primeiro momento o speaker. 

  

  

## 2. Premissas de negócio 

  

- Todos os produtos de dados entregues devem ser acessíveis via internet.

O planejamento da solução será validado com os times de negócio, visando garantir que as soluções desenvolvidas sejam úteis na sua tomada de decisão.

Serão realizadas o cálculo da elasticidade do preço nos produtos com uma significância estatística maior que 5%.


  

## 3. Planejamento da solução 

Baixar os dados e ler os dados

Executar o processo de limpeza de dados como:

renomear colunas

renomear categorias mudar de tipo de variável, caso necessário

Estatística descritiva com visualização

Feature Engineering

Machine Learning

Elasticidade

Business Performance

Cross Price Elasticity

### 3.1. Produto final 

  

O que será entregue efetivamente? 


- Um gráfico com a elesticidade de preços e os nomes do produtos
- Uma tabela com as elasticidade de preços e os nomes do produtos


  

### 3.2. Ferramentas 

  

Quais ferramentas serão usadas no processo? 

- Pyenv; 

- Jupyter Notebook; 

- Git, Github; 

- Python; 

- streamlit; 

- Sistema Linux. 

  

  

  

## 4. Resultados para o negócio 

  

### 4.1 Resultados 

  

![Dataset](imagem/df_elasticity_resultado.jpg) 


  

De acordo com os critérios definidos, foi segmentado os clientes em 13 grupos, embora não seja o melhor resultado como mostra a imagem da seção 5.1, mas apresenta um bom resultado. O motivo da escolha de 13 clusters em vez do melhor resultado 23 clusters, é a  facilidade para trabalhar com clientes em menos grupos 

  

Como resultado para o negócio foram criados: 

  

* Dataset ou conjunto de dados com a elasticidade dos preço e outras informações estatística como p-value. 

  

* Resultados no excel, caracterizando os principais clientes. 

  

* Insights sobre os negócios e principais clientes. 
	
	* Os clientes insider representa 14,21% da base de cliente
	* Os clientes insider representa 75,33% da receita gerada.
	* Os clientes insider compra uma grande quantidade de produtos.
	* Os clientes insider tem maior número de retorno, isso pode ser devido os atacandistas compram em grande quantidade, então ao cancelar é número grande de retorno.
    * Os clientes insider tem uma intervalo médio de 32 dias para realizar novamente uma compra.
    * Observação: Pode ser tirado mais informações das features criadas em relação aos clientes.
  

## 5. Conclusão 

  

* O objetivo foi alcançado, dado que o produto de dados foram gerados com sucesso. O funcionario pode utilizar a ferramenta criado para fazer a elasticidade de preço. 

  

Planilha no google sheets [Planilha com resultados do perfil dos grupos](https://docs.google.com/spreadsheets/d/1sODujh6S8vNwnoUkBMuaOJWzYAolyqs-JhU4cWSq5oo/edit?usp=sharing). 

  

  

[Dashbord no streamlit](https://elasticidade-dashbord.streamlit.app/) 

  

  

## 6. Próximos passos 

  

Algumas melhorias no projeto podem ser incrementadas no futuro: 

  

* Carregar os dados em servidor. 

* Deploy do modelo. 

* Criar um botão com api do modelo de Machine Learning no google sheets para que resultado seja emitido nele com as médias de característica dos clientes. 

* Deixar um dashbord no streamlit ou metabase com informações dos dados. 

  

## 7 Referências 

* Este Projeto foi feito como parte do curso "DS em Produção", da [Comunidade DS](https://www.comunidadedatascience.com/). 

* O Dataset foi obtido no [UC irvine](https://archive.ics.uci.edu/dataset/502/online+retail+ii). 

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

#### Observação:  

**Python 3.12.3** 
