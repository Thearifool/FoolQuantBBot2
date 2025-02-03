class AutoRecoveryEngine:
    def __init__(self):
        self.max_retries = 3
        self.repair_actions = ["restart_bot", "switch_api", "adjust_risk"]

    def diagnose_issue(self, error_code):
        if error_code in ["API_FAIL", "ORDER_REJECTED"]:
            return self.repair_actions[0]
        elif error_code == "HIGH_LATENCY":
            return self.repair_actions[1]
        return self.repair_actions[2]
