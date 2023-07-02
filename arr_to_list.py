import requests as rq

url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'

response = rq.get(f"{url}")
arr = response.text.split('\n')[:-1]
arr_res = [arr[x].replace(' ','').split('|')[1:-1] for x in range(len(arr)) if x%2 !=0]

def get_matrix(url: str) -> list[int]:
    result_list = []
    r = col = 0
    l_row = len(url)


    while l_row > 0:
        for row in range(l_row):
            result_list.append(int(url[row+r][col+r]))
        for col in range(l_row-1):
            result_list.append(int(url[row+r][col+1+r]))
        for row in range(l_row-1, 0, -1):
            result_list.append(int(url[row-1+r][col+1+r]))
        for col in range(l_row-2, 0, -1):
            result_list.append(int(url[row-1+r][col+r]))
        col = 0
        r +=1
        l_row -=2
    
    return result_list

print(get_matrix(arr_res))

