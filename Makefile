SHELL=/bin/bash
all: venv
	@if [[ -e "requirements.txt" ]]; then source venv/bin/activate && pip install -r requirements.txt; fi
	@echo
	@echo 'To activate virtualenv:'
	@echo 'source venv/bin/activate'
	@echo

venv:
	@virtualenv venv

clean:
	$(RM) -r venv
