import requests
import json
import pandas as pd

class ConexaoApi:
    def __init__(self, accuweatherAPIKey):
        self.accuweatherAPIKey = accuweatherAPIKey
        self.lat = 'geoplugin_latitude'
        self.lon = 'geoplugin_longitude'

    def lat_lon(self, url_api):
        r = requests.get(url_api)
        if r.status_code != 200:
            print('Não foi possível obter as localização.')
        else:
            localizacao = json.loads(r.text)
            lat = localizacao[self.lat]
            lon = localizacao[self.lon]
            LocationAPIURL = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/' \
            + 'search?apikey='+ self.accuweatherAPIKey +'&q='+ lat + ',' + lon +'&language=pt-br'
            return LocationAPIURL

    def locationAPI(self, LocationAPIURL):
        r = requests.get(LocationAPIURL)
        if r.status_code != 200:
            print('Não foi possível obter a localização.')
        else:
            location_response = json.loads(r.text)
            codigo_local = location_response['Key']
            forecast_5_days = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' \
            + codigo_local +'?apikey='+ self.accuweatherAPIKey +'&language=pt-br&metric=true'
            
            cidade = location_response['LocalizedName']
            estado = location_response['AdministrativeArea']['LocalizedName']
            pais = location_response['Country']['LocalizedName']
            lista_forecast_5_dyas = []
            lista_forecast_5_dyas.append(forecast_5_days)
            lista_forecast_5_dyas.append(cidade)
            lista_forecast_5_dyas.append(estado)
            lista_forecast_5_dyas.append(pais)
            
            return lista_forecast_5_dyas

    def estrutura_dados_5_dias(self, lista_forecast_5_dyas):
        r = requests.get(lista_forecast_5_dyas[0])
        if r.status_code != 200:
            print('Não foi possível obter a localização.')
        else:
            conteudo_previsao = json.loads(r.text)
            return conteudo_previsao


    def listas_dados(self, conteudo_previsao, lista_forecast_5_dyas):
        data = []
        texto_dia = []
        texto_noite = []
        temp_max = []
        temp_min = []
        cidade = []
        estado = []
        pais = []

        dias_previsao = conteudo_previsao['DailyForecasts']
        for item_previsao in dias_previsao:
            data.append(item_previsao['Date'])
            texto_dia.append(item_previsao['Day']['IconPhrase'])
            texto_noite.append(item_previsao['Night']['IconPhrase'])
            temp_max.append(item_previsao['Temperature']['Maximum']['Value'])
            temp_min.append(item_previsao['Temperature']['Minimum']['Value'])

        
        while len(cidade) < len(data):
            cidade.append(lista_forecast_5_dyas[1])
            estado.append(lista_forecast_5_dyas[2])
            pais.append(lista_forecast_5_dyas[3])

        agrupamento = []
        agrupamento.append(data)
        agrupamento.append(texto_dia)
        agrupamento.append(texto_noite)
        agrupamento.append(temp_max)
        agrupamento.append(temp_min)
        agrupamento.append(cidade)
        agrupamento.append(estado)
        agrupamento.append(pais)

        return agrupamento

    def cria_data_frame(self, agrupamento):
        df = pd.DataFrame({'data': agrupamento[0], 
                    'texto_dia': agrupamento[1],
                    'texto_noite': agrupamento[2], 
                    'temp_max': agrupamento[3], 
                    'temp_min':agrupamento[4], 
                    'cidade': agrupamento[5], 
                    'estado': agrupamento[6], 
                    'pais': agrupamento[7]})

        df.to_csv('dados/cinco_dias_previsao.csv', sep=';', index = False)
        print(df)


