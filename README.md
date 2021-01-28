# CIFAR 10 Dataset Library
This library was created to allow an easy usage of [CIFAR 10 DATA](https://www.cs.toronto.edu/~kriz/cifar.html). This is a wrapper around the instructions given on the [CIFAR 10 Site](https://www.cs.toronto.edu/~kriz/cifar.html)

## Installation
```bash
pip3 install cifar10
```

## Sample Usage
```python
import cifar10

# Train data
for image, label in cifar10.data_batch_generator():
    image # numpy array of an image, which is of shape 32 x 32 x 3
    label # integer value of the image label

# Test data
for image, label in cifar10.test_batch_generator():
    image # numpy array of an image, which is of shape 32 x 32 x 3
    label # integer value of the image label
```

## API

### data_batch_generator
Returns a generator of each image and label pair for data batch
```python
data_batch_generator(cache_location: str=".") -> Iterator[Tuple[np.array, int]]
```
#### parameters
* `cache_location` (default: library folder location): where to cache the cifar10 data

### test_batch_generator
Returns a generator of each image and label pair for test batch
```python
test_batch_generator(cache_location: str=".") -> Iterator[Tuple[np.array, int]]
```
#### parameters
* `cache_location` (default: library folder location): where to cache the cifar10 data

### meta
Returns the raw meta file
```python
meta(cache_location: str=".") -> Dict[bytes, Any]
```
#### parameters
* `cache_location` (default: library folder location): where to cache the cifar10 data

### image_label_map
Returns a dictionary of label
```
{
    0: 'airplane',
    1: 'automobile',
    ...
}
```

```python
image_label_map(cache_location: str=".") -> Dict[int, str]
```
#### parameters
* `cache_location` (default: library folder location): where to cache the cifar10 data
