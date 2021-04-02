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
5. You need to put your database credentials in db-config.py

## **How to launch**
1. `pipenv install` (if virtual environment not already installed)
2. `python3 -m core.install`
3. `python3 main.py`

Enjoy!
