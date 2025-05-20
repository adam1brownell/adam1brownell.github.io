import { defineConfig } from 'astro/config';

export default defineConfig({
  // this must be the full canonical URL of your live site:
  site: 'https://adambrownell.com',
  base: '/blog/',
  outDir: '../blog',
});