from models import *


@app.route("/users", methods=["GET", "POST"])
def get_all_users():
    if request.method == "GET":
        user_list = []
        for user in User.query.all():
            user_list.append(user.create_dict())
        return json.dumps(user_list)
    elif request.method == "POST":
        user_data = json.loads(request.data)
        new_user = User(
            id=user_data.get("id"),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            age=user_data.get("age"),
            email=user_data.get("email"),
            role=user_data.get("role"),
            phone=user_data.get("phone")
        )
        db.session.add(new_user)
        db.session.commit()
        return "Пользователь добавлен"

@app.route("/users/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_id(id):
    if request.method == "GET":
        return json.dumps(User.query.get(id).create_dict())
    elif request.method == "DELETE":
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return "Пользователь удален"

    elif request.method == "PUT":
        user_data = json.loads(request.data)
        update_user = User.query.get(id)
        update_user.first_name = user_data.get("first_name")
        update_user.last_name = user_data.get("last_name")
        update_user.age = user_data.get("age")
        update_user.email = user_data.get("email")
        update_user.role = user_data.get("role")
        update_user.phone = user_data.get("phone")

        db.session.add(update_user)
        db.session.commit()
        return "Данные пользователя обновленны"



@app.route("/orders", methods=['GET', 'POST'])
def get_all_orders():
    if request.method == "GET":
        order_list = []
        for order in Order.query.all():
            order_list.append(order.create_dict())
        return json.dumps(order_list, ensure_ascii=False)
    elif request.method == "POST":
        order_data = json.loads(request.data)
        new_order = Order(
            id=order_data.get("id"),
            name=order_data.get("name"),
            description=order_data.get("description"),
            start_date=order_data.get("start_date"),
            end_date=order_data.get("end_date"),
            address=order_data.get("address"),
            price=order_data.get("price"),
            customer_id=order_data.get("customer_id"),
            executor_id=order_data.get("executor_id")
        )
        db.session.add(new_order)
        db.session.commit()
        return "Заказ добавлен"

@app.route("/orders/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_order_id(id):
    if request.method == "GET":
        return json.dumps(Order.query.get(id).create_dict(), ensure_ascii=False)
    elif request.method == "DELETE":
        order = Order.query.get(id)
        db.session.delete(order)
        db.session.commit()
        return "Заказ удален"
    elif request.method == "PUT":
        order_data = json.loads(request.data)
        update_order = Order.quest.get(id)
        update_order.name=order_data.get("name")
        update_order.description=order_data.get("description")
        update_order.start_date=order_data.get("start_date")
        update_order.end_date=order_data.get("end_date")
        update_order.address=order_data.get("address")
        update_order.price=order_data.get("price")
        update_order.customer_id=order_data.get("customer_id")
        update_order.executor_id=order_data.get("executor_id")

        db.session.add(update_order)
        db.session.commit()
        return "Данные заказа обновлены"



@app.route("/offers", methods=['GET', 'POST'])
def get_all_offers():
    if request.method == "GET":
        offer_list = []
        for offer in Offer.query.all():
            offer_list.append(offer.create_dict())
        return json.dumps(offer_list, ensure_ascii=False)
    elif request.method == "POST":
        offers_data = json.loads(request.data)
        new_offer = Offer(
            id=offers_data.get("id"),
            order_id=offers_data.get("order_id"),
            executor_id=offers_data.get("executor_id")
        )

        db.session.add(new_offer)
        db.session.commit()
        return "Предложение добавлено"

@app.route("/offers/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_id(id):
    if request.method == "GET":
        return json.dumps(Order.query.get(id).create_dict(), ensure_ascii=False)
    elif request.method == "DELETE":
        offer = Offer.query.get(id)
        db.session.delete(offer)
        db.session.commit()
        return "Предложение удалено"
    elif request.method == "PUT":
        offer_data = json.loads(request.data)
        update_offer = Offer.query.get(id)
        update_offer.order_id=offer_data.get("order_id")
        update_offer.executor_id=offer_data.get("executor_id")

        db.session.add(update_offer)
        db.session.commit()
        return "Предложение обновлено"


if __name__ == "__main__":
    app.run(port=4777)