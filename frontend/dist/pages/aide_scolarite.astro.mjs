import { c as createComponent, b as renderComponent, r as renderTemplate, m as maybeRenderHead } from '../chunks/astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import { $ as $$DsfrLayout } from '../chunks/dsfrLayout_BwcXtYtu.mjs';
export { renderers } from '../renderers.mjs';

const $$AideScolarite = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${renderComponent($$result, "DsfrLayout", $$DsfrLayout, {}, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<div class="fr-container fr-mt-8v fr-mt-md-14v fr-mb-2v fr-mb-md-8v"> <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--center"> <div class="fr-col-12 fr-col-md-10 fr-col-lg-8"> <h2>Calcul de l'aide a la scolarité</h2> <p class="fr-text--lead">Renseignez les informations fournies par l'agent dans son dossier</p> </div> </div> </div> <div class="fr-container fr-container--fluid fr-mb-md-14v"> <div class="fr-grid-row fr-grid-row-gutters fr-grid-row--center"> <div class="fr-col-12 fr-col-md-10 fr-col-lg-8"> <div class="fr-alert fr-alert--info"> <h3 class="fr-alert__title">Calculatrice en cours de création</h3> <p>Ce calcul n'est pas encore disponible mais nous espérons pouvoir vous le proposer tres bientot !</p> <button title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert)" type="button" class="fr-btn--close fr-btn">Masquer le message</button> </div> </div> </div> </div> ` })}`;
}, "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/pages/aide_scolarite.astro", void 0);

const $$file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/pages/aide_scolarite.astro";
const $$url = "/aide_scolarite";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
    __proto__: null,
    default: $$AideScolarite,
    file: $$file,
    url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
