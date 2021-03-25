# Openfoodfacts Quality Food Generator

## **What does it do?**
This little program will help you replace bad quality food with better ones.
You will be able to choose between categories and products.
Once you have chose a product, a substitute will be generated.
The program is looking at the Nutri-Score of a product.
The better product will always have a better score than the one you chose.
All the informations are taken from the Openfoodfacts website.

## **Prerequesites**
1. Python must be installed on your computer
2. You have to create a virtual environment
3. MySQL must be installed on your computer
4. A MySQL database must be created under the name 'Openfoodfacts'
    
For the virtual environment you need to create:
* Windows: `py -3.8 -m venv env`
* Mac/Linux: `python3 -m venv env`
    
Then activate it: 
* Windows: `source venv\Scripts\activate`
* Mac/Linux: `source env/bin/activate`

Regarding the Openfoodfacts dependency: `pip3 install -r requirements.txt`

Then you can launch the program:
* Windows: `python main.py`
* Mac/Linux: `python3 main.py`

Enjoy!
