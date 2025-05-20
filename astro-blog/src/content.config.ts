// src/content.config.ts
import { defineCollection, z } from 'astro:content';

export const collections = {
  blog: defineCollection({
    schema: z.object({
      title:    z.string(),
      pubDate:  z.string(),
      description: z.string().optional(),
      image:      z.string().optional(),
    }),
  }),
};

