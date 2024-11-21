.PHONY: init

init:
	touch text.txt
	python3 -m venv .venv 
	. .venv/bin/activate && \
	python3 -m pip install boto3 pdfplumber && \
	python3 upload.py
