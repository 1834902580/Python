import zipfile

print('UnZip started')

uzip_file = zipfile.ZipFile('make.zip', 'r')
uzip_file.extractall('file.txt')

print('Done')