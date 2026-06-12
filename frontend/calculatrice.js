let calculForm = document.getElementById("calculForm");
calculForm.addEventListener("submit", (e) => {
  e.preventDefault();
  fetch(
    "http://localhost:8000/quotient_familial?" +
    "agent_revenu="+ document.getElementById('agent_revenu').value +"&"+
    "agent_enfants="+ document.getElementById('agent_enfants').value +"&"+
    "conjoint_revenu="+ document.getElementById('conjoint_revenu').value +"&"+
    "conjoint_enfants="+ document.getElementById('conjoint_enfants').value +"&"+
    "etudiant_revenu=0&"+
    "etudiant_enfants=0&"+
    "personne_ou_enfant_porteur_handicap="+ document.getElementById('personne_ou_enfant_porteur_handicap').value +"&"+
    "garde_alternee="+ document.getElementById('garde_alternee').value +"&"+
    "parent_isole="+ document.getElementById('parent_isole').value +"&"+
    "outre_mer="+ document.getElementById('outre_mer').value
   )
  .then((response) => {
    if (!response.ok) {
        throw new Error(`On a un souci, contactez le support`);
    }
    return response.json()
  })
  .then((data) => {
    document.getElementById("answer").style.display="block";
    document.getElementById('value').textContent = "Le quotient famillial est de " + data.value + "€"
    document.getElementById('explanation').textContent = data.explanation 
  })
});