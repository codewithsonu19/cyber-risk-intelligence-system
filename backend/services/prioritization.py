def prioritize_risks(
    risks: list[dict]
) -> list[dict]:
    """
    Rank risks from highest to lowest.
    """

    return sorted(
        risks,
        key=lambda risk: risk.get(
            "risk_score",
            risk.get(
                "adjusted_risk_score",
                0
            )
        ),
        reverse=True
    )


def prioritize_vulnerabilities(
    vulnerabilities: list[dict]
) -> list[dict]:
    """
    Rank vulnerabilities based on:

    Severity
    Exploitability
    Likelihood
    """

    def vulnerability_score(
        vulnerability
    ):

        severity = vulnerability.get(
            "severity",
            0
        )

        exploitability = vulnerability.get(
            "exploitability",
            0
        )

        likelihood = vulnerability.get(
            "likelihood",
            0
        )

        return (
            severity * 0.4
            +
            exploitability * 0.3
            +
            likelihood * 10 * 0.3
        )

    return sorted(
        vulnerabilities,
        key=vulnerability_score,
        reverse=True
    )