import '@testing-library/jest-dom';
import { render, screen } from "@testing-library/svelte";
import Navbar from './Navbar.svelte';

describe('Navbar component', () => {

  test('filter button', () => {
    render(Navbar);
    const filterButton = screen.getByTestId('filter-button');

    expect(filterButton).toBeEnabled();
  })

});
