import os
import shutil
import zipfile

print(os.getcwd())
print(os.listdir())

# shutil.move("DemoOs/one/hello.txt", "DemoOs/two/")
# shutil.move("DemoOs/two/hello.txt", "DemoOs/one/")

newFile = open("DemoOs/one/debb.txt", "w+")
newFile.write("Hay, debb file")
newFile.close()

newCompress = zipfile.ZipFile("DemoOs/one/debb.zip", "w")
newCompress.write("DemoOs/One/debb.txt", compress_type=zipfile.ZIP_DEFLATED)
newCompress.write("DemoOs/One/hello.txt", compress_type=zipfile.ZIP_DEFLATED)
newCompress.close()

newExtract = zipfile.ZipFile("DemoOs/one/debb.zip", "r")
newExtract.extractall("DemoOs/Extract")
newExtract.close()
