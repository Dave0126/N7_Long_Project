PROJECT_HOME=$(shell pwd)
PY=python
PY3=python3
PYUI=pyuic5

show:
	echo "- Project Direction: $(PROJECT_HOME)"

demo:
	$(PY3) src/frontend/main.py

clean:
	rm -f data/temp/customAreas/*.json
	rm -f data/temp/customLines/*.json

ui:
	$(PYUI) -o src/frontend/mainWidget.py src/frontend/UI/mainWidget.ui
	$(PYUI) -o src/frontend/editWidget.py src/frontend/UI/editWidget.ui
	$(PYUI) -o src/frontend/editAreaWidget.py src/frontend/UI/editAreaWidget.ui
	$(PYUI) -o src/frontend/simulation1Widget.py src/frontend/UI/simulation1Widget.ui
	$(PYUI) -o src/frontend/mainWindow.py src/frontend/UI/mainWindow.ui
