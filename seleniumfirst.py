from selenium import webdriver
from time import sleep
import random

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
email = []
fullName = []
username = []
Password = ('Macan123')

def dot_trick(username):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@gmail.com")
    return emails
resultdottrick = random.choice(dot_trick('boostmedia0'))
email.append(resultdottrick)

def generatornama():
    global nomor1
    global username1
    global nama
    first = ['Anisa' , 'Ainin' , 'Atika', 'Arda' , 'Adriana' , 'Alice' , 'Afifah' , 'Adelia' , 'Azni' , 'Azula' , 'Adelle' , 'Abigail' , 'Adena' , 'Audora' , 'Anindita' , 'Anindira', 'Arumi', 'Azka' , 'Ayudha', 'Azhar' , 'Anggi' , 'Azizah' , 'Ananda', 'Asyifa' , 'ALine', 'Albertina', 'Alifah' , 'Alifia' , 'Alivia' , 'Aline' , 'Atiqa' , 'Atiqah', 'Askanah' , 'Afiqa' , 'Anggun' 'Aaurora' , 'Audora' , 'Adsila' , 'Afsheen' , 'Ardilah' , 'Atikah' , 'Agata' , 'Adonia' , 'Aulia', 'Alya' , 'Adele' , 'Arum' , 'Bunga' ,'Bilqis' , 'Belinda' , 'Bella' , 'Briliant' , 'Badriyah', 'Bunga' , 'Cahya' , 'Alessandra' , 'Adela' , 'Alicia' , 'Citra' , 'Dela' , 'Dwi' , 'Dewi'  , 'Diah' , 'Diyahana' , 'Dian' , 'Daliyah' , 'Daniyah' , 'Dariah', 'Eka' , 'Elok' , 'Erina' , 'Ertika' , 'Eshal' , 'Ezzah' , 'Fitria' , 'Fatinah' , 'Fatimah' , 'Fithrya' , 'Fitriyani' , 'Fitri', 'Fitriyyah' , 'Fijriyah' , 'Farah' , 'Fadhila' , 'Fadila' , 'Fadhilah' , 'Fadwa', 'Fadwah', 'Fakiha' , 'Faiha' , 'Faimah' , 'Fiderya' , 'Gemi' , 'Gurtina' , 'Hanifah' , 'Harum' , 'Hilya' , 'Husniah' , 'Husna' , 'Hana', 'Husniah' , 'Hafsah' ,'Hafsa' , 'Haurah' , 'Hadziqa' , 'Haura' , 'Isytihar' , 'Izzah' , 'Irene' , 'Indah' , 'Intan' , 'Inten' , 'Jamilah' , 'Jamiah' , 'Jauharah' , 'Jazima' , 'Jasmin' , 'Jaudah' , 'Jahidah' , 'Jihan' , 'Jizah' , 'Juhaina' , 'Juhhaira' , 'Khansa' , 'Khadziya' , 'Kamala' , 'Kamila' , 'Kamilla' , 'Khamilah' , 'kamilatunisa' , 'Kamuning' , 'Keisha' , 'Keisya' , 'Lia' , 'Lailah' , 'Lamiah' , 'Latifah' , 'Laila' , 'Legi' , 'Lestari' , 'Layanah' , 'Lulu' , 'Lala', 'Layanah', 'Layyan' , 'Maharani' , 'Marshanda' , 'Mawar' , 'Melati' , 'Mega' , 'Mentari' , 'Mariah' , 'Mariam' , 'Murni' , 'Mustika' , 'Nurul' , 'Nur' , 'Nasya' , 'Nafisah' , 'Nijihab' , 'Naimah' , 'Nazina' , 'Nisrina' , 'Najwa' , 'Nikmah' , 'Nimra' , 'Nismah' , 'Nurani' , 'Nujannah' , 'Nuwairah' , 'Nuzhah' , 'Nabila' , 'Ndari' , 'Ningrum' , 'Ningsih' , 'Nisrina' , 'Omaira' , 'Oadira' , 'Okta' , 'Oaisara' , 'Putri' , 'Permata' , 'Pertiwi' , 'Prameswari' , 'Puspita' , 'Rara' , 'Rahmah' , 'Rahma' , 'Ratih' , 'Ratu' , 'Rani' , 'Rina' , 'Sarah' , 'Sarwedah' , 'Setiawati' , 'Siti' , 'Syauqia' , 'Susil' , 'Tsabita' , 'Tsabira' , 'Talia' , 'Talita' , 'Tania' , 'Ufaira' , 'Ulfa' , 'Ulfi' ,  'Wangi' , 'Wening' , 'Wulan' , 'Wulandari' , 'Yuni' , 'Yasmin' , 'Zaenab' , 'Zahwa']
    second = ['Anisa' , 'Ainin' , 'Atika', 'Arda' , 'Adriana' , 'Alice' , 'Afifah' , 'Adelia' , 'Azni' , 'Azula' , 'Adelle' , 'Abigail' , 'Adena' , 'Audora' , 'Anindita' , 'Anindira', 'Arumi', 'Azka' , 'Ayudha', 'Azhar' , 'Anggi' , 'Azizah' , 'Ananda', 'Asyifa' , 'ALine', 'Albertina', 'Alifah' , 'Alifia' , 'Alivia' , 'Aline' , 'Atiqa' , 'Atiqah', 'Askanah' , 'Afiqa' , 'Anggun' 'Aaurora' , 'Audora' , 'Adsila' , 'Afsheen' , 'Ardilah' , 'Atikah' , 'Agata' , 'Adonia' , 'Aulia', 'Alya' , 'Adele' , 'Arum' , 'Bunga' ,'Bilqis' , 'Belinda' , 'Bella' , 'Briliant' , 'Badriyah', 'Bunga' , 'Cahya' , 'Alessandra' , 'Adela' , 'Alicia' , 'Citra' , 'Dela' , 'Dwi' , 'Dewi'  , 'Diah' , 'Diyahana' , 'Dian' , 'Daliyah' , 'Daniyah' , 'Dariah', 'Eka' , 'Elok' , 'Erina' , 'Ertika' , 'Eshal' , 'Ezzah' , 'Fitria' , 'Fatinah' , 'Fatimah' , 'Fithrya' , 'Fitriyani' , 'Fitri', 'Fitriyyah' , 'Fijriyah' , 'Farah' , 'Fadhila' , 'Fadila' , 'Fadhilah' , 'Fadwa', 'Fadwah', 'Fakiha' , 'Faiha' , 'Faimah' , 'Fiderya' , 'Gemi' , 'Gurtina' , 'Hanifah' , 'Harum' , 'Hilya' , 'Husniah' , 'Husna' , 'Hana', 'Husniah' , 'Hafsah' ,'Hafsa' , 'Haurah' , 'Hadziqa' , 'Haura' , 'Isytihar' , 'Izzah' , 'Irene' , 'Indah' , 'Intan' , 'Inten' , 'Jamilah' , 'Jamiah' , 'Jauharah' , 'Jazima' , 'Jasmin' , 'Jaudah' , 'Jahidah' , 'Jihan' , 'Jizah' , 'Juhaina' , 'Juhhaira' , 'Khansa' , 'Khadziya' , 'Kamala' , 'Kamila' , 'Kamilla' , 'Khamilah' , 'kamilatunisa' , 'Kamuning' , 'Keisha' , 'Keisya' , 'Lia' , 'Lailah' , 'Lamiah' , 'Latifah' , 'Laila' , 'Legi' , 'Lestari' , 'Layanah' , 'Lulu' , 'Lala', 'Layanah', 'Layyan' , 'Maharani' , 'Marshanda' , 'Mawar' , 'Melati' , 'Mega' , 'Mentari' , 'Mariah' , 'Mariam' , 'Murni' , 'Mustika' , 'Nurul' , 'Nur' , 'Nasya' , 'Nafisah' , 'Nijihab' , 'Naimah' , 'Nazina' , 'Nisrina' , 'Najwa' , 'Nikmah' , 'Nimra' , 'Nismah' , 'Nurani' , 'Nujannah' , 'Nuwairah' , 'Nuzhah' , 'Nabila' , 'Ndari' , 'Ningrum' , 'Ningsih' , 'Nisrina' , 'Omaira' , 'Oadira' , 'Okta' , 'Oaisara' , 'Putri' , 'Permata' , 'Pertiwi' , 'Prameswari' , 'Puspita' , 'Rara' , 'Rahmah' , 'Rahma' , 'Ratih' , 'Ratu' , 'Rani' , 'Rina' , 'Sarah' , 'Sarwedah' , 'Setiawati' , 'Siti' , 'Syauqia' , 'Susil' , 'Tsabita' , 'Tsabira' , 'Talia' , 'Talita' , 'Tania' , 'Ufaira' , 'Ulfa' , 'Ulfi' ,  'Wangi' , 'Wening' , 'Wulan' , 'Wulandari' , 'Yuni' , 'Yasmin' , 'Zaenab' , 'Zahwa']
    penyambung = ['_' , '.']
    nomor = list(range(0, 100))
    nomor1 = random.choice(nomor)
    penyambung1 = random.choice(penyambung)
    first1 = random.choice(first)
    seccond = random.choice(second)
    username1 =  (first1 + penyambung1 + seccond + str(nomor1))
    nama =str (first1 + " " + seccond)
generatornama()
fullName.append(nama)
username.append(username1)

def daftar():
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    sleep(8) #tunggu aja bos
    driver.find_element_by_name('emailOrPhone').send_keys(email)
    driver.find_element_by_name('fullName').send_keys(fullName)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(Password)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click();
daftar()


