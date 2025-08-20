import json, sys
from pathlib import Path

from fc_model import FCModel

p = Path('data/ultracube.fc')
m = FCModel(str(p))
out = p.with_name(p.stem + '_roundtrip.fc')
m.save(str(out))
with open(out, 'r') as f:
    json.load(f)