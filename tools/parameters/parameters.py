#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

DEFAULT_SNAPSHOT_COLUMN_POSITION = 1
DEFAULT_PEER_COLUMN_POSITION = 2
DEFAULT_FEATURE_WINDOW_LENGTH = 256
DEFAULT_FEATURE_WINDOW_WIDTH = 256
DEFAULT_NUMBER_BLOCK_PER_SAMPLES = 32
DEFAULT_INPUT_FILE_SWARM_SORTED = 'S4'
DEFAULT_OUTPUT_FILE_SWARM_SORTED = 'S4_output.txt'

DEFAULT_TRAINING_EPOCHS = 10
DEFAULT_TRAINING_METRICS = 'mse'
DEFAULT_TRAINING_LOSS = 'mse'
DEFAULT_TRAINING_OPTIMIZER = 'adam'
DEFAULT_TRAINING_BATCH_SIZE = 32
DEFAULT_SAVE_MODEL_FILE = 'models_saved/model'
DEFAULT_LOAD_MODEL_FILE = 'models_saved/model'
DEFAULT_ADVERSARIAL_MODEL = False
DEFAULT_VERBOSITY = 1
TIME_FORMAT = '%Y-%m-%d,%H:%M:%S'

DEFAULT_FILE_SAVE_SAMPLES = 'samples_saved/samples'
DEFAULT_FILE_LOAD_SAMPLES = 'samples_saved/samples'



def add_arguments(parser):


    help_msg = 'Snapshot column position (Default {})'.format(DEFAULT_SNAPSHOT_COLUMN_POSITION)
    parser.add_argument("--column_snapshot", type=int, help=help_msg, default=DEFAULT_SNAPSHOT_COLUMN_POSITION)

    help_msg = 'Peer column position (Default {})'.format(DEFAULT_PEER_COLUMN_POSITION)
    parser.add_argument("--column_peer", type=int, help=help_msg, default=DEFAULT_PEER_COLUMN_POSITION)

    help_msg = 'Feature window length (Default {})'.format(DEFAULT_FEATURE_WINDOW_LENGTH)
    parser.add_argument("--window_length", type=int, help=help_msg, default=DEFAULT_FEATURE_WINDOW_LENGTH)

    help_msg = 'Feature window width (Default {})'.format(DEFAULT_FEATURE_WINDOW_WIDTH)
    parser.add_argument("--window_width", type=int, help=help_msg, default=DEFAULT_FEATURE_WINDOW_WIDTH)

    help_msg = 'Number block per samples (Default {})'.format(DEFAULT_NUMBER_BLOCK_PER_SAMPLES)
    parser.add_argument("--number_block", type=int, help=help_msg, default=DEFAULT_NUMBER_BLOCK_PER_SAMPLES)

    help_msg = 'Input swarm file (Default {})'.format(DEFAULT_INPUT_FILE_SWARM_SORTED)
    parser.add_argument("--input_swarm", type=str, help=help_msg, default=DEFAULT_INPUT_FILE_SWARM_SORTED)

    help_msg = 'Output swarm file (Default {})'.format(DEFAULT_OUTPUT_FILE_SWARM_SORTED)
    parser.add_argument("--output_swarm", type=str, help=help_msg, default=DEFAULT_OUTPUT_FILE_SWARM_SORTED)

    help_msg = 'Training epochs (Default {})'.format(DEFAULT_TRAINING_EPOCHS)
    parser.add_argument("--epochs", type=int, help=help_msg, default=DEFAULT_TRAINING_EPOCHS)

    help_msg = 'Training metrics (Default {})'.format(DEFAULT_TRAINING_METRICS)
    parser.add_argument("--metrics", type=str, help=help_msg, default=DEFAULT_TRAINING_METRICS)

    help_msg = 'Training loss (Default {})'.format(DEFAULT_TRAINING_LOSS)
    parser.add_argument("--loss", type=str, help=help_msg, default=DEFAULT_TRAINING_LOSS)

    help_msg = 'Training optimizer (Default {})'.format(DEFAULT_TRAINING_OPTIMIZER)
    parser.add_argument("--optimizer", type=str, help=help_msg, default=DEFAULT_TRAINING_LOSS)

    help_msg = 'Training size batch (Default {})'.format(DEFAULT_TRAINING_BATCH_SIZE)
    parser.add_argument("--size_batch", type=int, help=help_msg, default=DEFAULT_TRAINING_BATCH_SIZE)

    help_msg = 'Save file neural model (Default {})'.format(DEFAULT_SAVE_MODEL_FILE)
    parser.add_argument("--save_model", type=str, help=help_msg, default=DEFAULT_SAVE_MODEL_FILE)

    help_msg = 'Load file neural model (Default {})'.format(DEFAULT_LOAD_MODEL_FILE)
    parser.add_argument("--load_model", type=str, help=help_msg, default=DEFAULT_LOAD_MODEL_FILE)

    help_msg = 'Adversarial Model (Default {})'.format(DEFAULT_ADVERSARIAL_MODEL)
    parser.add_argument("--adversarial_model", type=bool, help=help_msg, default=DEFAULT_ADVERSARIAL_MODEL)

    help_msg = 'Verbosity level (Default {})'.format(logging.INFO)
    parser.add_argument("--verbosity", type=int, help=help_msg, default=logging.INFO)

    help_msg = 'Save file neural model (Default {})'.format(DEFAULT_FILE_SAVE_SAMPLES)
    parser.add_argument("--save_samples", type=str, help=help_msg, default=DEFAULT_FILE_SAVE_SAMPLES)

    help_msg = 'Load file neural model (Default {})'.format(DEFAULT_FILE_LOAD_SAMPLES)
    parser.add_argument("--load_samples", type=str, help=help_msg, default=DEFAULT_FILE_LOAD_SAMPLES)




    self.corrected_swarm_file = ''
    self.failed_swarm_file = ''
    self.original_swarm_file = ''
    self.topology = 'ModelV1'
    self.analyse_file_mode = 'a+'
    self.analyse_file_results = 'results.txt'
    self.trace_found_in_original_and_failed = 0
    self.trace_found_in_original_and_corrected = 0
    self.trace_found_in_original_and_failed_and_corrected = 0
    self.threshold = 1
    self.seed = 0
    self.pif = 0



















    cmd_choices = ['Calibration', 'CreateSamples', 'Training', 'Predict', 'Analyse']
    parser.add_argument('cmd', choices=cmd_choices)
    return parser






