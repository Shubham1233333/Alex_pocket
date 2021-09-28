a=['https://www.animaapp.com/', ',', 'which was bootstrapped until last year, ', 'https://techcrunch.com/2020/10/27/animas-latest-update-draws-on-the-popularity-of-design-and-no-code-tools/', '.']
# new_list = [elem for elem in a if elem.strip()]
# print(new_list)
new_list=[]
for i in a:
    if ',' in i :
        print(a.remove(','))
       

#     else:
#         print(i)    
#         new_list.append(i)
# print(new_list)   
print(a) 
