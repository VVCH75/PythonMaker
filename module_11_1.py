from PIL import Image
import numpy as np
import requests


with Image.open('1234567.webp') as im:
    im.rotate(180).show()

r = requests.post('https://app.epn.bz/test/user-info')

if r.status_code == 403:
    print('Информация о пользователе недоступна')

a = np.array([[5, 2, 4],
              [6, 1, 3]])
print(a.shape)

b = np.sort(a)
print(b)

