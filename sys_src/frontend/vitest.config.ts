import { defineConfig } from 'vitest/config'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import { resolve } from 'path';

export default defineConfig({
  resolve: {
    alias: {
      $lib: resolve(__dirname, 'src/lib'),
      $components: resolve(__dirname, './src/lib/components'),
      $utils: resolve(__dirname, './src/lib/utils'),
      $stores: resolve(__dirname, './src/lib/stores')
    },
  },
  plugins: [svelte({ hot: !process.env.VITEST })],
  test: {
    include: ['src/**/*.{test,spec}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}'],
    globals: true,
    environment: 'jsdom',
    coverage: {
      reporter: ['text', 'html'],
    },
  },
})