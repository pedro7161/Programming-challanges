#fazer tipo a barra de pesquisa do google onde estou na pagina  10(current_page) a amostrar 5 ha volta(5 6 7 8 9)(around) e mostrar as 2 ultimas 1 2 e 99 100(boundaries) num total de 100 paginas
import time
start=time.time()
pagination = {
        "current_page":10,
        "total_pages":100,
        "boundaries":2,
        "around":1,
        }

def boundaries(pagination,arr):
    last=pagination["total_pages"]-pagination["boundaries"]+1
    first=pagination["total_pages"]-pagination["total_pages"]+pagination["boundaries"]

    for i in range(last,pagination["total_pages"]+1):
        arr.append(i)
    for k in range(1,first+1):
        arr.insert(0,k)
    arr=sorted(arr)
    return arr
def around(pagination):
    arr=[]
    back = pagination["current_page"]-pagination["around"]
    front =pagination["current_page"]+pagination["around"]+1
    for i in range(back,pagination["current_page"]):
        arr.append(i)
    for k in range(pagination["current_page"],front):
        arr.append(k)
    return boundaries(pagination,arr)
if pagination["around"]>pagination["total_pages"] or pagination["boundaries"]>pagination["total_pages"]:
    print("o around ou o boundaries é maior que as paginas")
if pagination["current_page"]>pagination["total_pages"]:
    print("o current page é maior que as paginas")
else:
    print(around(pagination))
stop=time.time()
print(stop-start)