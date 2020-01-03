import connexion
import hiyapyco

options = {"swagger_ui": True}  # turn off ui
connex_app = connexion.FlaskApp(__name__, specification_dir='swagger-doc/', options=options)


swagger_file = hiyapyco.load(
    [
        # main
        'swagger-doc/main.yaml',
        'swagger-doc/auth.yaml',
        'swagger-doc/upload.yaml',

        # swagger-doc
        'swagger-doc/user.yaml',
        'swagger-doc/account.yaml',
        'swagger-doc/product.yaml',
        'swagger-doc/type_member.yaml',
        'swagger-doc/bill.yaml',
        'swagger-doc/bill_detail.yaml',
        'swagger-doc/money_to_point.yaml',
        'swagger-doc/point_to_money.yaml',
        'swagger-doc/extract_point.yaml',
        'swagger-doc/cart.yaml',
        'swagger-doc/my_order.yaml',

    ],
    method=hiyapyco.METHOD_MERGE
)
swagger_file_dumped = hiyapyco.dump(swagger_file)
