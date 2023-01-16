import '@testing-library/jest-dom';
import { fireEvent, render, screen } from "@testing-library/svelte";
import Navbar from './Navbar.svelte';
import { isFilterVisible } from '$stores/filter';

describe('Navbar component', () => {

  test('filter button', () => {
    render(Navbar);
    const filterButton = screen.getByTestId('filter-button');

    expect(filterButton).toBeEnabled();
  })

  test('handle click', async() => {
    render(Navbar);
    const filterButton = screen.getByTestId('filter-button');
    await fireEvent.click(filterButton)
    expect(isFilterVisible).toBeTruthy()
  })


});
