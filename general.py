import argparse
import os


def get_arguments():
    parser = argparse.ArgumentParser()
    parser._optionals.title = 'Arguments'
    parser.add_argument('-f', '--frequency', required=True, type=int, choices=[0, 1], help='0: quarterly | 1: yearly')
    parser.add_argument('-t', '--tab', required=True, type=int, choices=[0, 1, 2, 3, 4, 7],
                        help='0:BCDKT | 1:BCKQHDKD| 2:BCLCTTTT| 3:BCLCTTGT | 4:TMBCTC | 7:CSTC')
    parser.add_argument('-u', '--unit', required=True, type=int, choices=[1, 1000, 1000000])
    parser.add_argument('-y', '--final-year', required=True, type=int)
    parser.add_argument('-p', '--path', default='./data', help='Choose directory')
    return parser.parse_args()


def make_directory(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except NotADirectoryError:
        print('The directory name is invalid: ' + str(path))
        raise SystemExit
    os.chdir(path)