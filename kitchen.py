import subprocess
import os
import glob

class kitchen:
    subprocess.run("color 02", shell=True)
    subprocess.run("cls", shell=True)

    title_home = ("Welcome to Mellow's Kitchen").center(60)
    print("\n\n",title_home)

    if not os.path.exists('Place'):
        os.mkdir('Place')

    if not os.path.exists('Work'):
        os.mkdir('Work')

    if not os.path.exists('Out'):
        os.mkdir('Out')

    print("\n\nHome")
    input_home = 0

    while input_home != 4:
        print("\n1- Extract Zip \n2- Dat.br to dat conversion \n3- Clean Out Folder \n4- Exit")
        input_home = int(input("\nEnter an option to Perform: "))

        if input_home ==1:
            #subprocess.call("extract_new.py", shell=True)
            extract_zip

        elif input_home ==2:
            convert_dat()

        elif input_home==3:
            subprocess.run("rd /s /q Out", shell=True)
            os.mkdir("Out")
            subprocess.call("home.py", shell=True)

        elif input_home==4:
            raise SystemExit()
        else:
            print("Invalid Choice")
    
    def extract_zip():
        path = os.getcwd()
        zip_path = path+("\Place")

        zipfiles=[]
        for file in glob.glob("Place\*.zip"):
            zipfiles.append(file)
            
        input_home = 0

        while input_home!=2:

            #Title
            title_extract = ("\n\nExtractor by Mellow").center(60)
            print(title_extract)
            display_options_home = ("\n1- Extract Zip \n2- Back to home").center(24)
            print(display_options_home)
            input_home = int(input("\nEnter a option to Perform: "))

            if input_home == 1:
                if len(zipfiles)==0:
                    print("\nNo zip found")
                else:
                    for x in range(len(zipfiles)):
                        print("\n",x,"-",zipfiles[x])
                    input_a = int(input("\nEnter an option to extract the zip: "))
            
                    cmd1 = zipfiles[input_a]+' '+'-o'+ path+'\\Out'
                    cmd2 = 'tools\\7z.exe'+' '+'x'+' '+cmd1
                    execute_cmd = subprocess.run(cmd2, shell=True)
                    subprocess.run("cls", shell=True)
                    print("\n\n\nExtracted to "+path+"\\Out")
            elif input_home == 2:
                subprocess.call("home.py", shell=True)

    def convert_dat():
        # Initializing Commands
        s_de = ("tools\\brotli.exe --decompress --in Place\\system.new.dat.br --out Out\\system.new.dat")
        v_de = ("tools\\brotli.exe --decompress --in Place\\vendor.new.dat.br --out Out\\vendor.new.dat")

        s_com = ("tools\\brotli.exe --in Place\\system.new.dat --out Out\\system.new.dat.br -f -q5")
        v_com = ("tools\\brotli.exe --in Place\\vendor.new.dat --out Out\\vendor.new.dat.br -f -q5")

        a = 0
        while a!=4:

            subprocess.run("cls", shell=True)
            print("\nBrotli Convertor by Gautham")
            
            # Input Home
            a = int(input("\n\n1. Compress to dat.br \n2. Decompress to dat \n3. Clean Out Folder \n4. Back to Home\n\nInput:- "))

            # 1. Compress to dat.br
            if (a==1):
                c = int(input("\n\n1. Convert System.new.dat to System.new.dat.br \n2. Convert Vendor.new.dat to Vendor.new.dat.br \n3. Both System and Vendor \n4. Back\n\nInput:- "))

                # Converting System
                if (c==1):
                    if os.path.isfile('Out/system.new.dat.br'):
                        print("\nDelete or Move the Existing files from Out Directory")
                        while input("Press Enter to continue..."):
                                break
                    else:
                        if os.path.isfile('Place/system.new.dat'):
                            print("\nConverting to System.new.dat.br ...")
                            print("\nCompression may take time depends on cpu")
                            subprocess.run(s_com, shell=True)
                            print("\nConversion Completed")
                            while input("Press Enter to continue..."):
                                break
                        else:
                            print("\n File not Found")
                            while input("Press Enter to continue..."):
                                break
                            
                # Converting Vendor
                elif(c==2):
                    if os.path.isfile('Out/vendor.new.dat.br'):
                        print("Delete or Move the Existing files from Out Directory")
                        while input("Press Enter to continue..."):
                                break
                    else:
                        if os.path.isfile('Place/vendor.new.dat'):
                            print("\nConverting to Vendor.new.dat.br ...")
                            print("\nCompression may take time depends on cpu")
                            subprocess.run(v_com, shell=True)
                            print("\nConversion Completed")
                            while input("Press Enter to continue..."):
                                break
                        else:
                            print("\nFile not Found")
                            while input("Press Enter to continue..."):
                                break

                # Converting Both
                elif(c==3):
                    if os.path.isfile('Out/system.new.dat.br') | os.path.isfile('Out/vendor.new.dat.br'):
                        print("Delete or Move the Existing files from Out Directory")
                        while input("Press Enter to continue..."):
                                break
                    else:
                        if os.path.isfile('Place/system.new.dat') & os.path.isfile('Place/vendor.new.dat'):
                            print("\nConverting Both System and Vendor...")
                            print("\nCompression may take time depends on cpu")
                            subprocess.run(v_com, shell=True)
                            print("\nWIP Dont Exit...")
                            subprocess.run(s_com, shell=True)
                            print("\nConversion Completed")
                            while input("Press Enter to continue..."):
                                break
                        else:
                            print("\nFiles not Found")
                            while input("Press Enter to continue..."):
                                break
                elif(c==4):
                    continue


            # 2. DeCompress to dat.br
            elif (a==2):
            
                # Input Conversions
                b = int(input("\n\n1. Convert System.new.dat.br to System.new.dat \n2. Convert Vendor.new.dat.br to Vendor.new.dat \n3. Both System and Vendor \n4. Back\n\nInput:- "))
            
                # Converting System
                if (b==1):
                    if os.path.isfile('Out/system.new.dat'):
                        print("\nDelete or Move the Existing files from Out Directory")
                        while input("Press Enter to continue..."):
                                break
                    else:
                        if os.path.isfile('Place/system.new.dat.br'):
                            print("\nConverting to System.new.dat ...")
                            subprocess.run(s_de, shell=True)
                            print("\nConversion Completed")
                            while input("Press Enter to continue..."):
                                break
                        else:
                            print("\n File not Found")
                            while input("Press Enter to continue..."):
                                break

                # Converting Vendor
                elif(b==2):
                    if os.path.isfile('Out/vendor.new.dat'):
                        print("Delete or Move the Existing files from Out Directory")
                        while input("Press Enter to continue..."):
                                break
                    else:
                        if os.path.isfile('Place/vendor.new.dat.br'):
                            print("\nConverting to Vendor.new.dat ...")
                            subprocess.run(v_de, shell=True)
                            print("\nConversion Completed")
                            while input("Press Enter to continue..."):
                                break
                        else:
                            print("\nFile not Found")
                            while input("Press Enter to continue..."):
                                break

                # Converting Both
                elif(b==3):
                    if os.path.isfile('Out/system.new.dat') | os.path.isfile('Out/vendor.new.dat'):
                        print("Delete or Move the Existing files from Out Directory")
                        while input("Press Enter to continue..."):
                                break
                    else:
                        if os.path.isfile('Place/system.new.dat.br') & os.path.isfile('Place/vendor.new.dat.br'):
                            print("\nConverting Both System and Vendor...")
                            subprocess.run(v, shell=True)
                            print("\nWIP Dont Exit...")
                            subprocess.run(s, shell=True)
                            print("\nConversion Completed")
                            while input("Press Enter to continue..."):
                                break
                        else:
                            print("\nFiles not Found")
                            while input("Press Enter to continue..."):
                                break

                elif(c==4):
                    continue                    


            # 3. Clean Out Folder
            elif(a==3):
                subprocess.run("rd /s /q Out", shell=True)
                os.mkdir("Out")

            # 4. Exit
            elif(a==4):
                subprocess.call("home.py", shell=True)

            else:
                print("\nInvalid Choice")
        
        
