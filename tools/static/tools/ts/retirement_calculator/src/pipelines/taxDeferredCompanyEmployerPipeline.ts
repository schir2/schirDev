import {Pipeline} from "../interfaces/Pipeline";
import {Row} from "../interfaces/Row";
import {getElectiveContribution} from "./taxDeferredPipeline"

export default class TaxDeferredCompanyEmployerPipeline implements Pipeline {
    process(row: Row) {
        row = this.calculateContribution(row);
        row.employerContributionLifetime += row.employerContribution
        return row;
    }

    initialize(row: Row): Row {
        row = this.calculateContribution(row);
        row.employerContributionLifetime += row.employerContribution
        return row
    }

    calculateContribution(row: Row): Row {
        let employerContribution = 0
        const electiveContribution = getElectiveContribution(row)
        switch (row.employerContributionStrategy) {
            case 'none':
                break
            case "percentage_of_contribution":
                employerContribution = row.employerContribution * (row.employerMatchPercentage / 100)
                break
            case "fixed":
                employerContribution = row.employerContributionFixedAmount
                break
            case "percentage_of_compensation":
                const employerMatch = electiveContribution * (row.employerMatchPercentage / 100);
                const maxEmployerMatch = row.incomePreTaxed * row.employerMatchPercentageLimit / 100;
                employerContribution = Math.min(employerMatch, maxEmployerMatch)
                break
        }
        row.employerContribution = Math.min(employerContribution, row.taxDeferredContributionElectiveTotalLimitApplied)
        return row

    }
}