# Streamlit Samples

This repository is a collection of various examples and code snippets to help you get started with [Streamlit](https://streamlit.io/), a powerful framework for building interactive web applications with Python.

## Table of Contents

- [Getting Started](#getting-started)
- [Examples](#examples)
- [License](#license)

## Getting Started

Before you can run the examples in this repository, you'll need to have [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.anaconda.com/miniconda/) installed on your system. Then, you can create a conda environment and install Streamlit along with other required dependencies.

1. Clone the repository:

   ```
   git clone https://github.com/<your_username>/streamlit-samples.git

   cd streamlit-samples
   ```

2. Create a conda environment:

   ```
   conda create --name <conda_env_name> python=3.9

   conda activate <conda_env_name>
   ```

3. Install the required dependencies:

   ```
   conda env update --file environment.yml
   ```

4. Run a sample:
   ```
   streamlit run 000-basics/<script_name>.py
   ```

## Examples

- [**Basic:**](000-basics) Introductory Streamlit examples that demonstrate key features such as widgets, layouts, and displaying data. These examples are ideal for beginners to learn how to create simple, interactive apps with Streamlit.

## License

This repository is licensed under the Apache License. See the [LICENSE](LICENSE) file for more information.
