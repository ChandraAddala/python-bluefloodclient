class Metric(object):

    def __init__(self, metric_name, metric_value, timestamp,
                 ttl=3 * 60 * 60 * 24):
        self.metric_name = metric_name
        self.metric_value = metric_value
        self.timestamp = timestamp
        self.ttl = ttl

    def get_name(self):
        return self.metric_name

    def __str__(self):
        return "metric name: %s, timestmap: %s, metric value %s" \
               %(self.metric_name, self.timestamp, self.metric_value)
