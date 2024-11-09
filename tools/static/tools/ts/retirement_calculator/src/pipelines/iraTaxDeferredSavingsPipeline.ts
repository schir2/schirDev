import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";
import {assertDefined} from "../utils";

export default class IraTaxDeferredSavingsPipeline implements InvestmentPipeline {

    process(row: Row) {
        assertDefined(row.savingsEndOfYear, 'savingsEndOfYear')
        row.savingsStartOfYear = row.savingsEndOfYear
        row.iraTaxDeferredContribution = row.calculateIraDeferredContribution()
        row.iraTaxDeferredGrowthAmount = row.calculateIraTaxDeferredGrowthAmount()
        row.iraTaxDeferredSavingsEndOfYear = row.calculateIraTaxDeferredSavingsEndOfYear()
        row.iraTaxDeferredContributionLifetime += row.iraTaxDeferredContribution
        row.savingsEndOfYear += row.iraTaxDeferredContribution + row.iraTaxDeferredGrowthAmount
        return row
    }
}