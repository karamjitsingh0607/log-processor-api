def aggregator(output):
    all_result = {
        "INFO": [],
        "WARNING": [],
        "ERROR": []
    }
    for res in output:
        for key in all_result:
            all_result[key].extend(res[key])

    return all_result