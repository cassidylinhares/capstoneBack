# A list of the microservice routes and APIs
# IoT device routes

thermostat = {
    'base': "http://192.168.0.140",
    'getTemp': "/getTemp",
    'setTemp': "/setTemp?temp="
}

lights = {
    'room1': "http://192.168.0.141",
    'room2': "http://192.168.0.145",
    'room3': "http://192.168.0.142",
    'room4': "http://192.168.0.144",
    'getLight': "/getLight",
    'setLight': "/setLight?status="
}