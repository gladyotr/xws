from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

new_accs = []
with open('config.data', 'ab') as g:
        phone_number = str(input(f'\n{lg} [~] Telefon numarası giriniz: {r}'))
        parsed_number = ''.join(phone_number.split())
        pickle.dump([parsed_number], g)
        new_accs.append(parsed_number)
        print(f'\n{lg} [i] numara kaydedildi')
        clr()
        print(f'\n{lg} [*] Yeni kullanıcı oturum actı\n')
        for number in new_accs:
            c = TelegramClient(f'sessions/{number}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            c.start(number)
            print(f'{lg}[+] Giriş Başarılı')
            c.disconnect()