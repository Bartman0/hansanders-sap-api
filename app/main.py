import connexion

app = connexion.FlaskApp(__name__, specification_dir='.', server='tornado')
#app = connexion.FlaskApp(__name__, specification_dir='.')
app.add_api('swagger.yaml')
print(app.app.__dict__)
app.run(port=8080)
