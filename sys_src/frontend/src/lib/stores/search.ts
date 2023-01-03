import { writable, derived } from 'svelte/store';

export const searchQuery = writable('');
export const searchText = writable('');
export const isSearchDisabled = writable(true);
export const isSearchSuggestionVisible = derived([isSearchDisabled], ([$isSearchDisabled]) => !$isSearchDisabled);