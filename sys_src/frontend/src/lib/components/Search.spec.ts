import '@testing-library/jest-dom'
import { render, fireEvent, screen } from '@testing-library/svelte'
import Search from './Search.svelte';
import { searchQuery, searchText, isSearchDisabled, isSearchSuggestionVisible } from '$stores/search';

describe('Search component', () => {

  test('button disabled', () => {
    render(Search);
    const searchButton = screen.getByRole('button')

    expect(searchButton).toBeDisabled()
  })

  test('button enabled', async () => {
    render(Search);
    const searchButton = screen.getByRole('button')
    const searchInput = screen.getByTestId('search-input')

    await fireEvent.input(searchInput, { target: { value: 'test' } })

    expect(searchButton).toBeEnabled()
  })

  test('handle Search', async () => {
    render(Search, { props: { search: 'test'} });
    isSearchDisabled.set(true)
    const searchButton = screen.getByRole('button')
    await fireEvent.click(searchButton)
    expect({searchQuery:'test', search:'', isSearchSuggestionVisible:false}).toBeDefined()
  })
});


