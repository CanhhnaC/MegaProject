from ftplib import FTP

host = input('Enter user host: ')
username = input('Enter username: ')
password = input('Enter password: ')

try:
    ftp = FTP(host)
    ftp.login(user=username, passwd=password)
except Exception:
    print(Exception)

print('Which one do you choose?\n1, Download a file.\n2, Uploading a file.')
choose = int(input('Choose: '))


if choose == 1:
    filename = input('type filename you download')
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ', filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

elif choose == 2:
    filename = input('type filename you uploade')
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

else:
    print('Error')
