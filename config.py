import os

NUM_WORKER = min(4, os.cpu_count())
BATCH_SIZE = 5000