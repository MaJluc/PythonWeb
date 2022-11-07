import sys
#import pathlib
import os
import asyncio

from aiopath import AsyncPath
from time import time


def normalize(name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()       
    b = ""
    a = name.translate(TRANS)
    for i in a:
        if i.lower() not in "abcdefghijklmnopqrstuvwxyz" and i not in "0123456789":
            i = "_"
            b += i
        else:
            b += i

    return b


async def sort_files(path):
    if not os.path.exists(f'images'):
        os.mkdir(f'images')
    if not os.path.exists(f'video'):
        os.mkdir(f'video')
    if not os.path.exists(f'documents'):
        os.mkdir(f'documents')
    if not os.path.exists(f'archives'):
        os.mkdir(f'archives')
    if not os.path.exists(f'music'):
        os.mkdir(f'music')
    if not os.path.exists(f'else'):
        os.mkdir(f'else')
    if await path.is_dir():
        if len(os.listdir(path)) == 0:
            await path.rmdir()
        else:           
            async for element in path.iterdir():
                if element.name in ('video', 'documents', 'archives', 'music', 'images'):
                    pass               
                else:
                    await sort_files(element)
    else: 
        new_file_name = normalize(path.stem)
        if path.suffix.upper() in ('.JPEG', '.PNG', '.JPG', '.SVG'): 
            os.replace(path, f'.\\images\\{new_file_name}{path.suffix}')
        if path.suffix.upper() in ('.AVI', '.MP4', '.MOV', '.MKV'): 
            os.replace(path, f'.\\video\\{new_file_name}{path.suffix}')
        if path.suffix.upper() in ('.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'): 
            os.replace(path, f'.\\documents\\{new_file_name}{path.suffix}')
        if path.suffix.upper() in ('.MP3', '.OGG', '.WAV', '.AMR'): 
            os.replace(path, f'.\\music\\{new_file_name}{path.suffix}')
        if path.suffix.upper() in ('.ZIP', '.GZ', '.TAR'):
            os.replace(path, f'.\\archives\\{new_file_name}{path.suffix}')
        if path.suffix.upper() not in ('.ZIP', '.GZ', '.TAR', '.JPEG', '.PNG', '.JPG', '.SVG', '.AVI', '.MP4', '.MOV', '.MKV', '.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX', '.MP3', '.OGG', '.WAV', '.AMR'):
            os.replace(path, f'.\\else\\{new_file_name}{path.suffix}')

     
async def main():
    #path = r'D:\Pyton\p-web\hw6\Новая папка'
    path = sys.argv[1]
    #path = pathlib.Path(path)
    path = AsyncPath(path)
    while os.path.exists(path):
        await sort_files(path)



if __name__ == '__main__':
    start = time()
    asyncio.run(main())
    a = time() - start
print(round(a, 3), 'sec')
