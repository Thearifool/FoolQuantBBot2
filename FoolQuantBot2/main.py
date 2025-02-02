from bot.core.hft_execution import HFTExecutionEngine
from bot.macro.macro_economic_monitor import MacroEconomicMonitor

if __name__ == '__main__':
    macro_monitor = MacroEconomicMonitor()
    execution_engine = HFTExecutionEngine()
    execution_engine.execute_trade()
