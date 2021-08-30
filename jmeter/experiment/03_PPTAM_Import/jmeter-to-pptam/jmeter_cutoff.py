import pandas as pd


class JMeterCutOff:
    def __init__(self, in_file='sample_results.jtl', out_file='sample_results_cutoff.jtl',
                 start_ms=240000, end_ms=120000, timestamp_field='timestamp'):
        self.__in_file = in_file
        self.__out_file = out_file
        self.__start_ms = start_ms
        self.__end_ms = end_ms

        csv_in = pd.read_csv(self.__in_file)
