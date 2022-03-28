# A list of the microservice routes and APIs
# IoT device routes

thermostat = {
    'base': "http://192.168.129.142",
    'getTemp': "/getTemp",
    'setTemp': "/setTemp?temp="
}

lights = {
    'room1': "http://192.168.16.52",
    'room2': "http://192.168.16.52",
    'room3': "http://192.168.16.52",
    'room4': "http://192.168.16.52",
    'getLight': "/getLight",
    'setLight': "/setLight?status="
}
