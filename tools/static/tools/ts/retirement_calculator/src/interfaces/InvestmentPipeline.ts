import { Row } from './Row';
export interface InvestmentPipeline {

    initialize(row: Row): Row;
    process(row: Row): Row;
    calculateSavingsStartOfYear(row: Row): Row;
    calculateContribution(row: Row): Row;
    calculateSavingsEndOfYear(row: Row): Row;
    calculateGrowthAmount(row: Row): Row;


}