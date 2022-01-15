from common.models import Contact, Customer, User


def find_by_user(user: User):
    customer = Customer.query.filter_by(user_id=user.user_id).first()
    if customer:
        return Contact.query.filter_by(customer_id=customer.customer_id).first()
    