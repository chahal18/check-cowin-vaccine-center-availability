import pandas as pd
import requests

states = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states')
if states.status_code == 200:
        states = states.json()['states']

        for state in states:
            districts = requests.get(f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state["state_id"]}')
            if districts.status_code == 200:
                districts = districts.json()['districts']

                for district in districts:

                    tmp = {'state_id': state["state_id"], 'state': state['state_name'], 'district_id': district['district_id'], 'district': district['district_name']}
                    refined_states_districts.append(tmp)


        df = pd.DataFrame(data=refined_states_districts)
        df.to_csv("district_codes.csv", sep=',',index=False)
        print('File generated!')
