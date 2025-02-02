import time
from bot.core.hft_execution import HFTExecutionEngine

def test_execution_latency():
    engine = HFTExecutionEngine()
    start_time = time.time()
    engine.execute_trade()
    end_time = time.time()
    assert (end_time - start_time) < 0.001, "Execution speed exceeded 1ms"
