#Zip and unzip a file 
import zipfile
def main():
    f1 = open('file1.txt', 'w+')
    f1.write('samar one')
    f1.close()
    f2 = open('file2.txt', 'w+')
    f2.write('samar two')
    f2.close()
    #Now Zip Files 
    comp_file = zipfile.ZipFile('test.zip','w')
    comp_file.write('file1.txt',compress_type=zipfile.ZIP_DEFLATED)
    comp_file.write('file2.txt',compress_type=zipfile.ZIP_DEFLATED)
    comp_file.close()
if __name__ == "__main__":
    main()