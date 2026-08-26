import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
    vite: {
    css: {
          lightningcss: {
            errorRecovery: true,
          },
        },
    },
    site: 'https://doc.prest-agri.beta.gouv.fr/',
    integrations: [
        starlight({
            title: 'Prest\'Agri-DOC',
            sidebar: [
                {
                    label: 'Tutoriels',
                    items: [{autogenerate: { directory: 'tutorial' }}],

                    // items: [
                        // Each item here is one entry in the navigation menu.
                       // { label: 'Example Guide', link: '/guides/example/' },
                    //],
                },
                {
                    label: 'Guides',
                    items: [{autogenerate: { directory: 'guide' }}],

                    // items: [
                        // Each item here is one entry in the navigation menu.
                       // { label: 'Example Guide', link: '/guides/example/' },
                    //],
                },
                {
                    label: 'Références',
                    items: [{autogenerate: { directory: 'reference' }}],
                },
                {
                    label: 'Explications',
                    items: [{autogenerate: { directory: 'explanation' }}],
                },
            ],
        }),
    ],
});
