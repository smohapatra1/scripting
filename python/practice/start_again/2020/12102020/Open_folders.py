#Open folders subfolders files 
import os 
main_path = "/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/12102020"
os.getcwd()
for folders,subfolders,files in os.walk(main_path):    
    print (f"Currently looking at Folder {folders}")
    print ('\n')
    #print ("The subfolders are : ")
    for sub_fold in subfolders:
        print (f"\t Looking subfolder at {sub_fold}")
        print ('\n')
        #print ("Files are : ")
      
    for f in files:
        print (f"\t Looking at files : {f}")
        print ('\n')
        #print ("Files are : ")