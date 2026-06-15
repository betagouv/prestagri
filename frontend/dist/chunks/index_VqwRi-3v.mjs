const id = "index.mdx";
						const collection = "docs";
						const slug = "index";
						const body = "\nimport { Card, CardGrid } from '@astrojs/starlight/components';\n\n<CardGrid stagger>\n    <Card title=\"Api de test\" icon=\"add-document\">\n      [Documentation OpenAPI [version de test]](https://prestagri-staging.osc-fr1.scalingo.io/docs)\n    </Card>\n    <Card title=\"Setup Prest'Agri\" icon=\"add-document\">\n      [First Run tutorial](/prestagri/tutorial/1_first_run)\n    </Card>\n</CardGrid>\n";
						const data = {title:"Welcome to the Prest'Agri Doc",description:"prestagri - Doc",editUrl:true,head:[],template:"splash",hero:{tagline:"Simplifier les demandes de prestations sociales des agents du ministère de l'Agriculture et de la Souveraineté alimentaire",image:{alt:"",file:
						new Proxy({"src":"/_astro/houston.CZZyCf7p.webp","width":800,"height":800,"format":"webp","fsPath":"/home/erica/Multi/projets/prestagri/prestagri/frontend/src/assets/houston.webp"}, {
						get(target, name, receiver) {
							if (name === 'clone') {
								return structuredClone(target);
							}
							if (name === 'fsPath') {
								return "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/assets/houston.webp";
							}
							if (target[name] !== undefined && globalThis.astroAsset) globalThis.astroAsset?.referencedImages.add("/home/erica/Multi/projets/prestagri/prestagri/frontend/src/assets/houston.webp");
							return target[name];
						}
					})
					},actions:[]},sidebar:{hidden:false,attrs:{}},pagefind:true,draft:false};
						const _internal = {
							type: 'content',
							filePath: "/home/erica/Multi/projets/prestagri/prestagri/frontend/src/content/docs/index.mdx",
							rawData: undefined,
						};

export { _internal, body, collection, data, id, slug };
