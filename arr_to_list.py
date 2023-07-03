import asyncio
from aiohttp import ClientSession

def start(url):
    return asyncio.run(get_matrix(url))

try:
    async def get_matrix(url: str) -> list[int]:
        async with ClientSession() as session:
            async with session.get(url=url) as response:
                arr = await response.text()
                return matrix_to_list(arr)
except Exception as e:
    print (e)

def matrix_to_list(arr:str) -> list[int]:
    mat = [arr.split('\n')[:-1][x].replace(' ','').split('|')[1:-1] for x in range(
        len(arr.split('\n')[:-1])) if x%2 !=0]
    result_list = []
    r = col = 0
    l_row = len(mat)

    while l_row > 0:
        for row in range(l_row):
            result_list.append(int(mat[row+r][col+r]))
        for col in range(l_row-1):
            result_list.append(int(mat[row+r][col+1+r]))
        for row in range(l_row-1, 0, -1):
            result_list.append(int(mat[row-1+r][col+1+r]))
        for col in range(l_row-2, 0, -1):
            result_list.append(int(mat[row-1+r][col+r]))
        col = 0
        r +=1
        l_row -=2
    
    return result_list