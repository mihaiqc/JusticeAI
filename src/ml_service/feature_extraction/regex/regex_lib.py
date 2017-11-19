# -*- coding: utf-8 -*-
import re


class RegexLib:
    regex_demands = [
        ("tenant_eviction", re.compile(r".*(locat(eur(s)?|rice(s)?)).*(expulsion|éviction).*locataire(s)?")),
        ("landlord_lease_termination", re.compile(r".*(locat(eur(s)?|rice(s)?)).*.+résiliation.+bail")),
        ("tenant_cover_rent", re.compile(r".*(demande(nt)?.+)?(locat(eur(s)?|rice(s)?))(s)?(.+demande(nt)?)?.+recouvrement\s(du|de)\sloyer")),
        ("paid_judicial_fees", re.compile(r".*(locat(eur(s)?|rice(s)?))\sdemande(nt)?.+(frais\sjudiciaires)")),
        ("landlord_money_cover_rent", re.compile(r".*(locat(eur(s)?|rice(s)?)).+(demand(e|ent))?.+recouvrement.+\sloyer")),
        ("landlord_fix_rent", re.compile(r".*(locat(eur(s)?|rice(s)?)).+(demand(e|ent)).+(fix(er|ation)).+loyer")),
        ("tenant_demands_money", re.compile(r".*locataire(s)?.+(demand(ait|ent|e)).+\b(\d{1,3}(\s\d{3}|,\d{2})*)+(\$|\s\$)")),
        ("tenant_claims_harassment", re.compile(r".*locataire(s)?.+(demand(ait|ent|e)).+dommages.+harcèlement")),
        ("landlord_demand_utility_fee", re.compile(r".*recouvrement(.+frais.+(énergie|électricité))+")),
        ("landlord_demand_legal_fees", re.compile(r".*demande(nt)?.*remboursement.+(frais)?judiciaires")),
        ("landlord_demand_bank_fee", re.compile(r".*recouvrement.*frais\sbancaire(s)?")),
        ("landlord_demand_retake_apartment", re.compile(r".*(locat(eur(s)?|rice(s)?)).*demand(e|ent).+(autoris(er|ation)).+reprendre.+logement")),
        ("landlord_claim_interest_damage", re.compile(r".*(locat(eur(s)?|rice(s)?)).*\b(\d{1,3}(\s\d{3}|,\d{2})*)+(\$|\s\$).*(dommages-intérêts)")),
        ("tenant_demand_rent_decrease", re.compile(r".*(locataire(s)?).*demande.*diminution.*loyer")),
        ("tenant_demand_interest_damage", re.compile(r".*(locataire(s)?).*demande(nt)?.*(dommages-intérêts)")),
        ("tenant_demand_indemnity_damage", re.compile(r".*locataire(s)?.*(l'indemnité\sadditionnelle)")),
        ("tenant_respect_of_contract", re.compile(r".*locataire(s)?.*(exécution\sen\snature\sd'une\sobligation)")),
        ("tenant_demand_indemnity_judicial_fee", re.compile(r"locataire(s)?.+(recouvrement\sdes\sfrais\sjudiciaires)")),
        ("tenant_demand_indemnity_Code_Civil", re.compile(r".*locataire(s)?.*demande.*(Code\scivil\sdu\sQuébec)")),
        ("landlord_demand_damage", re.compile(r".*(locat(eur(s)?|rice(s)?)).+(demand(ent|e)).+dommage(s)?")),
        ("tenant_demands_decision_retraction", re.compile(r".*locataire(s)?.+demande.+rétractation.+décision"))
    ]

    regex_facts = [
        ("tenant_lease_indeterminate", re.compile(r".*bail.+(durée\sindéterminée).*")),
        ("tenant_lease_fixed", re.compile(r".*((bail.*(reconduit.*)?(terminant.*)?((\d+?\w*?\s+?|)(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)(\s+\d{2,4}|))((.+au|.*terminant).*(\d+?\w*?\s+?|)(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)(\s+\d{2,4}|))?)|(fixation\sde\sloyer))")),
        ("tenant_monthly_payment", re.compile(r"..*loyer\smensuel.*\b(\d{1,3}(\s\d{3}|,\d{2})*)+(\$|\s\$).*")),
        ("tenant_owes_rent", re.compile(r"(.*preuve.+locateur(s)?.+non-paiement.+loyer)?.*(locataire(s)?.+(doi(vent|t))((.+somme\sde)|(total))?.+([\d\s,]+)(\$|\s\$)|locateur.+créance.+\b(\d{1,3}(\s\d{3}|,\d{2})*)+(\$|\s\$).+loyers\simpayés)|(.*paiement.*arriérés.+loyer.+\b(\d{1,3}(\s\d{3}|,\d{2})*))")),
        ("tenant_rent_not_paid_more_3_weeks", re.compile(r".*locataire(s)?.+retard.+plus.+((trois semaines)|(trois \(3\) semaines)).+(paiement\sdu\sloyer)")),
        ("tenant_violence", re.compile(r".*(raison.+)?.*(viol(ent|ence))")),
        #("tenant_request_cancel_lease", re.compile(r"")),
        ("tenant_not_request_cancel_lease", re.compile(r".*jamais.+(résiliation\sde\sbail).*")),
        #("tenant_pay_before_judgment", re.compile(r"")),
        ("tenant_group_responsability", re.compile(r".*bail.+(prévoit\spas).+locataire(s)?.+(solidairement\sresponsables).+(locat(eur(s)?|rice(s)?)).*")),
        ("tenant_individual_responsability", re.compile(r".*bail.+(prévoit).+locataire(s)?.+(solidairement\sresponsables).+(locat(eur(s)?|rice(s)?)).*")),
        ("tenant_withold_rent_without_permission", re.compile(r".*locataire(s)?.+(ne\speut).+(faire\sjustice).+retenir.+loyer.+(sans.+Tribunal)?.*")),
        ("landlord_prejudice_justified", re.compile(r".*(cause.+)?préjudice(causé)?.+((locat(eur(s)?|rice(s)?))|demanderesse)?(justifie.+décision|sérieux).*")),
        #("landlord_not_prejudice_justified", re.compile(r"")),
        ("tenant_bad_payment_habits", re.compile(r".*(retard(s)?.+)?(loyer.+)?(payé|paient|paiement)(.+loyer)?(.+retard(s)?)?.*")),
        ("tenant_financial_problem", re.compile(r".*(locataire(s)?.+)?difficultés.+financières(.+locataire(s)?)?.*")),
        ("landlord_rent_change", re.compile(r".*l'ajustement.+loyer.*")),
        ("landlord_rent_change_doc_renseignements", re.compile(r".*formulaire\s(r|R)enseignements.+loyer.*")),
        ("landlord_rent_change_piece_justification", re.compile(r".*formulaire\s(r|R)enseignements.+loyer.+(pièces\sjustificatives).*")),
        ("landlord_rent_change_receipts", re.compile(r".*formulaire\s(r|R)enseignements.+loyer.+(pièces\sjustificatives).+factures.*")),
        ("tenant_lacks_proof", re.compile(r".*considérant\sl'absence.+\;.*")),
        ("landlord_retakes_apartment", re.compile(r".*(locat(eur(s)?|rice(s)?)).+(reprendre|reprise)(.+logement)?.*")),
        ("landlord_notifies_tenant_retake_apartment", re.compile(r".*(locat(eur(s)?|rice(s)?)).+locataire(s)?.+(reprendre|reprise).+logement.*")),
        ("tenant_refuses_retake_apartment", re.compile(r".*locataire(s)?.+refus(e|ait|aient).+quitter.*")),
        ("landlord_sends_demand_regie_logement", re.compile(r".*(locat(eur(s)?|rice(s)?)).+demande.+(Régie\sdu\slogement).*")),
        ("landlord_sends_demand_regie_logement", re.compile(r".*(locat(eur(s)?|rice(s)?)).+demande.+(Régie\sdu\slogement).*")),
        #("tenant_claims_harm", re.compile(r"")),
        ("landlord_retakes_apartment_indemnity", re.compile(r".*compenser.+frais.+déménagement.*")),
        ("tenant_left_without_paying", re.compile(r".*(((départ.+|défaut.+|déguerpissement.+).*locataire(s)?)|(locataire(s)?.*quitté?))")),
        ("tenant_rent_not_paid_less_3_weeks", re.compile(r".*locataire(s)?.+pas.+retard.+(trois\ssemaines).+paiement.+loyer.*")),
        ("tenant_rent_paid_before_hearing", re.compile(r".*locataire(s)?.*payé.*loyer.*(dû le jour|avant).+(audience).*")),
        ("landlord_inspector_fees", re.compile(r".*(locat(eur(s)?|rice(s)?)).+(frais\sde\sdépistage).*")),
        ("landlord_relocation_indemnity_fees", re.compile(r".*(locat(eur|rice)(s))?.+réclame.+indemnité.*\b(\d{1,3}(\s\d{3}|,\d{2})*)+(\$|\s\$).*")),
        #("tenant_is_asshole", re.compile(r"")),
        ("tenant_continuous_late_payment", re.compile(r".*(fréquen(ce|ts)).*(retard(s)?)?.*(article\s1971)?")),
        ("tenant_landlord_agreement", re.compile(r".*entente.+(entre\sles\sdeux\sparties).*")),
        ("landlord_pays_indemnity", re.compile(r".*dédommage.+locataire(s)?.*")),
        ("apartment_impropre", re.compile(r".*(logement(était\s)?(.+impropre|infesté).+l'habitation|(bon\sétat.+propreté)).*")),
        ("landlord_is_a_rapist", re.compile(r".*violentée|violent(e)?|menaçant(e)?.*")),
        ("landlord_is_violent", re.compile(r".*violentée|violent(e)?|menaçant(e)?.*")),
        ("apartment_infestation", re.compile(r".*infestation(s)?|rat(s)?|fourmi(s)?|coquerelle(s)?|souri(s)?|excrément(s)?.*")),
        ("tenant_declare_insalubre", re.compile(r".*(locataire(s).+)?(apartment.+)?insalubre.*"))
    ]
