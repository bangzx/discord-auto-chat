import requests
import random
import time
import os
from datetime import datetime
from colorama import Fore, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = pyfiglet.figlet_format("Auto Bot", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.WHITE + "=" * 50)
    print(Fore.CYAN + "Discord Auto Chat")
    print(Fore.CYAN + "Telegram: https://t.me/airdropfetchofficial")
    print(Fore.WHITE + "=" * 50 + "\n")

def log_message(message, status="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color = {
        "TIME": Fore.LIGHTRED_EX,
        "SUKSES": Fore.GREEN,
        "ERROR": Fore.RED,
        "WARNING": Fore.YELLOW
    }.get(status, Fore.WHITE)
    
    print(f"{Fore.BLUE}[{timestamp}] {color}[{status}] {message}")

def main():
    clear_screen()
    print_banner()
    
    # Input Channel ID dan Token dari user
    channel_id = input(Fore.CYAN + "Enter your Channel ID: ")
    authorization = input(Fore.CYAN + "Enter your Token: ")
    
    # Set delay otomatis
    send_delay_min = 50  # Atur sesuai kebutuhan
    send_delay_max = 60  # Atur sesuai kebutuhan
    
    clear_screen()
    print_banner()
    
    # Read messages
    try:
        with open("pesan.txt", "r", encoding='utf-8') as f:
            words = f.readlines()
    except FileNotFoundError as e:
        log_message(f"File not found: {str(e)}", "ERROR")
        return
    
    # Main loop
    while True:
        try:
            # Send message
            payload = {
                'content': random.choice(words).strip()
            }
            headers = {
                'Authorization': authorization
            }
            
            r = requests.post(
                f"https://discord.com/api/v9/channels/{channel_id}/messages",
                data=payload,
                headers=headers
            )
            
            if r.status_code == 200:
                log_message(f"Kirim Pesan ID: {channel_id}: {payload['content']}", "SUKSES")
            else:
                log_message(f"Gagal kirim pesan: {r.status_code} - {r.text}", "ERROR")
            
            # Random delay before next message
            delay = random.uniform(send_delay_min, send_delay_max)
            log_message(f"Tunggu {delay:.1f} detik sebelum pesan berikutnya", "TIME")
            time.sleep(delay)
            
        except Exception as e:
            log_message(f"An error occurred: {str(e)}", "ERROR")
            time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log_message("\nSTOP SCRIPT")
