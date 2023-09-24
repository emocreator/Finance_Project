# Random Number Generation and Normal Distribution Sampling

This Python script generates random numbers and samples from a normal distribution using two different methods: Box-Muller and Polar-Marsaglia. It also includes visualization of the generated data and measures the execution time for each method.

## Description

This script demonstrates two methods for generating random numbers and sampling from a standard normal distribution:

1. **Box-Muller Method**: This method generates random normal numbers by transforming uniformly distributed random numbers using the Box-Muller transform.

2. **Polar-Marsaglia Method**: This method generates random normal numbers using the Polar-Marsaglia method, which involves acceptance-rejection of uniform random numbers.

## Usage

1. Ensure you have Python and the necessary libraries (NumPy and Matplotlib) installed.

2. Open the script in a Python environment or text editor.

3. Run the script to generate random numbers and sample from the normal distribution.

4. The script will display histograms of the generated data and print the empirical mean and standard deviation.

## Performance Comparison

The script also measures the execution time for both the Box-Muller and Polar-Marsaglia methods to generate 5000 random normal samples. Here are the execution times:

- Box-Muller Method: [Execution Time] seconds
- Polar-Marsaglia Method: [Execution Time] seconds

These execution times can help you understand the efficiency of each method for your specific use case.

## Dependencies

- Python (3.x recommended)
- NumPy
- Matplotlib
