# Extended RandCrack – Advanced Python `random` module cracker / predictor

This library is based on [randcrack](https://github.com/tna0y/Python-random-module-cracker) but provides **extended functionality**, including support for **64-bit number submission** and **64-bit state offsetting**, making it even more powerful for reverse-engineering or simulating Python's `random` module.

## What It Does

This script clones Python’s built-in random number generator based on the **Mersenne Twister**. After observing 624 outputs of 32-bit integers, it reconstructs the internal state and can then:

- **Predict all future outputs**
- **Predict past outputs**
- **Handle 64-bit values directly** with `submit_64()` and `offset_64()`

⚠️ The Mersenne Twister is **not cryptographically secure**. Do **not** use it for secure cryptographic applications. [More info](https://en.wikipedia.org/wiki/Mersenne_Twister)

## Installation

```bash
pip install extendedrandcrack
```

## Usage

You must provide exactly 624 **32-bit integers** or **312 64-bit integers** to reconstruct the RNG state. Use either:

- `submit(value)` – for 32-bit values
- `submit_64(value)` – for 64-bit values (automatically splits into two 32-bit chunks)

### Basic Example (32-bit)

```python
import random
import time
from extendedrandcrack import RandCrack

random.seed(time.time())
rc = RandCrack()

for \_ in range(624):
rc.submit(random.getrandbits(32))

print("Random:", random.getrandbits(32))
print("Predicted:", rc.predict_getrandbits(32))
```

### Using 64-bit Submissions

```python
import random
from extendedrandcrack import RandCrack

rc = RandCrack()
random.seed(12345)
values = [random.getrandbits(64) for _ in range(312)]

for v in values:
rc.submit_64(v)

print("Next random 64-bit value:")
high = rc.predict_getrandbits(32)
low = rc.predict_getrandbits(32)
predicted = (high << 32) | low
print(predicted)
```

## Predicting Past Outputs

You can go back in time using:

- `offset(n)` – where `n` is number of 32-bit steps
- `offset_64(n)` – where `n` is number of 64-bit steps

Negative values go back, positive values move forward.

### Example – Rewind and Predict

```python
import random
from extendedrandcrack import RandCrack

random.seed(42)
original = [random.getrandbits(32) for _ in range(10)]

rc = RandCrack()
for \_ in range(624):
rc.submit(random.getrandbits(32))

rc.offset(-624) # rewind to where we started
rc.offset(-10) # rewind before the known sequence

print("Original:", original)
print("Recovered:", [rc.predict_getrandbits(32) for _ in range(10)])
```

## Accuracy Note on High-level Functions

The following prediction methods are available:

- `predict_getrandbits(k)`
- `predict_randbelow(n)`
- `predict_randrange(start, stop[, step])`
- `predict_randint(a, b)`
- `predict_choice(seq)`
- `predict_random()`

⚠️ `randbelow()`, `randint()`, `randrange()`, and `choice()` may consume **more than one random number per call**, so **rewinding past these calls is imprecise**. Use `getrandbits()` or `random()` for exact state tracking.

## Testing

The script includes a test block that checks both forward and backward prediction across 1000 values and asserts 100% accuracy.

## License

MIT. Based on original `randcrack` by tna0y, extended for 64-bit support and improved state handling.
