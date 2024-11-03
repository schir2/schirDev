import {Row} from "../interfaces/Row";
import {Pipeline} from "../interfaces/Pipeline";

export default class TaxableSavingsPipeline implements Pipeline {
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

    calculateGrowth(row: Row): Row {
        switch (row.taxableGrowthStrategy) {
            case 'start':
                row.taxableGrowthAmount = row.taxableSavingsStartOfYear * (row.taxableGrowthRate / 100)
                return row
            case 'end':
                row.taxableGrowthAmount = (row.taxableSavingsStartOfYear + row.taxableContribution) * (row.taxableGrowthRate / 100)
                return row
        }
    }

    calculateSavingsEndOfYear(row: Row): Row {
        row.taxableSavingsEndOfYear = row.taxableSavingsStartOfYear + row.taxableContribution + row.taxableGrowthAmount;
        return row
    }

    initialize(row: Row) {
        row.taxableSavingsStartOfYear = row.taxableSavingsStartOfYear ? row.taxableSavingsStartOfYear : 0
        row = this.calculateContribution(row)
        row = this.calculateGrowth(row)
        row = this.calculateSavingsEndOfYear(row)
        row.taxableContributionLifetime += row.taxableContribution
        return row
    }

    process(row: Row) {
        row.taxableSavingsStartOfYear = row.taxableSavingsEndOfYear
        row = this.calculateContribution(row)
        row = this.calculateGrowth(row)
        row = this.calculateSavingsEndOfYear(row)
        row.taxableContributionLifetime += row.taxableContribution
        return row

    }
}