from main import db, create_app

app = create_app()
app.app_context().push()

try:
	db.drop_all()
except Exception as e:
	print(e)

try:
	db.create_all()
except Exception as e:
	print(e)