# MNIST images prediction

## Pandas & Numpy 
Used to arrange data before and after the training of the model

## Model requirments
### os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

### Adjustment to cpu
Need to add:
```
with tf.device('/cpu:0):
```
before compiling, saving and loading the model

### Performed by
TensorFlow, keras and sklearn

## UI
While loop runs until closing the program. Every time you close the matplolib image another prediction is accured on random number.

```
while True:
    random_number = randrange(0,10000)
    Number_prediction(Guesser_model, random_number)
```
