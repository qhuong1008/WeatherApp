#%%
#import libraries
import re
from turtle import title
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


import pandas as pd
data = pd.read_csv('./weatherApp/Data02.csv')
df = pd.DataFrame(data)
df




#%%

class SetDaTaNgay:
    def __init__(self, id_PT, _Day, _Month, _Year):
        self.tinh_PT = id_PT
        self._Day = _Day
        self._Month = _Month
        self._Year = _Year


class SetDaTaThang:
    def __init__(self, id_PT, _Month, _Year, Type_PT):
        self.tinh_PT = id_PT
        self._Month = _Month
        self._Year = _Year
        self.Type_PT = Type_PT

class loai_PT:
    def __init__(self, type_PT):
        if type_PT == 'TEMP_2M':
            self.title_PT = 'Nhiệt độ' 
            self.label_y = '(C)'

        elif type_PT == 'DEW_FROST':
            self.title_PT = 'Điểm sương' 
            self.label_y = '(C)'

        elif type_PT == 'HUMI_2M':
            self.title_PT = 'Độ ẩm' 
            self.label_y = '(g/kg)'

        elif type_PT == 'PRECTOTCORR':
            self.title_PT = 'Lượng mưa' 
            self.label_y = '(mm/ngày)'

        elif type_PT == 'SURF_PRESS':
            self.title_PT = 'Áp suất bề mặt' 
            self.label_y = '(kPa)'

        elif type_PT == 'WIND_DIREC':
            self.title_PT = 'Hướng gió' 
            self.label_y = '(Degrees)'

        elif type_PT == 'WIND_SPEED':
            self.title_PT = 'Tốc độ gió' 
            self.label_y = '(m/s)'

            

def set_GiaTri(df, Type_PT):
    print('Max = ', df[Type_PT].max())
    print('Min = ', df[Type_PT].min())
    print('Avg = ', df[Type_PT].mean())
    df




def thongKeThang(id_PT, _Month, _Year, Type_PT):
    loaiPT = loai_PT(Type_PT)
    data_Thang = df[(df['ID'] == id_PT) & (df['YEAR'] == _Year) &(df['MO'] == _Month) ]
    ketqua = data_Thang[['DATE', 'DATE_M', 'TINH', Type_PT]]
    
    plt.figure(figsize=(20, 10))
    sns.barplot(x= 'DATE', y= Type_PT, data = ketqua)
    plt.xlabel("DATE") 
    plt.ylabel(loaiPT.label_y) 
    title_ = loaiPT.title_PT + ' thống kê của tháng ' + str(_Month) + '/' + str(_Year)
    plt.title(title_) 
    plt.xticks(rotation= 90) 
    plt.savefig('weatherApp/static/hinhanh.png')
    # plt.show()

    ketqua.columns = ['DATE', 'DATE_M', 'Tỉnh',loaiPT.title_PT]
    ketqua.reset_index()
    return ketqua

thongKeThang(21, 3, 2022, 'TEMP_2M')


#%%

def thongKeNgay(id_PT, _Day, _Month, _Year):
    _index = df[(df['ID'] == id_PT) & (df['YEAR'] == _Year) & 
    (df['MO'] == _Month) & (df['DY'] == _Day)].iloc[0].name

    dataNgay = df[['DATE', 'TINH', 'PRECTOTCORR', 'SURF_PRESS',
     'DEW_FROST', 'TEMP_2M', 'WIND_DIREC', 'WIND_SPEED', 'HUMI_2M']]
    ketqua = dataNgay.iloc[_index]
    ketqua = ketqua.to_frame()
    # ko co hinh 
    ketqua = pd.DataFrame({'Loại':['DATE','Tỉnh','Lượng mưa','Áp suất','Điểm sương','Nhiệt độ','Hướng gió','Tốc độ gió','Độ ẩm'],
                   'Dữ liệu':[df['DATE'][_index],df['TINH'][_index],df['PRECTOTCORR'][_index],
                              df['SURF_PRESS'][_index],df['DEW_FROST'][_index],df['TEMP_2M'][_index],
                              df['WIND_DIREC'][_index],df['WIND_SPEED'][_index],df['HUMI_2M'][_index]]})
    ketqua = ketqua.reset_index()
    ketqua = ketqua.drop('index', 1)
    return ketqua

# thongKeNgay(23,1,2,2020)


#%%
import js2py

def getTypeName(id):
    ten = ""
    if id == "TEMP_2M": ten = "Nhiệt độ"
    elif id == "DEW_FROST": ten = "Điểm sương"
    elif id == "HUMI_2M": ten == "Độ ẩm"
    elif id == "PRECTOTCORR": ten = "Lượng mưa"
    elif id == "SURF_PRESS": ten = "Áp suất bề mặt"
    elif id == "WIND_SPEED": ten = "Tốc độ gió"
    elif id == "WIND_DIREC": ten = "Hướng gió"
    return ten

def thongKeChung(_Month, _Year, Type_PT):
    loaiPT = loai_PT(Type_PT)

    data_chung = df[(df['YEAR'] == _Year) & (df['MO'] == _Month)]

    ketqua = data_chung[['DATE_M', 'TINH', Type_PT]]
    kq = ketqua.groupby(['DATE_M','TINH'])[Type_PT].mean().round(2).to_frame()
    kq = kq.reset_index()
    
    plt.figure(figsize=(20, 10))
    sns.barplot(x= 'TINH', y= Type_PT, data = kq)
    plt.xlabel("TINH") 
    plt.ylabel(loaiPT.label_y) 
    loai = getTypeName(Type_PT)
    title_ = loai + ' thống kê của các tỉnh tháng ' + str(_Month) + '/' + str(_Year)
    plt.title(title_) 
    plt.xticks(rotation= 90) 
    plt.savefig('weatherApp/static/hinhanh.png')

    kq.columns = ['DATE_M', 'Tỉnh',loaiPT.title_PT]
    kq.reset_index()
    return kq
    
