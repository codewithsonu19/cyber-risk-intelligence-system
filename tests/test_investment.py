from backend.services.investment_optimizer import optimize_investment


def test_investment_optimizer():

    options = [
        {
            "name": "MFA",
            "cost": 2,
            "risk_reduction": 9
        },
        {
            "name": "Patch Management",
            "cost": 3,
            "risk_reduction": 7
        },
        {
            "name": "Firewall Upgrade",
            "cost": 5,
            "risk_reduction": 8
        }
    ]

    result = optimize_investment(options, 3)

    assert len(result) == 2
    assert result[0]["name"] == "MFA"