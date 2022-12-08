import '@testing-library/jest-dom'
import { render, fireEvent, screen } from '@testing-library/svelte'
import Search from './Search.svelte';

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

});


