import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";
import {assertDefined} from "../utils";

export default class TaxDeferredPipeline implements InvestmentPipeline {

    process(row: Row) {
        assertDefined(row.taxDeferredSavingsEndOfYear,'taxDeferredSavingsEndOfYear' )
        row.taxDeferredSavingsStartOfYear = row.taxDeferredSavingsEndOfYear
        row.taxDeferredContribution = row.calculateTaxDeferredContribution()
        row.taxDeferredGrowthAmount = row.calculateTaxDeferredGrowthAmount()
        row.taxDeferredContributionLifetime += row.taxDeferredContribution
        row.taxDeferredSpending += row.taxDeferredContribution
        row.taxDeferredSavingsEndOfYear = row.calculateTaxDeferredSavingsEndOfYear();
        return row;
    }
}