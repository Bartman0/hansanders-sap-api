import os
import csv
from datetime import datetime
import threading
import connexion
from connexion import NoContent

DATA_DIR = "./data"

def put_articles():
	id = threading.get_ident()
	now = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"articles_{id}_{now}.csv"
	with open(os.path.join(DATA_DIR, filename), 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		body = connexion.request.json
		print(body)
		count = 0
		for row in body:
			print(list(row.keys()))
			if count == 0:
				writer.writerow(row.keys())
			writer.writerow(row.values())
	return NoContent, (200 if body is not None else 201)

def put_article_valuations():
	p = ''
	return NoContent, (200 if p is not None else 201)

def put_article_conditiontypes():
	p = ''
	return NoContent, (200 if p is not None else 201)

def put_article_preferred_suppliers():
	p = ''
	return NoContent, (200 if p is not None else 201)

def put_locations():
	p = ''
	return NoContent, (200 if p is not None else 201)

def put_receipts():
	p = ''
	return NoContent, (200 if p is not None else 201)

def put_stock_levels():
	p = ''
	return NoContent, (200 if p is not None else 201)

def put_stock_mutations():
	p = ''
	return NoContent, (200 if p is not None else 201)

def put_stockrooms():
	p = ''
	return NoContent, (200 if p is not None else 201)

def put_suppliers():
	p = ''
	return NoContent, (200 if p is not None else 201)

