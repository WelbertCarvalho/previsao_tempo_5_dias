import requests
import json
import pandas as pd

accuweatherAPIKey = 'insira_sua_chave_aqui'

r = requests.get('http://www.geoplugin.net/json.gp')

if r.status_code != 200:
    print('Não foi possível obter a localização.')
else:
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    lon = localizacao['geoplugin_longitude']
    LocationAPIURL = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/' \
    + 'search?apikey='+ accuweatherAPIKey +'&q='+ lat + ',' + lon +'&language=pt-br'
    
    r2 = requests.get(LocationAPIURL)
    if r2.status_code != 200:
        print('Não foi possível obter a locaização.')
    else:
        location_response = json.loads(r2.text)
        nome_local = location_response['LocalizedName'] + ', ' + location_response['AdministrativeArea']['LocalizedName'] + '. ' + location_response['Country']['LocalizedName']
        codigo_local = location_response['Key']
        
        forecast_5_days = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/'+ codigo_local +'?apikey='+ accuweatherAPIKey +'&language=pt-br&metric=true'

        r3 = requests.get(forecast_5_days)
        if r3.status_code != 200:
            print('Não foi possível obte a localização.')
        else:
            data = []
            texto_dia = []
            texto_noite = []
            temp_max = []
            temp_min = []
            conteudo_previsao = json.loads(r3.text)

            dias_previsao = conteudo_previsao['DailyForecasts']
            for item_previsao in dias_previsao:
                data.append(item_previsao['Date'])
                texto_dia.append(item_previsao['Day']['IconPhrase'])
                texto_noite.append(item_previsao['Night']['IconPhrase'])
                temp_max.append(item_previsao['Temperature']['Maximum']['Value'])
                temp_min.append(item_previsao['Temperature']['Minimum']['Value'])


            df = pd.DataFrame({'data': data, 'texto_dia': texto_dia,'texto_noite': texto_noite, 'temp_max': temp_max, 'temp_min':temp_min})
            df.to_csv('cinco_dias_previsao.csv', sep=';', index = False)

            


           