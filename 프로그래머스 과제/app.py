from flask import Flask, jsonify, request

app = Flask(__name__)


menus = [
    {"id" : 1, "name" : "Espresso", "price" : 3800},
    {"id" : 2, "name" : "Americano", "price" : 4100},
    {"id" : 3, "name" : "CaffeLatte", "price" : 4600},

]



@app.route('/')
def hello_flask():
    return "Hello World!"

@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

@app.route('/menus', methods=['POST'])
def create_menu():
    request_date = request.get_json()
    new_menu = {
        "id" : 4,
        "name" : request_date['name'],
        "price" : request_date['price'],   
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods=['PUT'])
def update_menus(id):
    update_data = request.get_json()
    try:
        menus[id-1]["name"] = update_data['name']
        menus[id-1]["price"] = update_data['price']
        return jsonify(menus[id-1])
    except Exception as ex:
        print(ex)
        return jsonify({'error' : "해당 자료가 존재하지 않습니다."})
        

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menus(id):
    try:
        del menus[id-1]
        return jsonify(menus)
    except Exception as ex:
        print(ex)
        return jsonify({'error' : "해당 자료가 존재하지 않습니다."})


if __name__ == '__main__':
    app.run()