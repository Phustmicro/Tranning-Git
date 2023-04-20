# call the class in main.py
from Person import Person

import picoscope as pc
def main():
    obj = Person("Le Quang Phu", 38)
    obj.greet()
if __name__ == "__main__":
    main()
