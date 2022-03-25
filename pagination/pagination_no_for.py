#fazer tipo a barra de pesquisa do google onde estou na pagina  10(current_page) a amostrar 5 ha volta(5 6 7 8 9)(around) e mostrar as 2 ultimas 1 2 e 99 100(boundaries) num total de 100 paginas
import time
start=time.time()
pagination = {
        "current_page":10,
        "total_pages":100,
        "boundaries":2,
        "around":1,
        }
def insert():
    list1=[0]
 
    list1.extend(pagination["total_pages"])
    print(list1)
    # print(len(list1)<pagination["total_pages"])
    # print(len(list1)," ",pagination["total_pages"])
    # print(list1)
    # if len(list1)<pagination["total_pages"]:
    #     x=x+1
    #     print(x)
    #     insert(x)
        
    # else:
    #     return list1

def searchbar():
    list2=[]
    # list2.append(insert())
    insert()
    print(list2)
    return list2

print(searchbar())
stop=time.time()
print(stop-start)