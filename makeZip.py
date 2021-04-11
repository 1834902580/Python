import zipfile

print('Zip started')

zip_file = zipfile.ZipFile('make.zip', 'w')
zip_file.write('make.txt', compress_type=zipfile.ZIP_DEFLATED)

zip_file.close()

print('Done')