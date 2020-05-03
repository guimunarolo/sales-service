import datetime
import uuid

import factory
from sales_service.db import session
from sales_service.models import Order, Seller


class SellerFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.LazyAttribute(lambda obj: str(uuid.uuid4()))
    name = factory.Faker("name")
    cpf = factory.Faker("ssn", locale="pt_BR")
    email = factory.Faker("email")
    password = factory.Faker("password")

    class Meta:
        model = Seller
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "flush"


class OrderFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.LazyAttribute(lambda obj: str(uuid.uuid4()))
    code = factory.Sequence(lambda n: f"COD0{n}")
    amount = 150.0
    timestamp = datetime.datetime.now()
    cpf = factory.Faker("ssn", locale="pt_BR")

    class Meta:
        model = Order
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "flush"
