import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";
import {assertDefined} from "../utils";

export default class TaxableSavingsPipeline implements InvestmentPipeline {

    process(row: Row) {
        assertDefined(row.taxableSavingsEndOfYear, 'taxableSavingsEndOfYear')
        row.taxableSavingsStartOfYear = row.taxableSavingsEndOfYear
        row.taxableContribution = row.calculateTaxableContribution()
        row.taxableGrowthAmount = row.calculateTaxableGrowthAmount()
        row.taxableContributionLifetime += row.taxableContribution
        row.taxableSpending += row.taxableContribution
        row.taxableSavingsEndOfYear = row.calculateTaxableSavingsEndOfYear()
        row.savingsEndOfYear += row.taxableContribution + row.taxableGrowthAmount
        return row

    }
}