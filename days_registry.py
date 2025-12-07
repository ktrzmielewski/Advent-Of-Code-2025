import os
import importlib

NUM_OF_DAYS = 12
FINISHED_DAYS = {}

days_path = os.path.join(os.path.dirname(__file__), "days")

for entry in os.scandir(days_path):
    if entry.is_dir() and entry.name.startswith("day"):
        day_number = int(entry.name[3:])
        py_files = []

        for f in os.listdir(entry.path):
            if f.endswith(".py") and not f.startswith("__"):
                py_files.append(f)

        for py_file in py_files:
            module_name = py_file[:-3]
            full_module_path = f"days.{entry.name}.{module_name}"
            module = importlib.import_module(full_module_path)
            day_class = getattr(module, module_name)
            FINISHED_DAYS[day_number] = day_class
