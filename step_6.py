# -*- coding: utf-8 -*-

import pandas as pd
import os
import argparse

from utils.utils import download, check_hash


def step6(save_folder: str = 'data'):

    print('Step 6')

    if not os.path.isdir(save_folder):
        os.makedirs(save_folder)

    output_file_path = os.path.join(save_folder, 'EBPlusPlusAdjustPANCAN_IlluminaHiSeq_RNASeqV2-v2.geneExp.tsv')
    if not os.path.isfile(output_file_path):
        download_link = 'https://api.gdc.cancer.gov/data/9a4679c3-855d-4055-8be9-3577ce10f66e'
        download(download_link, output_file_path)

    # check hashsum
    hash_pass = check_hash(output_file_path)
    if not hash_pass:
        raise Exception(f'Hash sum validation for {output_file_path} was not passed, check the file or download it again')

    print('OK')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This script downloads EBPlusPlusAdjustPANCAN_IlluminaHiSeq_RNASeqV2-v2.geneExp.tsv file ' + '\n' +
                                                 'and saves it to the data/ folder by default')
    parser.add_argument('-s', '--save_folder', type=str, help='full path to folder to save downloaded files', default='data')
    args = parser.parse_args()

    step6(args.save_folder)
