import { defineConfig } from 'astro/config';
import fs from 'fs';

export default defineConfig({
  site: 'https://adambrownell.com',
  base: '/myblog',
  hooks: {
    'astro:build:done': () => {
      fs.copyFileSync('public/CNAME', 'dist/CNAME');
    },
  },
});