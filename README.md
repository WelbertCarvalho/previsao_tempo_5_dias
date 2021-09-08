## Previsão do tempo - 5 dias

No arquivo app_5_dias_previsao.py, existe o código para realizar a previsão do tempo em determinada região através de APIs do site accuweather.
Para buscar as informações da API, é necessário realizar cadastro no site e gerar uma accuweatherAPIKEY. O plano gratuíto permite realizar 100 requisições diárias.
A API utilizada aceita uma chave padrão de localidade. Por este motivo, primeiro é necessário identificar a chave padrão da localidade utilizando-se informações de latitude e longitude.
Após obter a chave para a localidade, é necessário acessar a API que contem as informações de data, texto do dia, texto da noite, temperatura máxima e temperatura mínima.
Neste ponto, inserimos os dados em um DataFrame utilizando a lib pandas e exportando para um arquivo .CSV. Desta forma é possível utilizar estes dados para análises metereológicas.
