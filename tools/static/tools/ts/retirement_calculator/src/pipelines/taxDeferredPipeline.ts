import {Row} from "../interfaces/Row";
import {Pipeline} from "../interfaces/Pipeline";

export function getElectiveContribution(row: Row): number {
    let electiveLimit = 0
    switch (row.taxDeferredContributionStrategy) {
        case 'fixed':
            electiveLimit = row.taxDeferredContributionFixedAmount
            break
        case 'percent_of_income':
            electiveLimit = row.incomePreTaxed * (row.taxDeferredContributionPercentage / 100)
            break
        case 'until_company_match':
            electiveLimit = row.employerMatchPercentageLimit * row.incomePreTaxed / 100
            break
        case "max":
            electiveLimit = row.taxDeferredContributionElectiveLimitApplied
    }
    return Math.min(electiveLimit, row.taxDeferredContributionElectiveLimitApplied)

}

export default class TaxDeferredPipeline implements Pipeline {
    initialize(row: Row): Row {

        row.taxDeferredSavingsStartOfYear = row.taxDeferredSavingsStartOfYear ? row.taxDeferredSavingsStartOfYear : 0
        row = this.calculateContribution(row);
        row = this.calculateGrowth(row);
        row = this.calculateSavingsEndOfYear(row);
        row.taxDeferredContributionLifetime += row.taxDeferredContribution
        return row
    }

    process(row: Row) {

        row = this.calculateContribution(row);
        row = this.calculateGrowth(row);
        row = this.calculateSavingsEndOfYear(row);
        return row;
    }

    calculateContribution(row: Row): Row {
        row.taxDeferredContribution = getElectiveContribution(row)
        return row
    }

    calculateGrowth(row: Row): Row {
        row.taxDeferredSavingsStartOfYear * (row.taxDeferredGrowthRate / 100);
        return row
    }

    calculateSavingsEndOfYear(row: Row): Row {
        // TODO Fix this
        row.taxDeferredSavingsEndOfYear = row.taxDeferredSavingsStartOfYear + row.taxDeferredContribution + row.taxDeferredGrowthAmount;
        return row
    }
}