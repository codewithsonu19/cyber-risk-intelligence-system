def create_features(likelihood, impact, asset_criticality, cvss_score):
    return [[
        likelihood,
        impact,
        asset_criticality,
        cvss_score
    ]]