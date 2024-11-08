import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";

export default class TaxableSavingsPipeline implements InvestmentPipeline {
    calculateContribution(row: Row): Row {
        switch (row.taxableContributionStrategy) {
            case 'fixed':
                row.taxableContribution = row.taxableContributionFixedAmount
                return row
            case 'percent_of_income':
                row.taxableContribution = row.incomePreTaxed * (row.taxableContributionPercentage / 100)
                return row
        }
    }

    calculateGrowthAmount(row: Row): Row {
        switch (row.investmentGrowthStrategy) {
            case 'start':
                row.taxableGrowthAmount = row.taxableSavingsStartOfYear * (row.taxableGrowthRate / 100)
                return row
            case 'end':
                row.taxableGrowthAmount = (row.taxableSavingsStartOfYear + row.taxableContribution) * (row.taxableGrowthRate / 100)
                return row
        }
    }

    calculateSavingsStartOfYear(row: Row): Row {
        row.taxableSavingsStartOfYear= row.taxableSavingsEndOfYear
        return row
    }

    calculateSavingsEndOfYear(row: Row): Row {
        row.taxableSavingsEndOfYear = row.taxableSavingsStartOfYear + row.taxableContribution + row.taxableGrowthAmount;
        return row
    }

    initialize(row: Row) {
        row.taxableSavingsStartOfYear = row.taxableSavingsStartOfYear ?? 0
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row.taxableContributionLifetime += row.taxableContribution
        row.taxableSpending += row.taxableContribution
        row = this.calculateSavingsEndOfYear(row)
        return row
    }

    process(row: Row) {
        row = this.calculateSavingsStartOfYear(row)
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row.taxableContributionLifetime += row.taxableContribution
        row.taxableSpending += row.taxableContribution
        row = this.calculateSavingsEndOfYear(row)
        return row

    }
}