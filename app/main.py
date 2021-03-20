import connexion
from connexion.decorators.security import validate_scope
from connexion.exceptions import OAuthScopeProblem


def basic_auth(username, password, required_scopes=None):
    if username == 'sap' and password == 'secret':
        info = {'sub': 'admin', 'scope': ''}
    else:
        # optional: raise exception for custom error response
        return None

    # optional
    if required_scopes is not None and not validate_scope(required_scopes, info['scope']):
        raise OAuthScopeProblem(
                description="Provided user doesn't have the required access rights",
                required_scopes=required_scopes,
                token_scopes=info['scope']
            )

    return info


#app = connexion.FlaskApp(__name__, specification_dir='.', server='tornado')
app = connexion.FlaskApp(__name__, specification_dir='.')
app.add_api('swagger.yaml')
print(app.app.__dict__)
app.run(port=8080)
