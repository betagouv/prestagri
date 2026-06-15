import { c as createComponent, m as maybeRenderHead, u as unescapeHTML, r as renderTemplate } from './astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import 'clsx';

const html = "<p>L’environnement de test est deploye par la Ruche sur <a href=\"https://dashboard.scalingo.com/apps/osc-fr1/prestagri-staging\">Scaligo</a>\nLa surveillance des erreurs et l’acces aux logs se fait via <a href=\"https://multicoop.sentry.io/issues/?environment=staging&#x26;project=4511309425803344\">Sentry</a></p>\n<p>Dans ce tutoriel, nous allons lancer prestagri localement pour la première fois.</p>";

				const frontmatter = {"title":"Environnement de test","description":"Presentation du serveur et des outils"};
				const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/1_staging.md";
				const url = undefined;
				function rawContent() {
					return "\nL'environnement de test est deploye par la Ruche sur [Scaligo](https://dashboard.scalingo.com/apps/osc-fr1/prestagri-staging)\nLa surveillance des erreurs et l'acces aux logs se fait via [Sentry](https://multicoop.sentry.io/issues/?environment=staging&project=4511309425803344)\n\nDans ce tutoriel, nous allons lancer prestagri localement pour la première fois.\n";
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
