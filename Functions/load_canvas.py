import json
from pathlib import Path
def load_canvas(path_or_dict):
    if isinstance(path_or_dict, (str, Path)):
        return json.loads(Path(path_or_dict).read_text(encoding="utf-8"))
    CanvasDict=path_or_dict        
    return CanvasDict
