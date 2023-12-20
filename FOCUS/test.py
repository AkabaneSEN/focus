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

        url = "https://arbiscan.io/tx/0xdc3e90043bc5483293a61caa19c80a331c75ddc00ef5d3c32cb15fc3bd790a74"

        scraper = cfscrape.create_scraper()
        response = scraper.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        isSucces = soup.find(class_="badge bg-success bg-opacity-10 border border-success border-opacity-25 text-green-600 fw-medium text-start text-wrap py-1.5 px-2")

        if True:
                
                nbTransac = soup.find(id="wrapperContent")
                
                if nbTransac:
                            data = nbTransac.find_all(class_="mr-1")
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
                    if elements == "":
                        transacData.remove(elements)
                    

                allTransaction = [transacData[i:i+8] for i in range(0, len(transacData), 8)]
                if allTransaction != []:
                    
                    
                    for transacFromAllTransaction in allTransaction:
                        currentTransaction.clear()

                        firstCoin = data_.Coin(None, None, None, None, None, None, None)
                        secondCoin = data_.Coin(None, None, None, None, None, None, None)

                        for info in transacFromAllTransaction:
                            currentTransaction.append(info)
                            print(info)

                        print(currentTransaction, tokenData)

run()