# API

This CRUD-API

## Installation

### Setup

-   create a new project and clone it to your computer with `git clone`.
-   navigate your terminal into the project folder and create a python virtual environment `python -m venv venv`
-   activate the virtual environment `source ./venv/bin/activate`
-   install all the dependencies from the requirements.txt `pip install -r requirements.txt`
-   update the requirements.txt if you install more libraries use the following command `pip freeze > requirements.txt`

## Documentation

Documentation is available at:
`www.azureapi.cloud/docs`

## Get VM ready

Run the following command to connect to your VM via terminal:
`ssh -i ~/<Path to .pem>/azure-FastAPI_key.pem azureuser@pubIP`

If you're successfully connected run the following commands to update the linux VM
`sudo apt update && sudo apt upgrade -y` 

Check if Python3 is installed
`python3 --version`

Install pip
`sudo apt install python3-pip`

Install virtualenv
`sudo pip3 install virtualenv`

Install Postgresql
`sudo apt install postgresql postgresql-contrib -y`

Login as postgres
`sudo -i -u postgres`

Setup password for postgres-user
`\password postgres`
now type the password and after successful setup type `\q` to exit the user

## FAQ

## Known Bugs

-   None so far

## License

This project is licensed under the terms of the MIT license.