class ThreatDetectionSystem:
    def __init__(self):
        self.alert_threshold = 95  # AI Security Rating

    def evaluate_risk(self, threat_level):
        if threat_level > self.alert_threshold:
            return 'Activate Quantum Key Rotation'
        return 'Normal Operation'
