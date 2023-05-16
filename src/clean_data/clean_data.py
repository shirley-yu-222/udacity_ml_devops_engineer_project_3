#!/usr/bin/env python
"""
Performs basic cleaning on data
"""
import argparse
import logging
import pandas as pd
import os

logging.basicConfig(
    filename=os.getcwd()+'/../../logs/clean_data.log',
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def clean_data(args):
    """
    Basic cleaning of data, including removing initial whitespace in column
    headers and removing duplicate rows
    """
    # remove inital whitespace in column headers
    df = pd.read_csv(args.path_data, skipinitialspace=True)
    # drop duplicate rows
    df.drop_duplicates(inplace=True)
    # drop rows with '?' i.e. unknowns
    df.replace({'?': None}, inplace=True)
    df.dropna(inplace=True)
    df.to_csv(args.path_data_clean)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This steps cleans the data")
    parser.add_argument(
        "--path_data",
        type=str,
        help="path to data",
        required=True
    )
    parser.add_argument(
        "--path_data_clean",
        type=str,
        help="path to save clean data",
        required=True
    )
    args = parser.parse_args()

    logger.info("Cleaning data process started")
    clean_data(args)
    logger.info("Cleaning data complete")
