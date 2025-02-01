
class ChaosInjector:
    def __init__(self):
        self.error_modes = ['api_down', 'network_latency', 'order_rejection']

    def inject_failure(self):
        failure = random.choice(self.error_modes)
        print(f'?? Injecting Failure: {failure}')

