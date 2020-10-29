# Task-inventory-management-erpmax

An inventory management system using Flask

## Getting Started


## Clone this repository and set your path to it's folder, to get it up and running on your local system.

```
git clone https://github.com/abdullarayyan/Task-inventory-management-erpmax.git
cd Task-inventory-management-erpmax


To run this system you will need :

- Python 3
- Flask
- SQLALCHEMY
- WTForms

Assuming you have Python, proceed to install the rest using the command below:

```
pip3 install -r requirements.txt
```


## Running the app
1) Set your current path to where the cloned folder is and run the file **run.py**


2) Either copy paste the url as shown above into your browser **or** simply check into *localhost:5000/* as shown below. You will see the initial views of each page as no actions are performed.

## Features

### Adding Products and Locations
Products require product name and quantity to be filled. Location only requires location name


![adding product](https://github.com/abdullarayyan/Task-inventory-management-erpmax/blob/main/secreenshot/123292620_2742774802662239_7812100159452872729_n.png)
![adding location](https://github.com/abdullarayyan/Task-inventory-management-erpmax/blob/main/secreenshot/addlocation.png)


### manage Products and Locations


![product edit/delete](https://github.com/abdullarayyan/Task-inventory-management-erpmax/blob/main/secreenshot/manage%20product.png)
![location edit/delete](https://github.com/abdullarayyan/Task-inventory-management-erpmax/blob/main/secreenshot/123292620_2742774802662239_7812100159452872729_n.png)


### Moving products
Here products can be moved to a location, from a location as well as to and from a location. Products need to initially be added to various locations from the central warehouse.

![mvng](https://github.com/abdullarayyan/Task-inventory-management-erpmax/blob/main/secreenshot/movement%20product.png)

### OverView
Change in product or loaction name creates changes in their names in the history and system overview.So, you can rectify a spelling error and still not loose any data.


![Overview](https://github.com/abdullarayyan/Task-inventory-management-erpmax/blob/main/secreenshot/overview.png)


# Built using
- Flask
- SQLAlchemy

