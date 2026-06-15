import { c as createComponent, m as maybeRenderHead, u as unescapeHTML, r as renderTemplate } from './astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import 'clsx';

const html = "<p>[Work in Progress]</p>\n<p>This documentation follow the <a href=\"https://diataxis.fr/\">Diataxis</a> system. On your rigth, you can see 4 sections :</p>\n<ul>\n<li><strong>Getting started</strong> :\nall our tutorials, step by step explanations to discover the project</li>\n<li><strong>How to…</strong> :\nall our how to guide for more advanced configuration</li>\n<li><strong>Let’s talk about</strong> :\nall our articles to better understand the “theory” behind the code (architecture, testing philosophy etc…)</li>\n<li><strong>Reference</strong> :\nall our data for future reference (database structure, tools, API etc..)</li>\n</ul>";

				const frontmatter = {"title":"This doc","description":"We need you !"};
				const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/explanation/doc.md";
				const url = undefined;
				function rawContent() {
					return "\n[Work in Progress]\n\nThis documentation follow the [Diataxis](https://diataxis.fr/) system. On your rigth, you can see 4 sections :\n\n- **Getting started** :\n    all our tutorials, step by step explanations to discover the project\n- **How to...** :\n    all our how to guide for more advanced configuration\n- **Let's talk about** :\n    all our articles to better understand the \"theory\" behind the code (architecture, testing philosophy etc...)\n- **Reference** :\n    all our data for future reference (database structure, tools, API etc..)\n";
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
