import { c as createComponent, m as maybeRenderHead, u as unescapeHTML, r as renderTemplate } from './astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import 'clsx';

const html = "<p>Voir la <a href=\"../../../assets/references/note_service.pdf\">note de service</a></p>";

				const frontmatter = {"title":"Note de service"};
				const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/note_service.md";
				const url = undefined;
				function rawContent() {
					return "\nVoir la [note de service](../../../assets/references/note_service.pdf)";
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
