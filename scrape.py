from bs4 import BeautifulSoup
import requests
import smtplib

URL='https://www.flipkart.com/asian-bouncer-01-running-shoes-boys-sports-men-latest-stylish-casual-sneakers-lace-up-lightweight-black-running-walking-gym-trekking-hiking-party/p/itm911b8bb86db5f?pid=SHOGY3G4RB4MTYKP&lid=LSTSHOGY3G4RB4MTYKP4INTBB&marketplace=FLIPKART&sattr[]=color&sattr[]=size&st=size'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}


def check_prices():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    price=soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
    conv_prices=int(price[1:])
    print(conv_prices)
    if(conv_prices<650):
        send_mail()

def send_mail():
    
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.set_debuglevel(1)
        server.starttls()
        server.ehlo()
        server.login('tulasihariharan@gmail.com','###########')
    
        subject="Price fall down!!!"
        body='https://www.flipkart.com/asian-bouncer-01-running-shoes-boys-sports-men-latest-stylish-casual-sneakers-lace-up-lightweight-black-running-walking-gym-trekking-hiking-party/p/itm911b8bb86db5f?pid=SHOGY3G4RB4MTYKP&lid=LSTSHOGY3G4RB4MTYKP4INTBB&marketplace=FLIPKART&sattr[]=color&sattr[]=size&st=size'
    
        msg=f"Subject:{subject}\n\n{body}"
    
        server.sendmail('tulasihariharan@gmail.com','20euec055@skcet.ac.in',msg)
    
        print("Hey email has been sent!")
    
    except Exception as e:
    # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
    
    
check_prices()
