import '@testing-library/jest-dom';
import {render, screen, fireEvent} from "@testing-library/svelte";
import Tags from './Tags.svelte';


describe("Tag components", () => {
    test('display date tag', () => {
        render(Tags, { props: { date: 2002, group: ['Test'], color: 'red' } });
        const dateTag = screen.getByTestId('date-tag')
        expect(dateTag).toHaveTextContent('2002')
      })
    test('display chechbox tag', () => {
        render(Tags, { props: {date: 2002, group: ['Test'], color: 'red' } });
        const dateTag = screen.getByTestId('checkbox-tag')
        expect(dateTag).toHaveTextContent('Test')
    })
    test('delete checkbox tag', async () => {
        render(Tags, { props: { date: 2002, group: ['test'], color: 'red' } });
        const deleteGroup = screen.getByTestId('checkbox-tag-button')
        await fireEvent.click(deleteGroup)
        expect(deleteGroup).not.toBeInTheDocument()
    })
    test('delete date tag', async () => {
        render(Tags, { props: { date: 2002, group: ['Test'], color: 'red' } });
        const deleteDate = screen.getByTestId('date-tag-button')
        await fireEvent.click(deleteDate)
        expect(deleteDate).not.toBeInTheDocument()
    })

  });
