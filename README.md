# Denoise - A quick analysis in frequency domain to smooth your time series data in python!

 
With Denoise, you can quickly analyze and visualize the fast fourier transform of your time series data with python in just few lines of code. Just read the time series data collected at equal time intervals and specify the final time (# of datapoints * sample time) and the sample time, and the rest is done for you.

# Overview
The Denoise Python package was written to improve the time in analyzing the time series data in frequency domain and understand the significant frequency components in data. It provides the following key features

  - Visualize the noise data
  - Calculate fft, power spectral density (PSD)
  - Plot PSD
  - Calculate the cleaned time series
  - Plot the cleaned time series data


## Usage

In the following paragraphs, I am going to describe how you can get and use Denoise for your own projects.

###  Getting it

To download distributions, fork this github repo. 

### Using it

Denoise was programmed with ease-of-use in mind. First, import Denoisefft from Denoise

```Python
from Denoise import Denoisefft
```

And you are ready to go! At this point, I want to clearly explain Denoisefft class 

## Initialize a Denoisefft object
array is the time series value data
tf is the final time in seconds at which data logging was stopped
dt is the sample time - the interval between two observations

```Python
denoise_one=Denoisefft(array,tf,dt)
```

## Calculate fast fourier transform and power spectrum density
The class Denoisefft has a method PSD to calculate the fast fourier transform, PSD, and visualize the noisy data and
power spectrum density to understand the significant components of the time series data.

```Python
denoise_one.PSD()

```
#### Denoise the time series data
Using the power spectral density plot identify the cut off amplitude for the components in the time series data.

```Python
denoise_one.denoise()
```

License
----

MIT License

Copyright (c) 2020 Chaitanya Joshi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
