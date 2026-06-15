import { c as createComponent, m as maybeRenderHead, u as unescapeHTML, r as renderTemplate } from './astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import 'clsx';

const html = "<p>Documentation du champ permettant de faire des appels API depuis DN : <a href=\"https://doc.demarche.numerique.gouv.fr/tutoriels/champ-referentiel-avance-a-configurer\">https://doc.demarche.numerique.gouv.fr/tutoriels/champ-referentiel-avance-a-configurer</a></p>";

				const frontmatter = {"title":"Demarches Numeriques"};
				const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/dn.md";
				const url = undefined;
				function rawContent() {
					return "\nDocumentation du champ permettant de faire des appels API depuis DN : https://doc.demarche.numerique.gouv.fr/tutoriels/champ-referentiel-avance-a-configurer";
				}
				function compiledContent() {
					return html;
				}
				function getHeadings() {
					return [];
				}

				const Content = createComponent((result, _props, slots) => {
					const { layout, ...content } = frontmatter;
					content.file = file;
					content.url = url;

					return renderTemplate`${maybeRenderHead()}${unescapeHTML(html)}`;
				});

export { Content, compiledContent, Content as default, file, frontmatter, getHeadings, rawContent, url };
