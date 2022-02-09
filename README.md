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
The result is printed in the terminal and in matplotlib image

![image](https://user-images.githubusercontent.com/87011531/153202772-7c97a228-efcc-43d1-b015-1a47f977cc97.png)

![image](https://user-images.githubusercontent.com/87011531/153202495-805cc85f-7b4b-4ecd-8328-d595a081e7fb.png)
