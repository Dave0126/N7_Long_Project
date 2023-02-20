PROJECT_HOME=$(shell pwd)
PY=python
PY3=python3

show:
	echo "- Project Direction: $(PROJECT_HOME)"

demo:
	$(PY3) src/frontend/main.py

clean:
	rm -f data/temp/customAreas/*.json
	rm -f data/temp/customLines/*.json