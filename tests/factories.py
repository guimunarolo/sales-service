import uuid

import factory
from sales_service.db import session
from sales_service.models import Seller


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
