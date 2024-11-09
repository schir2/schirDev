import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";
import {Row} from "../interfaces/Row";
import {assertDefined} from "../utils";

export default class TaxDeferredEmployerPipeline implements InvestmentPipeline {

    process(row: Row) {
        assertDefined(row.taxDeferredSavingsEndOfYear, 'taxDeferredSavingsEndOfYear')
        row.taxDeferredSavingsStartOfYear = row.taxDeferredSavingsEndOfYear
        row.employerContribution = row.calculateEmployerContribution();
        row.employerContributionLifetime += row.employerContribution
        row.taxDeferredGrowthAmount = row.calculateGrowthAmount()
        row.taxDeferredSavingsEndOfYear = row.calculateSavingsEndOfYear();
        return row;
    }
}