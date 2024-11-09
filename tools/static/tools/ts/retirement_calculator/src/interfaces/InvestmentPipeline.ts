import { Row } from './Row';
export interface InvestmentPipeline {
    process(row: Row): Row;
}