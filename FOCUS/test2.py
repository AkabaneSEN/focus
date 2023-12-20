import cfscrape
import requests
from bs4 import BeautifulSoup
import data as data_
import time
import fileread
from datetime import datetime

def run():  
        
        content = ""

        TransacObject = []
        currentTransaction = []

        transacData = []
        tokenData = []
        tmpArray = []

        url = "https://etherscan.io/tx/0x299e2a1a95b45e648f2ec78bd2ef16ed50d1867c261b31307bcd33b417408582"

        scraper = cfscrape.create_scraper()
        response = scraper.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        isSucces = soup.find(class_="badge bg-success bg-opacity-10 border border-success border-opacity-25 text-green-600 fw-medium text-start text-wrap py-1.5 px-2")
        if isSucces:
                nbTransac = soup.find(class_="d-flex flex-column gap-3 overflow-y-auto scrollbar-custom")
                
                if nbTransac:
                        
                            data = nbTransac.find_all(class_="me-1")
                            token = nbTransac.find_all("a")
                            for info in data:
                                transacData.append(str(info.text.strip()))

                            for tokens in token:
                                tokenAdr = tokens["href"]
                                tokenName = tokens.text
                                if tokenAdr.startswith("/token/0x"):
                                    tmpArray.append(tokenAdr[7:49])
                                    tmpArray.append(tokenName)

                            tokenData = [tmpArray[i:i+2] for i in range(0, len(tmpArray), 2)]

                for elements in transacData:
                    if elements.startswith("("):
                        transacData.remove(elements)
                
                for elements in transacData:
                    if elements == "":
                        transacData.remove(elements)
                
                

                allTransaction = [transacData[i:i+2] for i in range(0, len(transacData), 2)]
                if allTransaction != []:
                    
                    
                    for transacFromAllTransaction in allTransaction:
                        currentTransaction.clear()

                        firstCoin = data_.Coin(None, None, None, None, None, None, None)
                        secondCoin = data_.Coin(None, None, None, None, None, None, None)

                        for info in transacFromAllTransaction:
                            currentTransaction.append(info)
                        print(currentTransaction)
                

run()