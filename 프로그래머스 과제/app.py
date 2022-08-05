from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

@app.route('/')
def hello_flask():
    return "Hello World!"

#menus 자료를 가지고 옴
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# menus 자료를 자원에 추가
@app.route('/menus', methods = ['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = {
        "id" : 4,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonfy(new_menu)
    
if __name__ == '__main__':
    app.run()
    