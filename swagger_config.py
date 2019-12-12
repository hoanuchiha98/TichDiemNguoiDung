import connexion
import hiyapyco

options = {"swagger_ui": True}  # turn off ui
connex_app = connexion.FlaskApp(__name__, specification_dir='swagger-doc/', options=options)


swagger_file = hiyapyco.load(
    [
        # main
        'swagger-doc/main.yaml',
        'swagger-doc/auth.yaml',

        # swagger-doc
        'swagger-doc/user.yaml',
        'swagger-doc/account.yaml'
    ],
    method=hiyapyco.METHOD_MERGE
)
swagger_file_dumped = hiyapyco.dump(swagger_file)
