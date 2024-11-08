import {Row} from "../interfaces/Row";
import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";

export function getElectiveContribution(row: Row): number {
    let electiveContribution = 0
    switch (row.taxDeferredContributionStrategy) {
        case 'fixed':
            electiveContribution = row.taxDeferredContributionFixedAmount
            break
        case 'percent_of_income':
            electiveContribution = row.incomePreTaxed * (row.taxDeferredContributionPercentage / 100)
            break
        case 'until_company_match':
            electiveContribution = row.employerMatchPercentageLimit * row.incomePreTaxed / 100
            break
        case "max":
            electiveContribution = row.taxDeferredContributionElectiveLimitApplied
            break
    }

    return Math.min(electiveContribution, row.taxDeferredContributionElectiveLimitApplied)

}

export default class TaxDeferredPipeline implements InvestmentPipeline {
    initialize(row: Row): Row {
        row.taxDeferredSavingsStartOfYear = row.taxDeferredSavingsStartOfYear ?? 0
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row.taxDeferredContributionLifetime = row.taxDeferredContribution
        row.taxDeferredSpending += row.taxDeferredContribution
        row = this.calculateSavingsEndOfYear(row);
        return row
    }

    process(row: Row) {
        row = this.calculateSavingsStartOfYear(row)
        row = this.calculateContribution(row)
        row = this.calculateGrowthAmount(row)
        row.taxDeferredContributionLifetime += row.taxDeferredContribution
        row.taxDeferredSpending += row.taxDeferredContribution
        row = this.calculateSavingsEndOfYear(row);
        row.savingsEndOfYear = row.taxDeferredContribution + row.taxDeferredGrowthAmount
        return row;
    }


    calculateGrowthAmount(row: Row): Row {
        switch (row.investmentGrowthStrategy) {
            case 'start':
                row.taxDeferredGrowthAmount = row.taxDeferredSavingsStartOfYear * (row.taxDeferredGrowthRate / 100)
                return row
            case 'end':
                row.taxDeferredGrowthAmount = (row.taxDeferredSavingsStartOfYear + row.taxDeferredContribution) * (row.taxDeferredGrowthRate / 100)
                return row
        }
    }

    calculateContribution(row: Row): Row {
        row.taxDeferredContribution = getElectiveContribution(row)
        return row
    }

    calculateSavingsStartOfYear(row: Row): Row {
        row.taxDeferredSavingsStartOfYear = row.taxDeferredSavingsEndOfYear
        return row
    }

    calculateSavingsEndOfYear(row: Row): Row {
        row.taxDeferredSavingsEndOfYear = row.taxDeferredSavingsStartOfYear + row.taxDeferredContribution + row.taxDeferredGrowthAmount;
        return row
    }
}