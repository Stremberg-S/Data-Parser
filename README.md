# Data Parser

<hr>

This is a Python script that allows you to retrieve and parse data from online catalogs of different stores. It uses
asynchronous programming with the asyncio library to efficiently fetch data from multiple sources simultaneously.

### Features

Retrieves product information such as price, availability status, and item details from specified online stores.
Supports multiple stores, including Jimms and Marimekko.
Fetches data asynchronously to improve performance and efficiency.
Writes the extracted data to separate files for each store.
Handles exceptions gracefully and writes error messages to the appropriate files.

### Requirements

* Python 3.x
* asyncio library
* Beautiful Soup library (for HTML parsing)

### Installation

1. Clone the project repository from GitHub:

   ```bash
   git clone https://github.com/Stremberg-S/Data-Parser.git
   ```

2. Change to the project directory:

   ```bash
   cd Data-Parser
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

<br>

### Usage

1. Configure path.py file to specify the file paths for storing the extracted data.

   ```python
   # you can modify this file according to your requirements
   all_stores = "your/path/All_Stores.txt"
   jimms = "/your/path/Jimms.txt"
   marimekko = "/Users/stremberg_s/Desktop/Marimekko.txt"
   ```

    2.
        * Customize the get_all_*() functions in the file to retrieve the desired data from the online catalogs. You can
          add
          or
          modify these functions according to your requirements.

            * For this you'll need to make catalog-directory, where is located files for all stores you need

                * Below is an example of my Graphic_Cards.py file which functions I call in main:

               ```python
                # you can modify this file according to your requirements
                import asyncio

                from Data_Parser import parse_data 
           
           
                async def get_all_RTX4080():
                    tasks = [
                        # Name of item
                        parse_data(
                            "store",
                            wanted_price,
                            "url"
                        ),
                        # Name of item
                        parse_data(
                            "store",
                            wanted_price,
                            "url"
                        ),
                        # Name of item
                        parse_data(
                            "store",
                            wanted_price,
                            "url"
                        )
                      ]
                      await asyncio.gather(*tasks)
                  
                  
                async def get_all_RTX4090():
                    tasks = [
                        # Name of item
                         parse_data(
                            "store",
                            wanted_price,
                            "url"
                         )
                     ]
                     await asyncio.gather(*tasks)
               


3. Run the script from Data_Parser_Main.py
4. The script will start retrieving and parsing data from the specified online stores. The extracted information will be
   written to separate files for each store.
5. The script will continue running until it is interrupted by a keyboard interrupt (Ctrl+C). The interrupted execution
   will be handled gracefully, and appropriate messages will be written to the files.

<hr>