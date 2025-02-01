
class AutoRecoveryEngine:
    def __init__(self):
        self.failure_history = deque(maxlen=100)
        self.adaptive_thresholds = {'api_errors': (5, 60), 'order_fills': (0.95, 30)}

    async def monitor_and_heal(self):
        while True:
            health_status = await self._assess_health()
            if health_status['critical']:
                await self._execute_graceful_shutdown()
            elif health_status['degraded']:
                await self._perform_targeted_recovery(health_status)
            await asyncio.sleep(1)

