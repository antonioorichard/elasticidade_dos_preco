 

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
 
* tv, television, video, laptop, computer, speaker, portable, bluetooth, camera, mirrorless, photo, car, speaker e subwoofer.

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

* Uma clusterização com descrição das características dos melhores clientes. 

  

  

## 2. Premissas de negócio 

  

- Todos os produtos de dados entregues devem ser acessíveis via internet.

O planejamento da solução será validado com os times de negócio, visando garantir que as soluções desenvolvidas sejam úteis na sua tomada de decisão.

Serão realizadas o cálculo da elasticidade do preço nos produtos com uma significância estatística maior que 5%.


  

## 3. Planejamento da solução 

  

### 3.1. Produto final 

  

O que será entregue efetivamente? 


- Um grafico com a elesticidade de preços e os nomes do produtos
- Uma tabela com as elasticidade de preços e os nomes do produtos


  

### 3.2. Ferramentas 

  

Quais ferramentas serão usadas no processo? 

- Pyenv; 

- Jupyter Notebook; 

- Git, Github; 

- Python; 

- Google Sheets; 

- Sistema Linux. 

  

## 4. Os 3 principais insights dos clientes 

  

#### 1 Qual o período do ano que mais vende? 

  

* 1. novembro.  

* 2. outubro.  

* 3. setembro. 

  

* Insight de negócio: Como se trata de um ecommerce de produtos voltados para presentes, existe um aumento significativo de vendas nos meses de setembro até a novembro. O que pode ser explicado no que se refere aos meses próximo do Natal e festividades. Contudo, nota se compras em atacado, o que remete a presença de revendedores, principalmente para o mês de outubro.  A empresa pode abraçar dando promoção a esses atacadistas ou limitar a quantidade de compra para aqueles produtos que tem uma previsão alta de vendas entre os dois últimos meses do ano, e buscar fazer elas mesmo a venda neste mercado. 

  

  

#### 2 Qual o período do ano que menos vende? 

  

* 1. dezembro. 

* 2. fevereiro. 

* 3. abril. 

  

  

  

#### 3 Qual país é do cliente que mais compra? 

  

* United Kingdom, o que era de espera já que maior parte das vendas é para United Kingdom. 

  

* Insight de negócio: É necessária uma pesquisa para saber o motivo das vendas está concentrado mais em United Kingdom. 

  

  

## 5. Resultados para o negócio 

  

### 5.1 Resultados do cluster 

  

![Silhouete Score](image/silhouete_score.jpg) 

  

### 5.2 Mapa dos cluster encontrado 

  

![Silhouete Score](image/mapa_cluster.jpg) 

  

De acordo com os critérios definidos, foi segmentado os clientes em 13 grupos, embora não seja o melhor resultado como mostra a imagem da seção 5.1, mas apresenta um bom resultado. O motivo da escolha de 13 clusters em vez do melhor resultado 23 clusters, é a  facilidade para trabalhar com clientes em menos grupos 

  

Como resultado para o negócio foram criados: 

  

* Dataset ou conjunto de dados em sqlite. 

  

* Resultados no excel, caracterizando os principais clientes. 

  

* Insights sobre os negócios e principais clientes. 
	
	* Os clientes insider representa 14,21% da base de cliente
	* Os clientes insider representa 75,33% da receita gerada.
	* Os clientes insider compra uma grande quantidade de produtos.
	* Os clientes insider tem maior número de retorno, isso pode ser devido os atacandistas compram em grande quantidade, então ao cancelar é número grande de retorno.
    * Os clientes insider tem uma intervalo médio de 32 dias para realizar novamente uma compra.
    * Observação: Pode ser tirado mais informações das features criadas em relação aos clientes.
  

## 5. Conclusão 

  

* O objetivo do projeto foi alcançado, dado que os produtos de dados propostos foram gerados com sucesso. O time de negócio irar utilizar para a tomada de decisão. 

  

Planilha no google sheets [Planilha com resultados do perfil dos grupos](https://docs.google.com/spreadsheets/d/1sODujh6S8vNwnoUkBMuaOJWzYAolyqs-JhU4cWSq5oo/edit?usp=sharing). 

  

  

![Planilha com a média do perfil dos grupos](image/result.jpg) 

  

Em relação aos tons de cores deve interpretar em relação ao quanto este grupo dar lucro a empresa verde e azul são cores que quanto mais fortes mais dar lucro. já as demais cores quanto mais forte menos dá lucro. Observação a tabela já está organizada neste sentido. 

  

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

A falta de conhecimento sobre como o aumento ou a redução dos preços impacta as vendas pode gerar diversos problemas para uma empresa. Aqui estão alguns dos principais:

1. **Decisões de Preço Inadequadas:**
   - **Aumento de Preços:** Se uma empresa não entende a sensibilidade ao preço dos seus clientes, pode aumentar os preços de forma inadequada e, como resultado, perder vendas e participação de mercado.
   - **Redução de Preços:** Uma redução de preço sem análise adequada pode levar a margens de lucro mais baixas, reduzindo a rentabilidade mesmo que as vendas aumentem.

2. **Perda de Clientes:**
   - A falta de compreensão sobre a elasticidade da demanda pode resultar em preços que afastam os consumidores. Um aumento considerável de preço em produtos essenciais pode levar à perda de clientes para concorrentes.

3. **Gestão de Estoques Ineficiente:**
   - A inadequação na previsão de demanda impactada por mudanças de preços pode levar a excessos ou faltas de estoque. Isso gera custos adicionais com armazenamento ou perda de vendas por falta de produtos.

4. **Estratégia de Marketing Ineficaz:**
   - Um preço mal definido pode comprometer as campanhas de marketing. Se a empresa não sabe como o preço afeta a percepção do consumidor, campanhas podem ser direcionadas de forma ineficaz.

5. **Segmentação de Mercado Incorreta:**
   - Não entender como diferentes segmentos de clientes reagem a mudanças de preço impede que a empresa crie ofertas personalizadas que atendam às necessidades específicas de cada grupo.

6. **Problemas de Competitividade:**
   - Empresas que não acompanham a concorrência em termos de preços podem perder espaço no mercado. O desconhecimento das práticas de precificação pode fazer com que a empresa fique em desvantagem competitiva.

7. **Impacto nas Finanças:**
   - A má gestão de preços pode afetar o fluxo de caixa e a saúde financeira da empresa, levando a dificuldades financeiras e até insolvência.

8. **Reputação da Marca:**
   - Alterações de preços mal gerenciadas podem afetar negativamente a percepção da marca. Se os consumidores sentirem que estão sendo explorados com preços injustos, a lealdade à marca pode ser comprometida.

Entender a relação entre preço e demanda é crucial para uma gestão eficaz e a sustentação do crescimento da empresa. Investir em pesquisas de mercado e análises financeiras pode ajudar a mitigar esses problemas. 
