# call the class in main.py
from Person import Person
import picoscope as pc
def main():
    obj = Person("abc xyz")
    obj.greet()

if __name__ == "__main__":
    main()
