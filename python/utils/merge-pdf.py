#!/usr/bin/env python3
"""
PDF Merger Tool

This script merges multiple PDF files into a single output PDF file.
It accepts input PDF files as command line arguments and produces
a merged PDF file as output.

Usage:
    python merge-pdf.py -i input1.pdf input2.pdf ... -o output.pdf
"""

import argparse
import logging
import os
import sys
from typing import List

from PyPDF2 import PdfMerger

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def validate_pdf_path(file_path: str) -> bool:
    """
    Validate if the given file path exists and has a .pdf extension.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return False
    if not file_path.lower().endswith('.pdf'):
        logger.error(f"Not a PDF file: {file_path}")
        return False
    return True

def merge_pdfs(input_files: List[str], output_file: str) -> bool:
    """
    Merge multiple PDF files into a single PDF file.
    
    Args:
        input_files (List[str]): List of input PDF file paths
        output_file (str): Output PDF file path
        
    Returns:
        bool: True if merge was successful, False otherwise
    """
    try:
        merger = PdfMerger()
        
        # Validate and merge each input file
        for pdf_file in input_files:
            if not validate_pdf_path(pdf_file):
                return False
            logger.info(f"Adding file: {pdf_file}")
            merger.append(pdf_file)
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Write the merged PDF
        logger.info(f"Writing merged PDF to: {output_file}")
        merger.write(output_file)
        merger.close()
        logger.info("PDF merge completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error merging PDFs: {str(e)}")
        return False

def main() -> int:
    """
    Main function to handle command line arguments and execute the PDF merge.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    parser = argparse.ArgumentParser(
        description="Merge multiple PDF files into a single PDF file"
    )
    parser.add_argument(
        '-i', '--input',
        nargs='+',
        required=True,
        help='Input PDF files to merge'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output PDF file path'
    )
    
    args = parser.parse_args()
    
    if merge_pdfs(args.input, args.output):
        return 0
    return 1

if __name__ == '__main__':
    sys.exit(main())
