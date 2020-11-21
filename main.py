import subprocess

# HEHE IT'S TOO CHALLENGING
# BRING ME A CUP OF COFFEE FOR BEGADANG TONIGHT
# SCRIPT BY AFI ISKANDAR == ANANDA FIKRI IJLAL AKBAR == CLONEWRITER == 19.83.0431
# UNCH UNCH USAHA YANG BERFAEDAH WALAU BELUM SEPENUHNYA SEMPURNA :))

mangAdmin = ("Admin","adminnet","PacMan")
admOpt = ("[1] Data Pegawai\n[2] Data Transaksi\n[3] Tambah Data Pegawai\n[4] Hapus Data Pegawai\n[5] Keluar")
mangUser = [{'username' : '19.83.0431', 'pass' : '123', 'nama' : 'Afi'},
            {'username' : '18.83.1234', 'pass' : '123', 'nama' : 'Zaki'},
            {'username' : '18.83.2345', 'pass' : '123', 'nama' : 'Diah'}]
usrOpt = ("[1] Transaksi\n[2] Lihat Transaksi\n[3] Ubah Password\n[4] Keluar")
transaksi = []

def clear():
    subprocess.call("clear") #for linux
    # subprocess.call("cls") #for windows

clear()
# passwd = input("Password : ")

