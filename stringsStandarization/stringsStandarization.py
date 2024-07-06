import pandas as pd
import os
import re
import unittest

def first_substring_before_delimiter(string):
    # Specific complex patterns to match
    specific_patterns = [
        r'Indian Institute of Technology',
        # Add more specific patterns here if needed
    ]
    
    for pattern in specific_patterns:
        match = re.search(pattern, string)
        if match:
            return match.group(0)
    
    # All other more general patterns will be sorted here
    parts = re.split(r'[^a-zA-Z\s,()]', string)
    return parts[0]

class TestStringMethods(unittest.TestCase):
    def test_specific_pattern(self):
        self.assertEqual(first_substring_before_delimiter("Director-Indian Institute of Technology(IIT Delhi)||Dy.Registrar(Stores) Central Store Purchase Section-IIT Delhi"), "Indian Institute of Technology")
    
    def test_default_split(self):
        self.assertEqual(first_substring_before_delimiter("Company XYZ||Other Information"), "Company XYZ")
    
    def test_exclude_commas_parentheses(self):
        self.assertEqual(first_substring_before_delimiter("Company, XYZ (Global)||Other Information"), "Company, XYZ (Global)")
    
    def test_no_delimiters(self):
        self.assertEqual(first_substring_before_delimiter("SimpleCompanyName"), "SimpleCompanyName")
    
    def test_empty_string(self):
        self.assertEqual(first_substring_before_delimiter(""), "")

def main(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        
        company_names = df['Organisation Chain']
        standardized_names = [first_substring_before_delimiter(name) for name in company_names]
        
        result_df = df.copy()
        result_df['Standardized_Name'] = standardized_names
        
        result_df.to_csv(output_file, index=False)
        print(f"Data successfully standardized and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = os.path.join('data', 'eprocureData.csv')
    output_file = os.path.join('output', 'standardized_file.csv')
    
    main(input_file, output_file)

    unittest.main(argv=[''], verbosity=2, exit=False)