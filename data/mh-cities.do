// first I tabbed all the dates and pasted those into the spreadsheet to create the new observations for Mumbai metro
// then run these commands to generate the Mumbai metro averages

bys date: egen mumbai_metro_avg = mean(pm10) if city_name=="Mumbai Metro" | city_name=="Mumbai" | city_name=="Navi Mumbai" | city_name=="Panvel" | city_name=="Thane" | city_name=="Taloja" | city_name=="Dombivali" | city_name=="Bhiwandi" | city_name=="Kalyan" | city_name=="Ulhasnagar" | city_name=="Ambernath" | city_name=="Badlapur"
replace pm10 = mumbai_metro_avg if city_name=="Mumbai Metro"
drop mumbai_metro_avg
drop if city_name=="Mumbai Metro" & missing(pm10)
