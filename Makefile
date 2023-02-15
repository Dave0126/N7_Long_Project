PROJECT_HOME=$(shell pwd)
PY=python
PY3=python3

show:
	echo "- Project Direction: $(PROJECT_HOME)"

demo:
	$(PY3) src/frontend/callWindow.py

clean:
	rm data/temp/customAreas/*.js
	rm data/temp/customLines/*.js