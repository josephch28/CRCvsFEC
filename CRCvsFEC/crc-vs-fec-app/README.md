# CRC vs FEC Comparison Application

This project implements a comparison between the Cyclic Redundancy Check (CRC) and Forward Error Correction (FEC) methods using a modern web interface built with Streamlit. The application allows users to input an 8-bit word and a polynomial, then measures and displays the execution times for both methods.

## Features

- User-friendly interface for inputting data.
- Real-time comparison of CRC and FEC execution times.
- Visual representation of the results using bar charts.

## Requirements

To run this application, you need to have Python installed on your machine. The following libraries are required:

- Streamlit
- Matplotlib

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd crc-vs-fec-app
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the application, run the following command in your terminal:

```
streamlit run app.py
```

This will launch the application in your default web browser.

## Usage

1. Enter an 8-bit binary word in the designated input field.
2. Enter a binary polynomial (minimum 2 bits) in the corresponding input field.
3. Click the "Compare" button to see the results.
4. The application will display the CRC remainder, FEC encoded word, and the execution times for both methods.

## Conclusion

This application demonstrates the efficiency of the CRC method compared to FEC, showcasing its low computational cost while maintaining data integrity.