import pandas as pd
dataframe_2021 = pd.read_csv('Ulaanbaatar_PM2.5_2021_YTD.csv')
dataframe_2020 = pd.read_csv('Ulaanbaatar_PM2.5_2020_YTD.csv')
dataframe_2019 = pd.read_csv('Ulaanbaatar_PM2.5_2019_YTD.csv')
dataframe_2018 = pd.read_csv('Ulaanbaatar_PM2.5_2018_YTD.csv')


#print(pd.options.display.max_rows) 
# default value is 60 

pd.options.display.max_rows = 99999
#print(dataframe_2021)
#one_line = dataframe_2021.head()
# dataframe_2021.shape()

# print(one_line)
#dataframe_2021_oneline = dataframe_2021.query("Month == '1'")
#print(dataframe_2021_oneline)

dataframe_master = pd.merge(dataframe_2021,dataframe_2020,how = "outer").merge(dataframe_2019,how='outer').merge(dataframe_2018,how='outer')
#print(dataframe_master)

row_head=dataframe_master.head(5)
row_tail=dataframe_master.tail(5)


# TESTING 
# print("\t 5 head rows \n")
# print(row_head)

# print("\t 5 tail rows \n")
# print(row_tail)

Parameter_Type  =type(dataframe_2021.Parameter[0])
Site_Type       =type(dataframe_2021.Site[0])
#  DateLT_Type     =type(dataframe_2021.Date+LT[0])   ---> check the space variable_name from source ??? 
Year_Type       =type(dataframe_2021.Year[0])
Month_Type      =type(dataframe_2021.Month[0])
Day_Type        =type(dataframe_2021.Day[0])
Hour_Type       =type(dataframe_2021.Hour[0])
#NowCast_Conc_Type       =type(dataframe_2021.Nowcast Conc[0])  --> Spacing ??
AQI_Type        =type(dataframe_2021.AQI[0])
#AQI_Category_Type       =type(dataframe_2021.AQI Category[0])  ---> spacing ??
#Raw_Conc_Type  =type(dataframe_2021.Raw Conc [0])
#Conc_Unit_Type  =                                              ---> spacing ??
Duration_Type   =type(dataframe_2021.Duration[0])
#QC_Name_Type    =type(dataframe_2021. [0])                     ---> spacing ??



print("Site:",Site_Type)
print("Parameter:",Parameter_Type)
print("Site:",Year_Type)
print("Parameter:",Month_Type)
print("Site:",Day_Type)
print("Parameter:",Hour_Type)
print("Site:",AQI_Type)
print("Parameter:",Duration_Type)

