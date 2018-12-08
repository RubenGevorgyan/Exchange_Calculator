from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if (is_good_response(resp)):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()

    return (resp.status_code == 200

            and content_type is not None

            and content_type.find('html') > -1)
def log_error(e):
    print(e)
class Exchanger:
    def __init__(self):
        self.__link = simple_get('https://www.cba.am/am/SitePages/default.aspx')
        self.__html = BeautifulSoup(self.__link, 'html.parser')
        self.__position=0
        self.__usd=self.__creator__()
        self.__gbp=self.__creator__()
        self.__eur = self.__creator__()
        self.__rub = self.__creator__()


    def __creator__(self):
        list = LinkedList()
        if (self.__position==0):
            self.__position = self.__html.find("em", {"class": "w_50"})
            list.push(self.__position.text)
            for i in range(0, 2):
                self.__position = self.__position.findNext("em", {"class": "w_50"})
                list.push(self.__position.text)
        else:
            self.__position.findNext("em", {"class": "w_50"})
            for i in range(0, 3):
                self.__position = self.__position.findNext("em", {"class": "w_50"})
                list.push(self.__position.text)
        return list

    def converter(self,amount,currency):
        if (str(currency).lower()=="usd" ):
            return  float(amount/float(self.__usd.get_by_index(0)))
        if (str(currency).lower() =="gbp"):
            return  float(amount/float(self.__gbp.get_by_index(0)))
        if (str(currency).lower() =="eur"):
            return  float(amount/float(self.__eur.get_by_index(0)))
        if (str(currency).lower() =="rub"):
            return  float(amount/float(self.__rub.get_by_index(0)))


    def reverse_converter(self,amount,currency):
        if (str(currency).lower =="usd"):
            return  float(float(self.__usd.get_by_index(0))/amount)
        if (str(currency).lower() =="gbp"):
            return  float(float(self.__gbp.get_by_index(0))/amount)
        if (str(currency).lower() =="eur"):
            return  float(float(self.__eur.get_by_index(0))/amount)
            return  float(float(self.rub.get_by_index(0))/amount)


    def show_rates(self):
        print("AMD to "+self.__usd.get_by_index(2)+" is "+self.__usd.get_by_index(1)+" : "+self.__usd.get_by_index(0))
        print("AMD to "+ self.__gbp.get_by_index(2) + " is " + self.__gbp.get_by_index(1) + " : " + self.__gbp.get_by_index(0))
        print("AMD to " + self.__eur.get_by_index(2) + " is " + self.__eur.get_by_index(1) + " : " + self.__eur.get_by_index(0))
        print("AMD to " + self.__rub.get_by_index(2) + " is " + self.__rub.get_by_index(1) + " : " + self.__rub.get_by_index(0))

    def choicer(self,choice):
        if(choice==1):
            self.show_rates()
        elif(choice==2):
            money=int(input("How much money do yo want to convert?"))
            currency=input("To what currency do you want to convert?")
            print(self.converter(money,currency))
        elif(choice==3):
            money = int(input("How much money do yo want to convert?"))
            currency = input("From what currency do you want to convert?")
            print(self.reverse_converter(money,currency))



class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def get_by_index(self, index):
        current = self.head
        count = 0

        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
        return 0;

def main():
    change=Exchanger()
    print("HELLO DEAREST CUSTOMER!!!!" )
    choice=1
    while(choice):
        choice=int(input("\n\nOur great programm can provide you with this services \n "
              "1:Rates: Shows the current rates which are provided by Central Bank of Armenia \n"
              "2:Converter: Converts any amount of AMD to USD/GBP/EUR/RUB\n"
              "3:Reverse Converter: As you may guessed converts USD/GBP/EUR/RUB to AMD\n"
              "Please choose which one do you want by number shown at the left\n"
              "If you want to quit just enter 0\n"))
        change.choicer(choice)
main()