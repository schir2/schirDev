import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";
import {assertDefined} from "../utils";

export default class IraTaxableSavingsPipeline implements InvestmentPipeline {

    process(row: Row) {
        assertDefined(row.iraTaxableSavingsEndOfYear,'iraTaxableSavingsEndOfYear')
        row.iraTaxableSavingsStartOfYear = row.iraTaxableSavingsEndOfYear
        row.iraTaxableContribution = row.calculateIraTaxableContribution()
        row.iraTaxableGrowthAmount = row.calculateIraTaxableGrowthAmount()
        row.iraTaxableSavingsEndOfYear = row.calculateIraTaxableSavingsEndOfYear()
        row.iraTaxableContributionLifetime += row.iraTaxableContribution
        return row

    }
}