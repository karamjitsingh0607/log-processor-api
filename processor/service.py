from multiprocessing import Pool, set_start_method
from processor.aggregator import aggregator
from processor.chunker import create_chunks
from processor.worker import worker

def process_logs(lines, batch_size, num_worker):
    batch = []
    output = []
    with Pool(num_worker) as p:
        count = 0
        for line in lines:
            batch.append(line)
            count += 1

            if count % 100000 == 0:
                print(f"Processed {count} lines...")
                
            if len(batch) == batch_size:
                chunks = create_chunks(batch, num_worker)
                output.extend(p.map(worker,chunks))
                batch.clear()
            
        if batch:
            chunks = create_chunks(batch,num_worker)
            output.extend(p.map(worker,chunks))
        return aggregator(output)