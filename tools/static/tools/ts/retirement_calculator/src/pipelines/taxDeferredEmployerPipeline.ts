import {InvestmentPipeline} from "../interfaces/InvestmentPipeline";
import {Row} from "../interfaces/Row";
import {getElectiveContribution} from "./taxDeferredPipeline"

export default class TaxDeferredEmployerPipeline implements InvestmentPipeline {
    initialize(row: Row): Row {
        row.employerSavingsStartOfYear = row.employerSavingsStartOfYear ?? 0
        row = this.calculateContribution(row);
        row.employerContributionLifetime += row.employerContribution
        row = this.calculateGrowthAmount(row)
        row = this.calculateSavingsEndOfYear(row)
        return row
    }

    process(row: Row) {
        row = this.calculateSavingsStartOfYear(row)
        row = this.calculateContribution(row);
        row.employerContributionLifetime += row.employerContribution
        row = this.calculateGrowthAmount(row)
        row = this.calculateSavingsEndOfYear(row);
        return row;
    }

    calculateSavingsEndOfYear(row: Row): Row {
        row.employerSavingsEndOfYear = row.employerSavingsStartOfYear + row.employerContribution + row.employerGrowthAmount
        return row
    }

    calculateSavingsStartOfYear(row: Row): Row {
        row.employerSavingsStartOfYear = row.employerSavingsEndOfYear
        return row
    }


    calculateGrowthAmount(row: Row): Row {
        switch (row.investmentGrowthStrategy) {
            case 'start':
                row.employerGrowthAmount = row.employerSavingsStartOfYear * (row.taxDeferredGrowthRate / 100)
                return row
            case 'end':
                row.employerGrowthAmount = (row.employerSavingsStartOfYear + row.employerContribution) * (row.taxDeferredGrowthRate / 100)
                return row
        }
    }

    calculateContribution(row: Row): Row {
        let employerContribution = 0
        const electiveContribution = getElectiveContribution(row)

        switch (row.employerContributionStrategy) {
            case 'none':
                break
            case "percentage_of_contribution":
                const employerMatch = electiveContribution * (row.employerMatchPercentage / 100);
                const maxEmployerMatch = row.incomePreTaxed * row.employerMatchPercentageLimit / 100;
                employerContribution = Math.min(employerMatch, maxEmployerMatch)
                break
            case "fixed":
                employerContribution = row.employerContributionFixedAmount
                break
            case "percentage_of_compensation":
                employerContribution = row.incomePreTaxed * (row.employerContributionPercentage / 100)
                break
        }
        row.employerContribution = Math.min(employerContribution, row.taxDeferredContributionElectiveTotalLimitApplied - electiveContribution)
        return row

    }
}