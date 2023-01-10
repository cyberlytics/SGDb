import '@testing-library/jest-dom';
import { render, screen, fireEvent, waitFor, getByTestId, getByRole, getByText} from "@testing-library/svelte";
import FilterModal from './FilterModal.svelte';

describe('Filter Modal component', () => {

  test('close button enabled',  () => {
    render(FilterModal);
    const closeButton = screen.getByTestId('close-button')
    expect(closeButton).toBeEnabled()
  })

  test('apply button disabled', () => {
    render(FilterModal);
    const applyButton = screen.getByTestId('apply-button')
    expect(applyButton).toBeDisabled()
  })
  test('cancel button enabled', () => {
    render(FilterModal);
    const cancelButton = screen.getByTestId('cancel-button')
    expect(cancelButton).toBeEnabled()
    })
});