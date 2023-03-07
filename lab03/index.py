from utils import zipfile
import model

zipfile.unarchive('data/lab03.zip')

model.generate('num_guess.model', 'data/mnist_train.csv', 28)

model.test('num_guess.model', 'data/mnist_test.csv')

model.predict('num_guess.model', 'digits')