---
title: Dev Q/A
description: Bug diary
---

This file is used as a reference for any bug encountered during the project. The
goal is to take the time to reflect on what was learned while solving it and
identify recurring ones. Copy the following template to add a new bug
description.

______________________________________________________________________

##  in get_dn_dossier return parse_dn_dossier(r.json()["data"]["dossier"]) TypeError: 'NoneType' object is not subscriptable


*how long* :

*what happened* : error 401 when calling the DN API

*why* : Token expired

*what did i do to fix it* : in DN, profil administrateur, voir mon profil, jeton d'identification de l'API
*how often* : depending on the validity of the token every ~6 month
