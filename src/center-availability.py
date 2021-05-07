import requests, json, tabulate, copy, os
from time import sleep

def filter_center(district_data,min_age_booking,minimum_slots):
    options = []

    if len(district_data['centers']) >= 0:
        for center in district_data['centers']:
            for session in center['sessions']:
                if (session['available_capacity'] >= minimum_slots) and (session['min_age_limit'] <= min_age_booking):
                    out = {
                        'name': center['name'],
                        'district': center['district_name'],
                        'center_id': center['center_id'],
                        'available': session['available_capacity'],
                        'min_age_limit': session['min_age_limit'],
                        'date': session['date']
                    }
                    options.append(out)
                else:
                    pass
    else:
        pass

    return options

def display_table(dict_list):

    header = ['idx'] + list(dict_list[0].keys())
    rows = [[idx + 1] + list(x.values()) for idx, x in enumerate(dict_list)]
    print(tabulate.tabulate(rows, header, tablefmt='grid'))

def make_request(district_id,date,headers):
    try:
        data = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={}&date={}'.format(district_id,date), headers = headers)
        return data
    except:
        print('Try again!')

district_id = input("Enter the district id: ")
date = input("Enter the date for which center availability's haas to be checked (format: DD-MM-YYYY -> 08-05-2021 ): ")
min_age_booking = int(input("Enter your age in years (example -> 20): "))
minimum_slots = int(input("Enter center's minimum available_capacity in numbers (example -> 3): "))
enable_auto_refresh = int(input("Enable auto refresh if center available count? Enter 1 for 'yes' and 0 for 'no': "))



headers = {
    'authority': 'cdn-api.co-vin.in',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'if-none-match': 'W/"256e-oyx5XR8C82STUtrd4mDE6jLcBqM"'
}

count = 0
while count == 0:
    district_data = make_request(district_id,date,headers)

    shortlisted_center = []

    district_data = district_data.json()
    shortlisted_center = filter_center(district_data, min_age_booking,minimum_slots)
    if len(shortlisted_center) > 0:
        display_table(shortlisted_center)
        os.system('say -v Alex "Available Center Count - {}"'.format(str(len(shortlisted_center))))
    else:
        print('No center available')

    if enable_auto_refresh == 0 or len(shortlisted_center) > 0:
        break
    sleep(30)
