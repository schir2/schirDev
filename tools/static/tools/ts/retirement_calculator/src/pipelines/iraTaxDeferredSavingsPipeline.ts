import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";

export default class IraTaxDeferredSavingsPipeline implements InvestmentPipeline {
    calculateContribution(row: Row): Row {
        switch (row.iraTaxDeferredContributionStrategy) {
            case 'fixed':
                row.iraTaxDeferredContribution = row.iraTaxDeferredContributionFixedAmount
                return row
            case 'percent_of_income':
                row.iraTaxDeferredContribution = row.incomePreTaxed * (row.iraTaxDeferredContributionPercentage / 100)
                return row
            case 'max':
                row.iraTaxDeferredContribution = Number(row.age) >= 50 ? row.iraContributionCatchUpLimit : row.iraContributionLimit
                return row
        }
    }

    calculateSavingsStartOfYear(row: Row): Row {
        row.iraTaxDeferredSavingsStartOfYear = row.iraTaxDeferredSavingsEndOfYear
        row.iraTaxDeferredSavingsStartOfYear = row.iraTaxDeferredSavingsEndOfYear
        return row
    }

    calculateSavingsEndOfYear(row: Row) {
        row.iraTaxDeferredSavingsEndOfYear = row.iraTaxDeferredSavingsStartOfYear + row.iraTaxDeferredContribution + row.iraTaxDeferredGrowthAmount;
        return row
    }

    calculateGrowthAmount(row: Row): Row {
        switch (row.investmentGrowthStrategy) {
            case 'start':
                row.iraTaxDeferredGrowthAmount = row.iraTaxDeferredSavingsStartOfYear * (row.iraGrowthRate / 100)
                return row
            case 'end':
                row.iraTaxDeferredGrowthAmount = (row.iraTaxDeferredSavingsStartOfYear + row.iraTaxDeferredContribution) * (row.iraGrowthRate / 100)
                return row
        }
        return row
    }

    initialize(row: Row) {
        row.iraTaxDeferredSavingsStartOfYear = row.iraTaxDeferredSavingsStartOfYear ? row.iraTaxDeferredSavingsStartOfYear : 0
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row = this.calculateSavingsEndOfYear(row)
        row.iraTaxDeferredContributionLifetime = row.iraTaxDeferredContribution
        return row
    }

    process(row: Row) {
        row = this.calculateSavingsStartOfYear(row)
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row = this.calculateSavingsEndOfYear(row)
        row.iraTaxDeferredContributionLifetime += row.iraTaxDeferredContribution
        return row

    }
}