import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";

export default class IraSavingsPipeline implements InvestmentPipeline {
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

    calculateSavingsStartOfYear(row: Row): Row {
        row.iraSavingsStartOfYear = row.iraSavingsEndOfYear
        return row
    }

    calculateSavingsEndOfYear(row: Row) {
        row.iraSavingsEndOfYear = row.iraSavingsStartOfYear + row.iraContribution + row.iraGrowthAmount;
        return row
    }

    calculateGrowthAmount(row: Row): Row {
        switch (row.investmentGrowthStrategy) {
            case 'start':
                row.iraGrowthAmount = row.iraSavingsStartOfYear * (row.iraGrowthRate / 100)
                return row
            case 'end':
                row.iraGrowthAmount = (row.iraSavingsStartOfYear + row.iraContribution) * (row.iraGrowthRate / 100)
                return row
        }
        return row
    }

    initialize(row: Row) {
        row.iraSavingsStartOfYear = row.iraSavingsStartOfYear ? row.iraSavingsStartOfYear : 0
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row = this.calculateSavingsEndOfYear(row)
        row.iraContributionLifetime = row.iraContribution
        return row
    }

    process(row: Row) {
        row = this.calculateSavingsStartOfYear(row)
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row = this.calculateSavingsEndOfYear(row)
        row.iraContributionLifetime += row.iraContribution
        return row

    }
}