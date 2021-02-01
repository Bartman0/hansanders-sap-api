import os
import csv
from datetime import datetime
import threading
import connexion
from connexion import NoContent
import inspect


# base directory where to put data
DATA_DIR = "./data"


def put_bundle():
	# bundle name is the name of the function of the caller of the function that triggered this one,
	# without the first part before the first '_' character
	# so with this stack, caller1() -> do_caller2() -> put_bundle(), "do_caller2" will be returned
	bundle_name = (inspect.stack()[1][3]).split("_", 1)[1]
	# get the thread identifier to keep bundles apart that are written to in different threads
	id = threading.get_ident()
	now = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"{bundle_name}_{id}_{now}.csv"
	directory = os.path.join(DATA_DIR, bundle_name)
	if not os.path.exists(directory):
		os.makedirs(directory)
	with open(os.path.join(directory, filename), 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		body = connexion.request.json
		print(body)
		count = 0
		for row in body:
			print(list(row.keys()))
			if count == 0:
				writer.writerow(row.keys())
			writer.writerow(row.values())
			count += 1
	return NoContent, 201


def put_articles():
	return put_bundle()


# def put_articles():
# 	id = threading.get_ident()
# 	now = datetime.now().strftime("%Y%m%d_%H%M%S")
# 	filename = f"articles_{id}_{now}.csv"
# 	with open(os.path.join(DATA_DIR, filename), 'w', newline='') as csvfile:
# 		writer = csv.writer(csvfile)
# 		body = connexion.request.json
# 		print(body)
# 		count = 0
# 		for row in body:
# 			print(list(row.keys()))
# 			if count == 0:
# 				writer.writerow(row.keys())
# 			writer.writerow(row.values())
# 			count += 1
# 	return NoContent, 201


def put_article_valuations():
	return NoContent, 201


def put_article_conditiontypes():
	return NoContent, 201


def put_article_preferred_suppliers():
	return NoContent, 201


def put_locations():
	return NoContent, 201


def put_receipts():
	return NoContent, 201


def put_stock_levels():
	return NoContent, 201


def put_stock_mutations():
	return NoContent, 201


def put_stockrooms():
	return NoContent, 201


def put_suppliers():
	return NoContent, 201
