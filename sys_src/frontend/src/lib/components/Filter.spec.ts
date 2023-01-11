import '@testing-library/jest-dom';
import { render, screen, fireEvent, waitFor, getByTestId, getByRole, getByText} from "@testing-library/svelte";
import Filter from './Filter.svelte';
import {filterSettings, isApplyDisabled, isInputDisabled, filter_data, toArray} from '$stores/filter.ts';

describe('Filter component', () => {
    const data = {
        'creator': [{'test': 20}, {'test1': 21}, {'test2': 22}],
        'platform': [{'test': 20}, {'test1': 21}, {'test2': 22}],
        'genre': [{'test': 20}, {'test1': 21}, {'test2': 22}],}
  
    test('render empty data',  () => {
        render(Filter, { props: { creator: [], platform: [], genre: []} });
    })
    test('tags and set data check',  () => {
        filter_data.set(data)
        render(Filter, { props: { creator: ['test', 'test1'], platform: ['test', 'test1'], genre: ['test', 'test1']} });
        const inputs = screen.findByTestId('tags')
        expect(inputs).toBeDefined()
    })

    test('render empty creator',  () => {
        render(Filter, { props: { creator: [], platform: ['test', 'test1'], genre: ['test', 'test1']} });
    })
    test('render empty platform',  () => {
        render(Filter, { props: { creator: ['test', 'test1'], platform: [], genre: ['test', 'test1']} });
    })
    test('render empty genre',  () => {
        render(Filter, { props: { creator: ['test', 'test1'], platform: ['test', 'test1'], genre: []} });
    })
});