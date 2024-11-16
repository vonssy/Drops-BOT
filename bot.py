import requests
import json
import urllib.parse
import os
from datetime import datetime
import time
from colorama import *
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Drops:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'api.drops-tgcoin.com',
            'Origin': 'https://app.drops-tgcoin.com',
            'Pragma': 'no-cache',
            'Referer': 'https://app.drops-tgcoin.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Drops - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)
            first_name = user_data['first_name']
            return first_name
        else:
            raise ValueError("User data not found in query.")
        
    def sessions(self, query: str, retries=3):
        url = "https://api.drops-tgcoin.com/sessions"
        data = json.dumps({'encodedMessage':query})
        self.headers.update({ 
            'Content-Type': 'application/json'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url,headers=self.headers, data=data, timeout=10)
                if response.status_code == 200:
                    return response.json()['token']
                else:
                    return None
            except (requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
        
    def sign_up(self, token: str, retries=3):
        url = "https://api.drops-tgcoin.com/users/sign-up-rewards"
        self.headers.update({ 
            'Content-Type': 'application/json',
            'X-Auth-Token': token
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url,headers=self.headers, timeout=10)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
        
    def rewards(self, token: str, retries=3):
        url = "https://api.drops-tgcoin.com/drops/claim/rewards"
        self.headers.update({ 
            'Content-Type': 'application/json',
            'X-Auth-Token': token
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.get(url,headers=self.headers, timeout=10)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
        
    def claim_farming(self, token: str, retries=3):
        url = "https://api.drops-tgcoin.com/drops/claim/rewards"
        self.headers.update({ 
            'Content-Type': 'application/json',
            'X-Auth-Token': token
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url,headers=self.headers, timeout=10)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
        
    def tasks(self, token: str, retries=3):
        url = "https://api.drops-tgcoin.com/tasks"
        self.headers.update({ 
            'Content-Type': 'application/json',
            'X-Auth-Token': token
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.get(url,headers=self.headers, timeout=10)
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except (requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
        
    def verify_tasks(self, token: str, task_id: int, retries=3):
        url = f"https://api.drops-tgcoin.com/tasks/{task_id}/verify"
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Content-length': '0',
            'X-Auth-Token': token
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.get(url,headers=self.headers, timeout=10)
                if response.status_code in [200, 201]:
                    return True
                else:
                    return False
            except (requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
        
    def process_query(self, query: str):

        account = self.load_data(query)

        token = self.sessions(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Query Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {account}  {Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT}Isn't Valid{Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
            )
            return
        
        user = self.rewards(token)
        if not user:
            signup = self.sign_up(token)
            if signup:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {signup['user']['firstName']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {signup['user']['dropsAmount']:.2f} $DROPS {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            return

        if user:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {account} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user['dropsAmount']:.2f} $DROPS {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
        else:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT}  {Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT}Is None{Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
            )

        claim_farm = self.claim_farming(token)
        if claim_farm:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {claim_farm['changeAmount']:.2f} $DROPS {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
        else:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )

        tasks = self.tasks(token)
        if tasks:
            for task in tasks:
                task_id = task['id']

                if task and task['active']:
                    verify = self.verify_tasks(token, task_id)
                    if verify:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {task['rewardDrops']} $DROPS {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
        else:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                f"{Fore.YELLOW+Style.BRIGHT} Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                time.sleep(1)
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                
                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Drops - BOT.{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = Drops()
    bot.main()
