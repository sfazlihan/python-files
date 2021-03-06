import os, shutil, cv2, numpy
shutil.copy("C:\\Users\\sfazl\\Desktop\\Fazlıhan\\ben.jpg","C:\\Users\\sfazl\\Desktop\\Test\\ben.jpg")
os.chdir("C:\\Users\\sfazl\\Desktop\\Test\\")
ben = cv2.imread("ben.jpg")
for f in range(500):
    cv2.imwrite("{f}.jpg".format(f=f),ben)
cv2.waitKey(0)
cv2.destroyAllWindows()