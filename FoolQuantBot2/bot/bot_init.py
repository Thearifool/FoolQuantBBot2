# Initialization for FoolQuantBot2
import os
import logging
from core.hft_execution import HFTExecutionEngine
from risk.risk_manager import RiskManager

class FoolQuantBot2:
    def __init__(self):
        self.trading_engine = HFTExecutionEngine()
        self.risk_manager = RiskManager()

    def start(self):
        logging.info("FoolQuantBot2 is starting...")
        self.trading_engine.execute()
