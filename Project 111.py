import os
import shutil

from_dir = "C:\\Users\\user\\Downloads"
to_dir = "C:\\Users\\user\\Documents"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    print(os.path.splitext(i))

'''
['.opera', '1.mp4', '16.11.22.xlsx', '2.mp4', '20221004_234232.jpg', '3.mp4', '360_F_296805389_ECzruLwPETAklaOnJKIEEolIrgoIPM9T.jpg', '4.mp4', ...] (#contined)

('.opera', '')
('1', '.mp4')
('16.11.22', '.xlsx')
('2', '.mp4')
('20221004_234232', '.jpg')
('3', '.mp4')
('360_F_296805389_ECzruLwPETAklaOnJKIEEolIrgoIPM9T', '.jpg')
('4', '.mp4')
... (#continued)
'''