# Checking Vaccine center's availability

This repo is created for finding the center availablity based on parameters like:
  1. district 
  2. Date
  3. minimum age limit 
  4. minimum slot

The `center-availability.py` is the main script which will find the center for you. But for feeding the required data to it, you have to run `fetch_district_id.py` script which will update the csv file `district_codes.csv` for you to have fresh state and district id. You would be required to provide the 'district_id' for your district. 

Example: For `Gurgaon`, `district_id` is `188`.


If `auto-refresh` is enabled then center's availability will be checked every 30th second. 

Clone the repo and start helping each other. 

![image](https://user-images.githubusercontent.com/16899332/117498065-e7921d80-af96-11eb-9fb4-c9de094b513f.png)

Pick `district_id` from `district_codes.csv`

![image](https://user-images.githubusercontent.com/16899332/117498214-21632400-af97-11eb-8c3e-18be69262aed.png)
