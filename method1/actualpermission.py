"""
Written By : Manuel Antony
mail : manuel314ad@gmail.com
"""


#create a directory "apks" and put a apk there
#the program will read the apk from apks directory only
import os
import re

def listing_apks(path):
    return os.listdir(path)

#here apk will be decompiled
def decompile(apk_name,path):
    decompile_path = path + "/" + apk_name.replace(".apk", " ")
    apktool = "apktool d " + path + "/" + apk_name + " -o " + decompile_path
    os.system(apktool)
    return decompile_path

#here all the permissions will collect
def permission_listing(d_path):
    permissions = []
    d_path = re.sub(' $',"/",d_path)
    l_file = os.listdir(d_path)
    #print l_file
    found = 0
    for manifest_file in l_file:
        if manifest_file == "AndroidManifest.xml":
            found = 1
            print "<<<<<<<<<<<<<<< AndroidManifest.xml found >>>>>>>>>>>>>>>>>>"
            manifest_path = d_path+"/AndroidManifest.xml"
            #print manifest_path
            fp_manifest = open(manifest_path,"r")
            for lines in fp_manifest:
                if "<uses-permission android:name=" in lines:
                    lines = lines.split('"')[1::2];
                    for line in lines:
                        line = line.strip("android.permission.")
                        permissions.append(line)
    if found != 1:
        print "AndroidManifest.xml file not found"

    return permissions

def main():
    path = "./apks"      #/apks from current directory
    apk_list = listing_apks(path)
    #print apk_list

    for apk in apk_list:
        #print apk
        d_path = decompile(apk,path)

        permissions = permission_listing(d_path)

    print "Permissions :"
    for permission in permissions:
        print permission


if __name__ == "__main__":
    main()
