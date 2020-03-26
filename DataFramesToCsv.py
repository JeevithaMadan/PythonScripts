import pandas as pd

dict_data = {
    'CHN': {'COUNTRY': 'China', 'POP': 1_398.72, 'AREA': 9_596.96,
            'GDP': 12_234.78, 'CONT': 'Asia'},
    'IND': {'COUNTRY': 'India', 'POP': 1_351.16, 'AREA': 3_287.26,
            'GDP': 2_575.67, 'CONT': 'Asia'},
    'USA': {'COUNTRY': 'US', 'POP': 329.74, 'AREA': 9_833.52,
            'GDP': 19_485.39, 'CONT': 'N.America'},
    'IDN': {'COUNTRY': 'Indonesia', 'POP': 268.07, 'AREA': 1_910.93,
            'GDP': 1_015.54, 'CONT': 'Asia'},
    'BRA': {'COUNTRY': 'Brazil', 'POP': 210.32, 'AREA': 8_515.77,
            'GDP': 2_055.51, 'CONT': 'S.America'},
    'PAK': {'COUNTRY': 'Pakistan', 'POP': 205.71, 'AREA': 881.91,
            'GDP': 302.14, 'CONT': 'Asia'},
    'CAN': {'COUNTRY': 'Canada', 'POP': 37.59, 'AREA': 9_984.67,
            'GDP': 1_647.12, 'CONT': 'N.America'},
    'AUS': {'COUNTRY': 'Australia', 'POP': 25.47, 'AREA': 7_692.02,
            'GDP': 1_408.68, 'CONT': 'Oceania'},
    'KAZ': {'COUNTRY': 'Kazakhstan', 'POP': 18.53, 'AREA': 2_724.90,
            'GDP': 159.41, 'CONT': 'Asia'}
}


df = pd.DataFrame(dict_data).T
selectcolsfile = '.\OutputFiles\ColumnsToCsv.csv'
# write to csv file
# selecting particular columns to save in file
df[['COUNTRY','POP']].to_csv(selectcolsfile)

addcolsfile = '.\OutputFiles\AddColsToCsv.csv'
# adding new column to the dataframe
df['IND_DAY'] = ['','1947-08-15', '1776-07-04', '1945-08-17', '1822-09-07', '1947-08-14', '1867-07-01', '1991-12-16', '1952-08-15']
df.to_csv(addcolsfile, na_rep='(missing)')
# handling missing values 
df_missing_values = pd.read_csv(addcolsfile)
print('\nData Frame handled with missing values:\n', df_missing_values)
#dropping columns
df_drop_columns = pd.read_csv(addcolsfile)
df_drop_columns.drop(['IND_DAY'], axis =1, inplace = True) 
print('\nAfter dropping "IND_DAY" column :\n', df_drop_columns)
#display columns names
print('\nColumn Headers are:\n', df_drop_columns.head())
print('\n\n',list(df_drop_columns.columns.values))