# thongKeChung(24,1,2020,'TEMP_2M')

#%%
def thongKeQuy(id_PT, _quy, _Year, Type_PT):  
    loaiPT = loai_PT(Type_PT)
    if _quy == 1:
        _Mo_S = 1
        _Mo_M = 2
        _Mo_E = 3
    elif _quy == 2:
        _Mo_S = 4
        _Mo_M = 5
        _Mo_E = 6
    elif _quy == 3:
        _Mo_S = 7
        _Mo_M = 8
        _Mo_E = 9
    elif _quy == 4:
        _Mo_S = 10
        _Mo_M = 11
        _Mo_E = 12
    data_quy_S = df[(df['ID'] == id_PT) & (df['YEAR'] == _Year) & (df['MO'] == _Mo_S)]
    data_quy_M = df[(df['ID'] == id_PT) & (df['YEAR'] == _Year) & (df['MO'] == _Mo_M)]
    data_quy_E = df[(df['ID'] == id_PT) & (df['YEAR'] == _Year) & (df['MO'] == _Mo_E)]

    ketqua = data_quy_S.append(data_quy_M)
    ketqua = ketqua.append(data_quy_E)
    
    plt.figure(figsize=(20, 10))
    sns.barplot(x= 'DATE_M', y= Type_PT, data = ketqua)
    plt.xlabel("Tháng") 
    loai = getTypeName(loaiPT.title_PT)
    plt.ylabel(loai) 
    title_ = loai + ' thống kê của quý '+ str(_quy) + ' năm ' + str(_Year)
    plt.title(title_) 
    plt.xticks(rotation= 45) 
    plt.savefig('weatherApp/static/hinhanh.png')
    
    ketqua = ketqua[['DATE', 'DATE_M', 'TINH', Type_PT]]
    ketqua.columns = ['DATE', 'DATE_M', 'Tỉnh',loaiPT.title_PT]
    ketqua = ketqua.reset_index()

    return ketqua


# thongKeQuy(2, 2, 2022, 'DEW_FROST')

#%%
def thongKeNam(id_PT, _Year, Type_PT):
    
    loaiPT = loai_PT(Type_PT)

    data_Thang = df[(df['ID'] == id_PT) & (df['YEAR'] == _Year)]

    ketqua = data_Thang[['DATE', 'DATE_M', 'TINH', Type_PT]]
    
    plt.figure(figsize=(20, 10))
    sns.barplot(x= 'DATE_M', y= Type_PT, data = ketqua)
    plt.xlabel("MONTH") 
    plt.ylabel(loaiPT.label_y) 
    title_ = loaiPT.title_PT + ' thống kê của năm ' + str(_Year)
    plt.title(title_) 
    plt.xticks(rotation= 45) 
    plt.savefig('weatherApp/static/hinhanh.png')
    # plt.show()
    ketqua = ketqua[['DATE', 'DATE_M', 'TINH', Type_PT]]
    ketqua.columns = ['DATE', 'DATE_M', 'Tỉnh',loaiPT.title_PT]
    
    ketqua = ketqua.reset_index()
    ketqua = ketqua.drop('index', 1)
    return ketqua

# thongKeNam(20, 2022, 'PRECTOTCORR')





#%%

# if __name__ == '__main__':

    
    
#     id_PT = '20'

#     Year_Sel = 2022
#     Month_Sel = 4


#     Time_PT = 'Month'

#     if Time_PT == 'Day':
#         #set giá trị
#         datangay_set = SetDaTa('BRUNEI', 7, 3, 2022, 10, 4, 2022, 'TEMP_2M')
#         #vẽ biểu đồ và lọc dữ liệu
#         dataNgay = thongKeTheoNgay(df, datangay_set.country_PT, datangay_set.Day_Start, datangay_set.Month_Start, datangay_set.Year_Start, datangay_set.Day_End, datangay_set.Month_End, datangay_set.Year_End, datangay_set.Type_PT)
#         #lọc ra những cột cần thiết
#         dataNgay = dataNgay[['COUNTRY', 'DATE', datangay_set.Type_PT]]
#         dataNgay #dataframe cần in ra
#         #lấy min max trung bình
#         set_GiaTri(dataNgay, datangay_set.Type_PT)

#         #Nếu dùng dataframe thì ko cần xuất file csv-> bỏ dòng này cũng được
#         export_file_cvs= dataNgay.to_csv ('dataNgay.csv', index = None, header=True)

        
#     elif Time_PT == 'Month':
                
#         datathang_set = SetDaTa('TIMOLESTE', 7, 3, 2021, 10, 4, 2022, 'PRECTOTCORR')
#         dataThang = thongKeTheoThang(df, datathang_set.country_PT, datathang_set.Day_Start, datathang_set.Month_Start, datathang_set.Year_Start, datathang_set.Day_End, datathang_set.Month_End, datathang_set.Year_End, datathang_set.Type_PT)

#         dataThang = dataThang[['COUNTRY', 'DATE', datathang_set.Type_PT]]
#         dataThang # dataframe cần in ra

#         #lấy min, max, trung bình
#         set_GiaTri(dataThang, datathang_set.Type_PT)

#         #Nếu dùng dataframe thì ko cần xuất file csv-> bỏ dòng này cũng được
#         export_file_csv= dataThang.to_csv('dataThang.csv', index = None, header=True)





























