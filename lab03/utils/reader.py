import numpy as np
import csv

def getInput(path: str, delimiter: str):
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=delimiter)
        next(reader)

        labels = []
        images = []

        for row in reader:
            label = int(row[0])
            image = np.array(row[1:], dtype=np.float32).reshape((28, 28))

            labels.append(label)
            images.append(image)
        
        labels = np.array(labels, dtype=np.int32)
        images = np.array(images, dtype=np.float32)
    
    return [labels, images]