.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y treasurebot || :
	@pip install -e .

run_api:
	uvicorn treasurebot.api.main:app --reload

run_app:
	streamlit run treasurebot/web_interface/app.py
