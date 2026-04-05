def worker(chunk):
    result = {
        "INFO": [],
        "WARNING": [],
        "ERROR": []
    }
    for line in chunk:
        if "INFO" in line:
            result["INFO"].append(line)
        elif "WARNING" in line:
            result["WARNING"].append(line)
        else:
            result["ERROR"].append(line)
    return result