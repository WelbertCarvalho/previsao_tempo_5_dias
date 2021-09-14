## Previsão do tempo - 5 dias

###Este repositório contém 2 versões de uma mesma aplicação.

###1 - Arquivo app_5_dias_previsao.py

Contém o código procedural para realizar a previsão do tempo em determinada região através de APIs do site accuweather.
Para buscar as informações da API, é necessário realizar cadastro no site e gerar uma accuweatherAPIKEY. O plano gratuíto permite realizar 100 requisições diárias.
A API utilizada aceita uma chave padrão de localidade. Por este motivo, primeiro é necessário identificar a chave padrão da localidade utilizando-se informações de latitude e longitude.
Após obter a chave para a localidade, é necessário acessar a API que contem as informações de data, texto do dia, texto da noite, temperatura máxima e temperatura mínima.
Neste ponto, inserimos os dados em um DataFrame utilizando a lib pandas e exportando para um arquivo .CSV. Desta forma é possível utilizar estes dados para análises metereológicas.

###2 - Arquivos conecta_api.py e execucao.py

O arquivo conecta_api contém a classe ConexaoApi. Neste arquivo, toda a lógica do código que inicialmente havia sido desenvolvida de forma procedural conforme descrito no item 1, foi remodelado e organizado em funções dentro da classe ConexaoApi para facilitar a inclusão de novas funcionalidades e manutenções posteriores.
O arquivo execucao.py contém a instância da classe e chama todas as funções necessárias para a execucao do programa.
