# capstoneBack
The api for the mobile, web, and nodeMCUs. Will also be the host of the ML system.

## API
### `/getLights`
Gets all the data on the Lights

### `/getLight/yyyy-mm-ddThh:MM:ssZ`
Gets the data on the lights from that specific time stamp  
Eg: `/getItem/2021-08-22T21:09:00Z`

### `/insertLight`
The body to submit is as follows:   
```
{ 
  "name":"light1", 
  "status": 0, 
  "time": 2021-08-22T21:09:00Z
}  
```
Inserts a document below is an example of what the data will look like in the db:   
```
"2021-08-22T21:09:00Z": { 
    "name":"light1", 
    "status": 0, 
    "time": 2021-08-22T21:09:00Z
}  
```

## Prerequisites
- Make sure you have python 3 installed
- Make sure you have python 3 pip installed
- 
## Set Up
1. Clone this repository
2. Open the repository in VS Code
3. `Ctrl+ tilde` to open a new terminal or command prompt in VS Code
4. Start a Virtual Environment by following [these steps](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial)
5. Install all the python requirements by running `pip install -r requirements.txt`
6. To set up Firebase: 
    1. Ask Cassidy for the private key
    3. Store the key in the `capstoneBack` directory or the same location as the README.
    4. Add the key to your Systems Path
    5. If this doesn't work, generate a new key from the firebase console

## To Run
1. Open the terminal in VS Code
2. From the capstoneBack Folder `cd capstoneApp` and then run `python manage.py runserver` to run on localhost or `python manage.py runserver ip_addr` to run a given ip address
