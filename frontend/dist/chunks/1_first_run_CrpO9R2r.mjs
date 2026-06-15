import { c as createComponent, m as maybeRenderHead, u as unescapeHTML, r as renderTemplate } from './astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import 'clsx';

const html = "<p>Dans ce tutoriel, nous allons lancer prestagri localement pour la première fois.</p>";

				const frontmatter = {"title":"First Run","description":"Tutorial to run prestagri locally"};
				const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/tutorial/1_first_run.md";
				const url = undefined;
				function rawContent() {
					return "\nDans ce tutoriel, nous allons lancer prestagri localement pour la première fois.\n";
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
