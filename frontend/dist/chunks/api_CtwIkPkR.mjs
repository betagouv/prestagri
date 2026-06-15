import { c as createComponent, m as maybeRenderHead, u as unescapeHTML, r as renderTemplate } from './astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import 'clsx';

const html = "<p><a href=\"https://particulier.api.gouv.fr/\">Particulier API</a></p>";

				const frontmatter = {"title":"Les API a disposition"};
				const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/api.md";
				const url = undefined;
				function rawContent() {
					return "\n[Particulier API](https://particulier.api.gouv.fr/)";
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
