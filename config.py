

class DevelopConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://admin:123456@127.0.0.1:3306/ad5_test1'

class TestConfig():
    DEBUG = False


class ProductConfig():
    DEBUG = False


contest_config = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig,
}
