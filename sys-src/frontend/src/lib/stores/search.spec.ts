import { get } from 'svelte/store';
import { searchQuery } from '$stores/search';

describe('Search store', () => {

  it('should have an empty string as the initial value in searchQuery', () => {
    const value = get(searchQuery);
    expect(value).toEqual('');
  });

  it('should update the searchQuery value', () => {
    searchQuery.set('test');
    const value = get(searchQuery);
    expect(value).toBe('test');
  });

});
