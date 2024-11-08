import { Row } from './Row';
export interface Pipeline {

    initialize(row: Row): Row;
    process(row: Row): Row;

}