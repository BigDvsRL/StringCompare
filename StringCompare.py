def check_str_(String, Comstring, Threshhold=0.8, skip=["#"]):
    # String is the main String, he will be compared with Comstring
    if isinstance(skip, str):
        skip = [str(skip)]
    try:
        if len(Check) == 0:
            Check = {"True": [],
                     "False": []}
    except:
        Check = {"True": [],
                 "False": []}
    if len(String) == 1 or len(Comstring) == 1:
        l = 0
        try:
            if String[l] == Comstring[l]:
                Check["True"].append(String[l])
            else:
                Check["False"].append(String[l])
        except:
            pass
    if len(String) > 1 and len(Comstring) > 1:
        for l in range(0, len(String) - 1):
            if l in skip:
                continue
            if l > len(Comstring) or l > len(String):
                continue
            try:
                if String[l] == Comstring[l]:
                    Check["True"].append(String[l])
                else:
                    Check["False"].append(String[l])
            except:
                continue
    try:
        if len(Check["True"]) >= math.floor(len(String) * Threshhold) and len(Check["True"]) > len(Check["False"]):
            return True
        if len(Check["True"]) < len(Check["False"]) and len(Check["False"]) >= math.floor(len(String) * Threshhold):
            return False
    except TypeError:
        raise ValueError("Threshhold isnt an Int or Float")
        return