import requests,openpyxl
from bs4 import BeautifulSoup

wb=openpyxl.Workbook()
sheet=wb.active

sheet.title='resort_info'

'''
sheet['A1']='景点名'
sheet['B1']='地址'
sheet['C1']='基本信息'
'''

resort_info_list=[]

#获取所有景点的网址
link_list=[]

for i in range(1,50):

    url='https://chs.meet-in-shanghai.net/travel-city/tourist-attraction.php?page=%d'%(i)
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
        }
    res=requests.get(url,headers=headers)
    
    soup=BeautifulSoup(res.text,'html.parser')

    main_div=soup.find('div',class_='piclist')

    main_list=main_div.find_all('a')

    for a in main_list:
        link_list.append(a['href'])

for r in link_list:
    sheet.append([r])

wb.save('test.xlsx')

'''
#遍历所有景点并爬取名称、地址、基本信息三要素      
for link in link_list:
    url_sub=link
    res_sub=requests.get(url_sub,headers=headers)
    res_sub.encoding = 'utf-8' 
    soup_sub_site=BeautifulSoup(res_sub.text,'html.parser')
    #景点名
    name=soup_sub_site.find(class_='p_site_name').text
    #地址
    address=soup_sub_site.find(class_='p_site_name3').text
    #基本信息，第一个class_='p_site_txt'
    info=soup_sub_site.find(class_='p_site_txt').text

    #三要素打包成一个列表，添加到景区信息大列表
    row=[name,address,info]
    resort_info_list.append(row)

for r in resort_info_list:
        sheet.append(r)

wb.save('上海旅游景点一览.xlsx')'''


    
