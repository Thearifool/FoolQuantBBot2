import asyncio
from bot.api.api_health_monitor import PreemptiveAPIMonitor

async def test_failover_recovery():
    monitor = PreemptiveAPIMonitor()
    await monitor.health_check()
    assert monitor.active_exchange != 'binance', 'Failover did not trigger properly'
