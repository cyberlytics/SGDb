import { writable} from 'svelte/store';


export const isFilterVisible = writable(false);
export const isFilterDisabled = writable(true);
export const isApplyDisabled = writable(false);
export const isInputDisabled = writable(false);
export const isPost = writable(false);

export let filter_data = writable("");
export let graphData = writable("");
export let filterSettings = writable("");

//append dict values to an array in order to be able to process them in the respective class
export function toArray(data){
    let dict = new Map();
    for (var key in data){
        for(var k in data[key]){
            dict.set(k, data[key][k])
        }
    }
    return dict;
}
