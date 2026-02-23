import re

file_path = '.venv/lib/python3.12/site-packages/chromadb/config.py'
with open(file_path, 'r') as f:
    orig = f.read()

lines = orig.split('\n')
out = []
in_settings = False
config_added = False
for line in lines:
    out.append(line)
    if line.strip().startswith('class Settings(BaseSettings)'):
        in_settings = True
    elif in_settings and not config_added:
        out.append('    model_config = {"extra": "ignore"}')
        config_added = True
        in_settings = False

with open(file_path, 'w') as f:
    f.write('\n'.join(out))

