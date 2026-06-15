import { l as createVNode, F as Fragment, _ as __astro_tag_component__ } from './astro/server_BskC6SXv.mjs';
import '@astrojs/internal-helpers/path';
import { b as $$Image, c as $$Card, d as $$CardGrid } from './route-data_C5oJZjyo.mjs';
import 'clsx';

const frontmatter = {
  "title": "Welcome to the Prest'Agri Doc",
  "description": "prestagri - Doc",
  "template": "splash",
  "hero": {
    "tagline": "Simplifier les demandes de prestations sociales des agents du ministère de l'Agriculture et de la Souveraineté alimentaire",
    "image": {
      "file": "../../assets/houston.webp"
    }
  }
};
function getHeadings() {
  return [];
}
const __usesAstroImage = true;
function _createMdxContent(props) {
  return createVNode($$CardGrid, {
    stagger: true,
    children: [createVNode($$Card, {
      title: "Api de test",
      icon: "add-document",
      "set:html": "<p><a href=\"https://prestagri-staging.osc-fr1.scalingo.io/docs\">Documentation OpenAPI [version de test]</a></p>"
    }), createVNode($$Card, {
      title: "Setup Prest'Agri",
      icon: "add-document",
      "set:html": "<p><a href=\"/prestagri/tutorial/1_first_run\">First Run tutorial</a></p>"
    })]
  });
}
function MDXContent(props = {}) {
  const {wrapper: MDXLayout} = props.components || ({});
  return MDXLayout ? createVNode(MDXLayout, {
    ...props,
    children: createVNode(_createMdxContent, {
      ...props
    })
  }) : _createMdxContent();
}
const url = "src/content/docs/index.mdx";
const file = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/index.mdx";
const Content = (props = {}) => MDXContent({
  ...props,
  components: { Fragment: Fragment, ...props.components, "astro-image":  props.components?.img ?? $$Image },
});
Content[Symbol.for('mdx-component')] = true;
Content[Symbol.for('astro.needsHeadRendering')] = !Boolean(frontmatter.layout);
Content.moduleId = "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/index.mdx";
__astro_tag_component__(Content, 'astro:jsx');

export { Content, __usesAstroImage, Content as default, file, frontmatter, getHeadings, url };
