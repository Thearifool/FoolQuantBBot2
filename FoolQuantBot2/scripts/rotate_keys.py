
class EmergencyKeyRotation:
    def execute(self):
        self._rotate_all_keys()
        self._purge_decrypted_cache()
        print('?? EMERGENCY KEY ROTATION EXECUTED')

