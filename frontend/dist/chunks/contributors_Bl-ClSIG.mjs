import { c as createComponent, m as maybeRenderHead, u as unescapeHTML, r as renderTemplate } from './astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import 'clsx';

const html = "<p>Parce que l’open-souce est toujours un travail d’equipe.</p>\n<p>Elles ont contribue (par ordre alphabetique) :</p>\n<ul>\n<li>Erica Delagnier</li>\n<li>Amandine Guegano</li>\n<li>Bouchra Masmoudi</li>\n</ul>";

				const frontmatter = {"title":"Contributeur.ices"};
				const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/contributors.md";
				const url = undefined;
				function rawContent() {
					return "\nParce que l'open-souce est toujours un travail d'equipe.\n\nElles ont contribue (par ordre alphabetique) :\n- Erica Delagnier\n- Amandine Guegano \n- Bouchra Masmoudi\n";
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
