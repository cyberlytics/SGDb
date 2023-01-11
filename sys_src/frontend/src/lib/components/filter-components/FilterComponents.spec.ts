import '@testing-library/jest-dom';
import { render, screen, fireEvent} from "@testing-library/svelte";
import Creator from './Creator.svelte';
import Genre from './Genre.svelte';
import Platform from './Platform.svelte';
import Date from './Date.svelte';

const data = [['test_creator1', '1'], ['test_creator2', '2'], ['test_creator3', '3']]
const group = []

describe("Creator inputs", () => {

    test("input checked", async () => {
        render(Creator, { props: { data: data, group: group, color: 'red' } });
        const creatorInput = screen.getAllByTestId('creator-input')[0]
        await fireEvent.click(creatorInput)
        expect(creatorInput).toBeChecked()
    });

  });

describe("Platform inputs", () => {

    test("input checked", async () => {
        render(Platform, { props: { data: data, group: group, color: 'red' } });
        const platformInput = screen.getAllByTestId('platform-input')[0]
        await fireEvent.click(platformInput)
        expect(platformInput).toBeChecked()
    });

});

describe("Genre inputs", () => {

    test("input checked", async () => {
        render(Genre, { props: { data: data, group: group, color: 'red' } });
        const genreInput = screen.getAllByTestId('genre-input')[0] 
        await fireEvent.click(genreInput)
        expect(genreInput).toBeChecked()
    });

});

describe("Date input", () => {

    test("set date",  () => {
        render(Date, { props: { date: 0, color: 'red' } });
        const dateInput = screen.getByTestId('date-input')
        fireEvent.change(dateInput, { target: { value: 2002 } });
        expect(dateInput).toHaveValue('2002')
    });

    test("date already setted",  () => {
        render(Date, { props: { date: 2002, color: 'red' } });
        const dateInput = screen.getByTestId('date-input')
        expect(dateInput).toHaveValue('2002')
    });
});
