import pandas as pd
import json

list_data =[ 
                ['India', 1_351.16, 3_287.26, 2_575.67, 'Asia', '1947-08-15'],
                ['China', 1_398.72, 9_596.96, 12_234.78, 'Asia', '1940-03-02'],
                ['US', 329.74, 9_833.52, 19_485.39, 'N.America', '1776-07-04'],
                ['Indonesia', 268.07, 1_910.93, 1_015.54, 'Asia', '1945-08-17'],
                ['Brazil', 210.32, 8_515.77, 2_055.51, 'S.America', '1822-09-07'],
                ['Japan', 126.22, 377.97, 4_872.42, 'Asia', '1852-03-04']
           ]

columns = ('COUNTRY', 'POP', 'AREA', 'GDP', 'CONT', 'IND_DAY')
print(list_data.count)
df = pd.DataFrame(list_data, columns = columns, index = [0, 1, 2, 3, 4, 5])
csvfilename = '.\OutputFiles\listtocsv.csv'
# write to csv file
df.to_csv(csvfilename)

jsonfilename = '.\OutputFiles\listtojson.json'
#write to json file
df.to_json(jsonfilename)


