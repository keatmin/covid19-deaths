import requests
URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'


def main(): 
    r = requests.get(URL)

    if r.status_code == 200:
        with open('data/covid19_deaths.csv', 'wb') as csv: 
            csv.write(r.content)
        
    else:
        print('Link invalid')
        
        
if __name__=='__main__': 
    main()
    