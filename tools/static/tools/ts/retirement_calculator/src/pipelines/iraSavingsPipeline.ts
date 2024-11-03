import {Row} from "../interfaces/Row";
import {Pipeline} from "../interfaces/Pipeline";

export default class IraSavingsPipeline implements Pipeline {
    calculateContribution(row: Row): Row {
        switch (row.iraContributionStrategy) {
            case 'fixed':
                row.iraContribution = row.iraContributionFixedAmount
                return row
            case 'percent_of_income':
                row.iraContribution = row.incomePreTaxed * (row.iraContributionPercentage / 100)
                return row
            case 'max':
                row.iraContribution = Number(row.age) >= 50 ? row.iraContributionCatchUpLimit : row.iraContributionLimit
                return row
        }
    }

    calculateGrowth(row: Row): Row {
        switch (row.iraGrowthStrategy) {
            case 'start':
                row.iraGrowthAmount = row.iraSavingsStartOfYear * (row.iraGrowthRate / 100)
                return row
            case 'end':
                row.iraGrowthAmount = (row.iraSavingsStartOfYear + row.iraContribution) * (row.iraGrowthRate / 100)
                return row
        }
    }

    calculateSavingsEndOfYear(row: Row) {
        row.iraSavingsEndOfYear = row.iraSavingsStartOfYear + row.iraContribution + row.iraGrowthAmount;
        return row
    }

    initialize(row: Row) {
        row.iraSavingsStartOfYear = row.iraSavingsStartOfYear ? row.iraSavingsStartOfYear : 0
        row = this.calculateContribution(row)
        row = this.calculateGrowth(row)
        row = this.calculateSavingsEndOfYear(row)
        row.iraContributionLifetime = row.iraContribution
        return row
    }

    process(row: Row) {
        row.iraSavingsStartOfYear = row.iraSavingsEndOfYear
        row = this.calculateContribution(row)
        row = this.calculateGrowth(row)
        row = this.calculateSavingsEndOfYear(row)
        row.iraContributionLifetime += row.iraContribution
        return row

    }
}