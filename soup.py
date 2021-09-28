# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from hiturl import BeautifulSoup
import selenium
import pandas as pd


def Get_soup(soup,li):
    
    # print(li.get('href').split('/')[2])
    url_id=li.get('href').split('/')[2]
    header=soup.find('header',{'class':'h15ky94r'})
    title=header.find('h1',{'class':'agrq4zn'})
    # print("TItleee",title.text)
    try:
            
        author=header.find('span',{'class':'awkz85g'}).text
        # print("Authorrrrrrr",author)
    except:
        author=("NA")    
    source=header.find('div',{'class':'d1slxp1m'})
    # print(source.text)
    time=header.find('div',{'class':'t1wtd119'})
    # print(time.text)
    section=soup.find('article',{'class':'c3dczqn h15il40k'})

    desc=section.find_all('p')
    

    desc_list=[]
    for d in desc:
        # print(d.text)
        # print(d)
        desc_list.append(d.text)
    
    images_links=section.find_all('img')
    img=[]
    if images_links:
        for i in images_links:
            # print(i)
            img.append(i.get('src'))
    else:
        img.append("None")
    # print(desc_list)
    external_links=soup.find('a',{'id':'reader.external-link.view-original'})
    # print(external_links.get('href'))
    tags=soup.find_all('button',{'class':'p1mk9fki'})
    tag_list=[]
    for i in tags:
        # print(i.text)
        tag_list.append(i.text)
    try:
        favorit=soup.find('button',{'aria-label':'Remove from Favorites'})
        if favorit:
            yes=("Yes")
        else:
            yes=("No")    
    except:
        pass   
    
   #####################    hightlightd       ##########################3


    highlighted_list_with_hyperlink=[]
    text_list=[]
    anchor_list=[]

    for idc, d in enumerate(desc):
            # print()
            span=d.find_all('span',{'class':'highlight'})
            for h in span:
                try:
                    if d.find('a',{'target':'_blank'}).find('span',{'class':'highlight'}).text in h.text:
                        highlighted_list_with_hyperlink.append(h.text.replace(d.find('a',{'target':'_blank'}).find('span',{'class':'highlight'}).text,"[["+d.find('a',{'target':'_blank'}).get('href')+" ,"+'display'+'='+d.find('a').text+"]]"))
                        # print(h.text.replace(d.find('a',{'target':'_blank'}).find('span',{'class':'highlight'}).text,"[["+d.find('a',{'target':'_blank'}).get('href')+" ,"+'display'+'='+d.find('a').text+"]]"))
                    else:                                                                                                                                                    
                         highlighted_list_with_hyperlink.append(h.text)

                        # print(h.text)    
                except:
                    pass 
    
          

    new_list=[]
    # print(highlighted_list_with_hyperlink)

    # for i in highlighted_list_with_hyperlink:
    # for i in highlighted_list_with_hyperlink:
    #     if ',' in i :
    #         (highlighted_list_with_hyperlink.remove(','))

    # print(highlighted_list_with_hyperlink)





            
    hightlighted=soup.find_all('button',{'class':'b5bt6fr q32pgmz'})
    hightlighted_list=[]
    if hightlighted:
        for h in hightlighted:
            hightlighted_list.append(h.text)
            # print(h.text)
    else:
        hightlighted_list.append('You haven’t highlighted anything yet')
        # print('You haven’t highlighted anything yet')

    hyperlinks=section.find_all('a',{'target':'_blank'}) 
    hyperlink=[]
    hyperlink_text=[]



    if hyperlinks:
        
        for h in hyperlinks:
            # print(h.text)
            # print(h.get('href'))
            hyperlink.append(h.get('href'))
            hyperlink_text.append(h.text)
    else:
        hyperlink.append('None')
        hyperlink_text.append('None')
    desc=section.find_all('p')
  

    # print(hyperlink_text)
    desc_list_with_hyperlink=[]
    def test(d):
       
                    if '<a' in str(d):
                      
                        desc_list_with_hyperlink.append(d.text.replace(d.find('a').text,"[["+d.find('a').get('href')+"  "+" ,"+'display'+'='+d.find('a').text+"]]"))    
                        # print(d.text.replace(d.find('a').text,d.find('a').get('href')+"  "+" ,"+'display'+'='+d.find('a').text))
                       
                    else:
                        
                        # print(idc,"ddddddddddd",d.text)    
                        desc_list_with_hyperlink.append(d.text)    

    for idc, d in enumerate( desc):
        test(d)
                           
    # print("llllllllllllllllllllllllllllllllllllllllll",desc_list_with_hyperlink)
            
#######################      creating csv              ####################

    c1=pd.Series(data=url_id,name="url_id")
    c2=pd.Series(data=[title.text],name="Title")
    c3=pd.Series(data=[author],name="Author")
    c4=pd.Series(data=[source.text],name="Source")
    c5=pd.Series(data=[time.text],name="Time")
    c6=pd.Series(data=[desc_list],name="Description")
    c7=pd.Series(data=[desc_list_with_hyperlink],name="Description")
    
    c8=pd.Series(data=[img],name="Image")

    c9=pd.Series(data=[external_links.get('href')],name="URL")
    c10=pd.Series(data=str(tag_list),name="URL")


    c11=pd.Series(data=yes,name="Favorited")
   
    c12=pd.Series(data=[hightlighted_list],name="Highlight")
    if len(highlighted_list_with_hyperlink)>0:
        c13=pd.Series(data=[highlighted_list_with_hyperlink],name="Highlight")

    else:
        c13=pd.Series(data=[highlighted_list_with_hyperlink],name="Highlight")



    
    
    
    data= pd.concat([c1, c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13], axis=1)
    
        
    data_frame=pd.DataFrame(data)
    data_frame.to_csv('output2.csv',index=False,mode='a',header=False, sep =',')    
    tag_list.clear()
    desc_list.clear()    
    img.clear()
    hightlighted_list.clear()
    hyperlink.clear()
    hyperlink_text.clear()
    desc_list_with_hyperlink.clear()
    highlighted_list_with_hyperlink.clear()
    new_list.clear()