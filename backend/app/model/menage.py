from pydantic import BaseModel
from app.model import FoyerFiscal, Centimes

class Menage (BaseModel):
    beneficiaire_porteur_handicap: bool
    garde_alternee: bool
    parent_isole: bool
    outre_mer: bool
    membres: list[FoyerFiscal]

    @classmethod
    def create_menage(cls, menage_agent_revenu: int,
        menage_agent_membres: int,
        foyer_fiscal_conjoint_revenu: int | None = None,
        foyer_fiscal_conjoint_membres: int | None = None,
        foyer_fiscal_etudiant_revenu: int | None = None,
        foyer_fiscal_etudiant_membres: int | None = None,
        beneficiaire_porteur_handicap: bool = False,
        garde_alternee: bool = False,
        parent_isole: bool = False,
        outre_mer: bool = False) :

        agent = FoyerFiscal(revenu=Centimes.from_euros_int(menage_agent_revenu),
                            personnes=menage_agent_membres)
        membres = [agent]
        if foyer_fiscal_conjoint_revenu is not None and foyer_fiscal_conjoint_membres is not None:
            conjoint = FoyerFiscal(revenu=Centimes.from_euros_int(foyer_fiscal_conjoint_revenu),
                                   personnes=foyer_fiscal_conjoint_membres)
            membres.append(conjoint)
        if foyer_fiscal_etudiant_revenu is not None and foyer_fiscal_etudiant_membres is not None:
            etudiant = FoyerFiscal(revenu=Centimes.from_euros_int(foyer_fiscal_etudiant_revenu),
                                   personnes=foyer_fiscal_etudiant_membres)
            membres.append(etudiant)
        menage = cls(beneficiaire_porteur_handicap=beneficiaire_porteur_handicap, garde_alternee=garde_alternee,
                        parent_isole=parent_isole, outre_mer=outre_mer, membres=membres)
        return menage
