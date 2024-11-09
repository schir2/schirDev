import {Row} from './Row';

export interface Process {

    process(row: Row): Row;

}