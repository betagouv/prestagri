from app.model import Menage


def create_menage_with_quotient(quotient_familial_euros: int, nombre_personnes: int = 1) -> Menage:
    """Helper to create a menage with a specific quotient familial.

    quotient_familial = revenu_fiscal_reference / (12 * nombre_unites)
    For a single person: revenu = quotient_familial * 12 * 1

    Args:
        quotient_familial_euros: The desired quotient familial in euros
        nombre_personnes: Number of people in the household (default: 1)

    Returns:
        A Menage object with the specified quotient familial
    """
    revenu_annuel = quotient_familial_euros * 12 * nombre_personnes
    return Menage.create_menage(
        foyer_fiscal_agent_revenu=revenu_annuel,
        foyer_fiscal_agent_membres=nombre_personnes
    )
