#!/usr/bin/env python3

import pandas as pd


class Aggregator:
    """
    Example usage:
        Aggregator('sample_results.jtl').write_file('results.csv')
    """

    header: str = 'Type,Name,Request Count,Failure Count,Median Response Time,Average Response Time,' \
                  'Min Response Time, Max Response Time,Average Content Size,Requests/s,Failures/s,25%,50%,75%,80%,' \
                  '90%,95%,98%,99%,99.9%,99.99%,100%,sd'

    def __init__(self, jmeter_results_file):
        self.__data = pd.read_csv(jmeter_results_file)
        self.__group_names = self.__data.groupby(['label']).groups.keys()
        self.__groups = {}
        for group_name in self.__group_names:
            self.__groups[group_name] = self.__data[self.__data['label'] == group_name]

    @staticmethod
    def csv_line(set_name, input_data):
        request_type = ''
        if '-' in set_name:
            request_type = set_name.split('-')[1].upper()
        name = set_name
        request_count: int = input_data['label'].count()
        failure_count = input_data[~input_data['success']]['label'].count()
        median_response_time = input_data['elapsed'].median()
        average_response_time = input_data['elapsed'].mean()
        min_response_time = input_data['elapsed'].min()
        max_response_time = input_data['elapsed'].max()
        min_ts: int = input_data['timeStamp'].min()
        max_ts: int = input_data['timeStamp'].max()
        duration: int = int((max_ts - min_ts)/1000)
        average_content_size_recv = input_data['bytes'].mean()
        average_content_size_sent = input_data['sentBytes'].mean()
        requests_per_second = request_count/duration
        failures_per_second = failure_count/duration
        percentile_25 = input_data['elapsed'].quantile(q=0.25)
        percentile_50 = input_data['elapsed'].quantile(q=0.5)
        percentile_75 = input_data['elapsed'].quantile(q=0.75)
        percentile_80 = input_data['elapsed'].quantile(q=0.8)
        percentile_90 = input_data['elapsed'].quantile(q=0.9)
        percentile_95 = input_data['elapsed'].quantile(q=0.95)
        percentile_98 = input_data['elapsed'].quantile(q=0.98)
        percentile_99 = input_data['elapsed'].quantile(q=0.99)
        percentile_99_9 = input_data['elapsed'].quantile(q=0.999)
        percentile_99_99 = input_data['elapsed'].quantile(q=0.9999)
        percentile_100 = input_data['elapsed'].quantile(q=1)
        standard_deviation = input_data['elapsed'].std()

        return f'{request_type},{name},{request_count},{failure_count},{median_response_time},{average_response_time},' \
               f'{min_response_time},{max_response_time},{average_content_size_recv},{requests_per_second},' \
               f'{failures_per_second},{percentile_25},{percentile_50},{percentile_75},{percentile_80},{percentile_90},' \
               f'{percentile_95},{percentile_98},{percentile_99},{percentile_99_9},{percentile_99_99},{percentile_100},' \
               f'{standard_deviation}'

    def write_file(self, out_file):
        with open(out_file, 'w') as agg_file:
            agg_file.write(f'{Aggregator.header}\n')
            for key, value in self.__groups.items():
                agg_file.write(f'{Aggregator.csv_line(key, value)}\n')
            agg_file.write(f'{Aggregator.csv_line("Aggregated", self.__data)}\n')
