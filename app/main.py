import os
import logging
from tornado.log import app_log, LogFormatter
import connexion
from connexion.decorators.security import validate_scope
from connexion.exceptions import OAuthScopeProblem


# use environment variable SAP_PASSWORD as the SAP password, if it exists
# otherwise, read the secret from the Docker 'sap_password' secret
sap_password = os.environ.get('SAP_PASSWORD')
if sap_password is None or sap_password == "":
    sap_password_fpath = f'/run/secrets/sap_password'
    sap_password = open(sap_password_fpath).read().rstrip('\n')


# customize logging
log_format = "%(asctime)s %(levelname)s %(name)s %(module)s %(funcName)s[%(lineno)d]: "
log_formatter = LogFormatter(fmt=log_format, datefmt="%Y-%m-%d %H:%M:%S", color=False)
root_logger = app_log.parent
root_logger.addHandler(logging.StreamHandler())
root_logger.handlers[0].setFormatter(log_formatter)
root_logger.handlers[0].setLevel(logging.INFO)


# basic authentication function, only knows about about a 'sap' user
def basic_auth(username, password, required_scopes=None):
    if username == 'sap' and password == sap_password:
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


# main program, start up connexion Flask app with tornado web server
app = connexion.FlaskApp(__name__, specification_dir='.', server='tornado')
#app = connexion.FlaskApp(__name__, specification_dir='.')
app.add_api('swagger.yaml')
app.run(port=8080)
