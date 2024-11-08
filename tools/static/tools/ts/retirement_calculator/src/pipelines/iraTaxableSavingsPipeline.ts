import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";

export default class IraTaxableSavingsPipeline implements InvestmentPipeline {
    calculateContribution(row: Row): Row {
        switch (row.iraTaxableContributionStrategy) {
            case 'fixed':
                row.iraTaxableContribution = row.iraTaxableContributionFixedAmount
                return row
            case 'percent_of_income':
                row.iraTaxableContribution = row.incomePreTaxed * (row.iraTaxableContributionPercentage / 100)
                return row
            case 'max':
                row.iraTaxableContribution = Number(row.age) >= 50 ? row.iraContributionCatchUpLimit : row.iraContributionLimit
                return row
        }
    }

    calculateSavingsStartOfYear(row: Row): Row {
        row.iraTaxableSavingsStartOfYear = row.iraTaxableSavingsEndOfYear
        row.iraTaxDeferredSavingsStartOfYear = row.iraTaxDeferredSavingsEndOfYear
        return row
    }

    calculateSavingsEndOfYear(row: Row) {
        row.iraTaxableSavingsEndOfYear = row.iraTaxableSavingsStartOfYear + row.iraTaxableContribution + row.iraTaxableGrowthAmount;
        return row
    }

    calculateGrowthAmount(row: Row): Row {
        switch (row.investmentGrowthStrategy) {
            case 'start':
                row.iraTaxableGrowthAmount = row.iraTaxableSavingsStartOfYear * (row.iraGrowthRate / 100)
                return row
            case 'end':
                row.iraTaxableGrowthAmount = (row.iraTaxableSavingsStartOfYear + row.iraTaxableContribution) * (row.iraGrowthRate / 100)
                return row
        }
        return row
    }

    initialize(row: Row) {
        row.iraTaxableSavingsStartOfYear = row.iraTaxableSavingsStartOfYear ? row.iraTaxableSavingsStartOfYear : 0
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row = this.calculateSavingsEndOfYear(row)
        row.iraTaxableContributionLifetime = row.iraTaxableContribution
        return row
    }

    process(row: Row) {
        row = this.calculateSavingsStartOfYear(row)
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row = this.calculateSavingsEndOfYear(row)
        row.iraTaxableContributionLifetime += row.iraTaxableContribution
        return row

    }
}