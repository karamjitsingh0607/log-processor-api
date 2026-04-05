def create_chunks(batch,NUM_WORKER):
    NUM_WORKER = min(len(batch),NUM_WORKER)
    chunk_size = len(batch) // NUM_WORKER
    start = 0
    destination = chunk_size
    chunks = []
    for i in range(NUM_WORKER):
        if i+1 == NUM_WORKER:
            destination = len(batch)
        chunks.append(batch[start:destination])
        start = destination
        destination = start + chunk_size
    return chunks

