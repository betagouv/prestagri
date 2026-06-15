import { c as createComponent, m as maybeRenderHead, u as unescapeHTML, r as renderTemplate } from './astro/server_BskC6SXv.mjs';
import 'kleur/colors';
import 'clsx';

const html = "<p>This file is used as a reference for any bug encountered during the project. The\ngoal is to take the time to reflect on what was learned while solving it and\nidentify recurring ones. Copy the following template to add a new bug\ndescription.</p>\n<hr>\n<h2 id=\"bug-description\">Bug description</h2>\n<p><em>how long</em> :</p>\n<p><em>what happened</em> :</p>\n<p><em>why</em> :</p>\n<p><em>what did i do to fix it</em> :</p>\n<p><em>how often</em> :</p>";

				const frontmatter = {"title":"Dev Q/A","description":"Bug diary"};
				const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/reference/what_did_I_do_then.md";
				const url = undefined;
				function rawContent() {
					return "\nThis file is used as a reference for any bug encountered during the project. The\ngoal is to take the time to reflect on what was learned while solving it and\nidentify recurring ones. Copy the following template to add a new bug\ndescription.\n\n______________________________________________________________________\n\n## Bug description\n\n*how long* :\n\n*what happened* :\n\n*why* :\n\n*what did i do to fix it* :\n\n*how often* :\n";
				}
				function compiledContent() {
					return html;
				}
				function getHeadings() {
					return [{"depth":2,"slug":"bug-description","text":"Bug description"}];
				}

				const Content = createComponent((result, _props, slots) => {
					const { layout, ...content } = frontmatter;
					content.file = file;
					content.url = url;

					return renderTemplate`${maybeRenderHead()}${unescapeHTML(html)}`;
				});

export { Content, compiledContent, Content as default, file, frontmatter, getHeadings, rawContent, url };
