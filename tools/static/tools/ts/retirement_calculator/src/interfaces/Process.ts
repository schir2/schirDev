import { Row } from './Row';
export interface Process {

    initialize(row: Row): Row;
    process(row: Row): Row;

}