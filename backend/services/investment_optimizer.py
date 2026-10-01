def optimize_investment(options, available_budget):
    """
    Available budget ke andar
    best security investment choose karta hai.
    """

    affordable_options = [
        option
        for option in options
        if option["cost"] <= available_budget
    ]

    for option in affordable_options:
        cost = option["cost"]
        risk_reduction = option["risk_reduction"]

        if cost > 0:
            option["roi"] = (
                (risk_reduction - cost) / cost
            ) * 100
        else:
            option["roi"] = 0

    affordable_options.sort(
        key=lambda x: x["roi"],
        reverse=True
    )

    return affordable_options
def optimize_investments(options, available_budget):
    return optimize_investment(options, available_budget)

