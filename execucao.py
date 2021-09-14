from conecta_api import ConexaoApi

# Execução do programa
conexao = ConexaoApi('insira aqui sua chave accuweather')
api_latitude_longetude = conexao.lat_lon('http://www.geoplugin.net/json.gp')
api_codigo_local = conexao.locationAPI(api_latitude_longetude)
api_estrutura_dados_5_dias = conexao.estrutura_dados_5_dias(api_codigo_local)
cria_listas_dados = conexao.listas_dados(api_estrutura_dados_5_dias, api_codigo_local)
conexao.cria_data_frame(cria_listas_dados)