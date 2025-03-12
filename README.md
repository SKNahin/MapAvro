# AvroConverter

A Python package for bidirectional conversion between Bengali (Bangla) text and Avro phonetic typing.

## Overview

AvroConverter provides a robust solution for converting between Bengali Unicode text and Avro phonetic transliteration. It enables seamless transformation of Bengali text to its phonetic representation and vice versa.

## Features

- **Bengali to Avro Conversion**: Convert Bengali Unicode text to Avro phonetic representation
- **Avro to Bengali Conversion**: Convert Avro phonetic text to Bengali Unicode


## Installation

```bash
pip install MapAvro
```

## Usage

### Basic Usage

```python
from MapAvro import AvroConverter

# Initialize the converter
converter = AvroConverter()

# Convert Bengali to Avro
bengali_text = "আমি বাংলায় গান গাই।"
avro_text = converter.bengali_to_avro(bengali_text)
print(avro_text)  # Output: "ami banglay gan gai."

# Convert Avro to Bengali
avro_input = "ami banglay gan gai."
bengali_output = converter.avro_to_bengali(avro_input)
print(bengali_output)  # Output: "আমি বাংলায় গান গাই।"
```

## Technical Details

The conversion is based on character mapping tries that efficiently handle the transformation between Bengali and Avro representations. The package also includes text normalization capabilities to handle edge cases and ensure consistent input/output.

The core components are:

- `AvroConverter`: Main class that handles bidirectional conversion


## Requirements

- Python 3.6+

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.