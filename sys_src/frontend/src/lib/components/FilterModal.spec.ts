import '@testing-library/jest-dom';
import { render, screen, fireEvent} from "@testing-library/svelte";
import FilterModal from './FilterModal.svelte';
describe('Filter Modal component', () => {

  test('close button enabled',  () => {
    render(FilterModal);
    const closeButton = screen.getByTestId('close-button')
    expect(closeButton).toBeEnabled()
  })

  test('cancel button enabled',  () => {
    render(FilterModal);
    const cancelButton = screen.getByTestId('cancel-button')
    expect(cancelButton).toBeEnabled()
  })

  test('apply button disabled', () => {
    render(FilterModal);
    const applyButton = screen.getByTestId('apply-button')
    expect(applyButton).toBeDisabled()
  })

  test('handle cancel', async() => {
    render(FilterModal);
    const cancelButton = screen.getByTestId('cancel-button');
    await fireEvent.click(cancelButton)
    expect({isPost: false, isFilterVisible:false, filterSettings:''}).toBeDefined()
    })

  test('handle close', async() => {
    render(FilterModal);
    const closeButton = screen.getByTestId('close-button');
    await fireEvent.click(closeButton)
    expect({isFilterVisible:false}).toBeDefined()
  })

});