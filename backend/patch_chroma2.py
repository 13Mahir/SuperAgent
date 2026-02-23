import re

file_path = '.venv/lib/python3.12/site-packages/chromadb/config.py'
with open(file_path, 'r') as f:
    orig = f.read()

lines = orig.split('\n')
out = []
in_settings = False
for line in lines:
    if line.strip().startswith('class Settings(BaseSettings)'):
        in_settings = True
    elif line.strip().startswith('class ') and in_settings:
        in_settings = False
        
    if in_settings:
        m = re.match(r'^(\s+)([a-zA-Z0-9_]+)\s*=\s*(["\'].*?["\']|\d+|True|False|None)(.*?)$', line)
        if m and ':' not in m.group(2): 
            val = m.group(3)
            typ = 'str'
            if val in ('True', 'False'): typ = 'bool'
            elif val == 'None': typ = 'Any'
            elif val.isdigit(): typ = 'int'
            
            line = f"{m.group(1)}{m.group(2)}: {typ} = {val}{m.group(4)}"
            
            if typ == 'Any' and 'from typing import Any' not in orig:
                out.insert(0, 'from typing import Any')
    
    out.append(line)

with open(file_path, 'w') as f:
    f.write('\n'.join(out))

