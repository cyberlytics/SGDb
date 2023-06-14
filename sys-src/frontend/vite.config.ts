import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import { resolve } from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      $lib: resolve(__dirname, 'src/lib'),
      $components: resolve(__dirname, './src/lib/components'),
      $utils: resolve(__dirname, './src/lib/utils'),
      $stores: resolve(__dirname, './src/lib/stores')
    },
  },
  plugins: [svelte()],
  server: {
    port: 8080
  }
})
