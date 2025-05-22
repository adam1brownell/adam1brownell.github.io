# adam1brownell.github.io
Personal Website

Set up local dev:

````
cd astro-blog
npm install
npm run dev 
local host

```

Build before deploy

```
cd astro-blog
npm run build
npm run preview
local host
```

Write pages in `/astro-blog/src/pages/blog/my-post/index.astro`
Put images in `/astro-blog/public/images/chart/png`
<img src="/images/chart.png" alt="My chart" />
Global style in `astro-blog/src/styles/global.css`

```
astro-blog/
├─ src/
│  ├─ content.config.ts
│  ├─ content/
│  │   └─ blog/
│  │      └─ test-post.md    ← blog posts
│  └─ pages/
│     ├─ index.astro         ← blog homepage
│     ├─ about.astro         ← optional About page
│     └─ blog/
│        ├─ index.astro      ← sorted via Date.parse, uses post.data.image + post.url
│        └─ [slug].astro     ← dynamic post renderer
└─ astro.config.mjs
```