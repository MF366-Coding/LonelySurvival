import json
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.abspath(os.path.dirname(script_path))
save_file = os.path.join(script_dir, "savefile.json")
data_file = os.path.join(script_dir, "achiev.json")


def load() -> list:
    with open(save_file, "r", encoding="utf-8") as f:
        f_obj = json.load(f)
        f.close()
        
    with open(data_file, "r", encoding="utf-8") as d:
        d_obj = json.load(d)
        d.close()
    
    return [f_obj, d_obj]


def save(saveObj: dict, dataObj: dict):
    with open(save_file, "w", encoding="utf-8") as f:
        json.dump(saveObj, f, indent=4)
        f.close()
        
    with open(data_file, "w", encoding="utf-8") as d:
        json.dump(dataObj, d, indent=4)
        d.close()
    
    
def reset(dataObj: dict):
    a = {
		"day": 1,
		"points": 0,
        "weapons": 0
	}

    save(a, dataObj)