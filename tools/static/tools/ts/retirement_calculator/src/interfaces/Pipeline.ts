import { Row } from './Row';
export interface Pipeline {

    process(row: Row): Row;

}