while True:
    def login():
        #loginPage
        print(" .: ", " "*9,"PSYCHO NET"," "*9, " :. ")
        print("-"*40)
        print(" "*14,"Login Page")
        print("="*40)
        uname = input("username : ")
        password = input("password : ")

        #Admin True Detection
        if uname == (mangAdmin[0]):
            if password == (mangAdmin[1]):
                print("\n>>> login berhasil")
                input("--continue--")
                clear()
            else:
                clear()
                print("password salah")
                login()
        
        elif uname !=(mangAdmin[0]):
        #klo cuma sekedar User, disini lapaknya Om
            for i, data in enumerate(mangUser):
                # Just for dividing among data and index to m4K3 1t 3zy
                if data['username'] == uname and data['pass'] == password:
                    signin = True
                    print("\n>>> login berhasil")
                    input("--continue--")

                    # Main Operation of user make me dagdigdug serrrr

                    while signin == True:
                        def usrInt():
                            print("="*40)
                            print(" "*14,"HELLO", data['nama'].upper())
                            print("="*40)
                        clear()
                        usrInt()
                        print(usrOpt)
                        usrChoice = input("> ")

                        #For shopping and burning money eyeyeyeyeyey
                        if usrChoice == "1":
                            clear()
                            print("TRANSAKSI")
                            data_1 = input("Username : ")
                            start = str(input("input the started time (hh.mm)\t: "))
                            end = str(input("input the ended time (hh.mm)\t: "))
                            print("-"*50)
                            pricePerTime = 500
                            pricePerHour = 3000

                            #intinya ini berdua buat biar mereka gak pacaran, makanya di split
                            is_accstart = str(start).split(".")
                            is_accend = str(end).split(".")
                            #Nah klo ini buat konsep perhitungan 60 menit aja sih, biar gak terbang kemana mana angkanya
                            is_retTimStart = int(is_accstart[0]) * 60 + int(is_accstart[1])
                            is_retTimEnd = int(is_accend[0]) * 60 + int(is_accend[1])
                            #Klo ini buat pengurangan
                            is_negatime = int(is_retTimEnd - is_retTimStart)
                            #ini buat nge float in data di is_negatime aja, diambil 2 angka belakang koma
                            is_est = float("{:.2f}".format(is_negatime))
                            is_estConv = int(is_est)
                            #dahlah, ini ngitung buat yang multiple price aja, liat di elif pertama, dipake tuch, unCH unCH
                            is_tenMult = int((is_estConv/10)*pricePerTime)
                            if is_retTimEnd > is_retTimStart:
                                #klo kurang dari 10 menit
                                if is_estConv >0 and is_estConv < 10:
                                    price=str(pricePerTime)
                                    print("Total Price\t\t\t: " + price)
                                #klo ini interval kurang dari sejam lebih dari 10 menit
                                elif is_estConv >= 10 and is_estConv < 60:
                                    price = str(is_tenMult)
                                    print("Total Price\t\t\t: " + price)
                                #Sejam murah sayyy
                                elif is_estConv == 60:
                                    price =str(pricePerHour)
                                    print( "Total Price\t\t\t: " + price)
                                # c# w# {# 3z# _# t0# _# f1nD# _# m3h# _# 4t # _# disKonan # _# W4rN3t # }
                                elif is_estConv > 60:
                                    price = str(((pricePerHour)+int(float("%.2g" % (((is_negatime%60)/10)*pricePerTime)))))
                                    print("Total Price\t\t\t: " + price)
                                else:
                                    exit()
                            transaksi.append({'data_1':data_1, 'waktu_mulai':start, 'selesai':end, 'total menit':is_estConv, 'bayar':price})
                            print(transaksi)
                            input("--back--")
                        
                        #Now_u_C_m3h
                        if usrChoice == "2":
                            clear()
                            print("LIHAT TRANSAKSI")
                            print("|\tpc\t|\tmulai\t|\tselesai\t|\ttotal menit\t|\tbayar\t|")
                            print("="*90)
                            for i in transaksi:
                                print(i["data_1"],"\t\t",i["waktu_mulai"],"\t\t",i["selesai"],"\t"*2, i["total menit"],"\t\t    ",i["bayar"])
                                input("--back--")

                        #u can access me to change pwd wow
                        if usrChoice == "3":
                            clear()
                            print("UBAH PASSWORD")
                            ganti = input("Masukkan password lama: ")
                            if ganti == password:
                                passNew = input("Masukkan pasword baru: ")
                                data['pass'] = passNew
                                clear()
                                print("PASSWORD HAS BEEN CHANGED")
                                print()
                            
                                input("--continue--")
                                clear()
                        
                        #well, I wanna go out
                        if usrChoice == "4":
                            ask = input("wanna quit (Y/N)? ")
                            if ask == "Y" or ask =="y":
                                clear()
                                exit()
                            elif ask == "N" or ask == "n":
                                clear()
                                login()
                    else:
                        pass #gataw ini buat apa, biar cantik aja sih :v nge pass doang
            #for anonymous user, reinput plz                
            else:
                print(" "*5,">>> user tidak tersedia <<<\n")
                print("-"*15, "RE-INPUT", "-"*15)
                login()
                print("\n")
            clear()

        #admin unyu mohon jangan salah user yaw
        else:
            print(" "*5,">>> user tidak tersedia <<<\n")
            print("-"*15, "RE-INPUT", "-"*15)
            login()
            print("\n")

        #mamang is in the house yo    
        while uname == (mangAdmin[0]):
            def admInt():
                print("="*40)
                print(" "*14,"HELLO", mangAdmin[2].upper())
                print("="*40)
                print(admOpt)

            admInt()
            admChoice = input("> ")
            
            #nge stalking in pegawai is the ninja way of aku
            if admChoice == "1":
                clear()
                print("="*70)
                print(" "*30,"Data Pegawai")
                print("="*70)
                print("|\tUSERNAME\t|\tPASSWORD\t|\tNAME\t  |")
                print("="*70)
                khusuzonAdmin = "\t" + mangAdmin[0] + "\t\t\t" +mangAdmin[1] + "\t\t" + mangAdmin[2]
                print(khusuzonAdmin)
                for us in mangUser:
                    print("\t" + us['username'] + "\t\t" + us['pass'] + "\t\t\t" + us['nama'])
                print("="*70, "\n")
                input("--continue--")
                clear()
            
            #oke data data nya kekmana aja, jangan sampe missing ntar rugi
            elif admChoice == "2":
                print("DATA TRANSAKSI")
                print("|\tpc\t|\tmulai\t|\tselesai\t|\ttotal menit\t|\tbayar\t|")
                print("="*90)
                for i in transaksi:
                    print(i["data_1"],"\t\t",i["waktu_mulai"],"\t\t",i["selesai"],"\t"*2, i["total menit"],"\t\t    ",i["bayar"])
                print("="*90, "\n")
                input("--continue--")
                clear()

            #nambah data aja, gamau update, tak ingin mengganti secara perlahan
            elif admChoice == "3":
                clear()
                print("TAMBAH DATA PEGAWAI")
                print("="*19)
                userAdd = input("Masukkan user      : ")
                passAdd = input("Masukkan password  : ")
                nameAdd = input("Masukkan nama      : ")
                mangUser.append({'username':userAdd,'pass':passAdd,'nama':nameAdd})
                clear()
                print("Berhasil menambah data pegawai")
                print("username     :",userAdd,"\npassword     :",passAdd,"\nname         :",nameAdd)
                input("--continue--")
                clear()

            #no change, but deleted it is better
            elif admChoice == "4":
                clear()
                print("HAPUS DATA PEGAWAI")
                print("="*19)
                khusuzonAdmin = "\t" + mangAdmin[0] + "\t\t\t" +mangAdmin[1] + "\t\t" + mangAdmin[2]    
                print(khusuzonAdmin)
                for index, us in enumerate(mangUser):
                    print(index, "\t" + us['username'] + "\t\t" + us['pass'] + "\t\t\t" + us['nama'])
                print("="*70, "\n")

                mangUser.pop(int(input("Choose one : ")))
                clear()
                print("\nDELETING USER SUCCESSFULLY")
                input("--continue--")
                clear()

            #Min, pulang Min, dah malem
            elif admChoice == "5":
                ask = input("wanna quit (Y/N)? ")
                if ask == "Y" or ask =="y":
                    clear()
                    exit()
                elif ask == "N" or ask == "n":
                    clear()
                    login()
            else:
                pass


            
    #command execution is 2 3z
    login()