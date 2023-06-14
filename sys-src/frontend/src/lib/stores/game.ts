import { writable } from 'svelte/store';

export const isDetailsVisible = writable(false);
export const selectedGame = writable('');
