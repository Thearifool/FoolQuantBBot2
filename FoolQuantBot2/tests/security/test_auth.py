from bot.auth.tiered_mfa_policy import TieredMFAPolicy

def test_mfa_enforcement():
    policy = TieredMFAPolicy()
    client = {'balance': 60000}
    assert policy.enforce_mfa(client) == True, "MFA should be enforced for high balances"
