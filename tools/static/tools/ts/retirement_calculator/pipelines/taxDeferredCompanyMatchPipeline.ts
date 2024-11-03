import {Pipeline} from "interfaces/Pipeline";
import {Row} from "interfaces/Row";

export default class TaxDeferredCompanyMatchPipeline implements Pipeline {
    process(row: Row) {
        row.employerContribution = this.getEmployerContribution(row);
        row.taxDeferredContribution = Math.min(row.taxDeferredContributionElectiveLimitApplied, row.employerContribution);
        row.taxDeferredContributionTotal = this.getTaxDeferredContributionTotal(row);
        return row;
    }

    initialize(row: Row): Row {
        // TODO Implement this
        return row
    }

    getEmployerContribution(row: Row) {
        const employerMatch = row.taxDeferredContribution * (row.employerMatchPercentage / 100);
        const maxEmployerMatch = row.incomePreTaxed * row.employerMatchPercentageLimit / 100;
        return Math.min(employerMatch, maxEmployerMatch);
    }

    getTaxDeferredContributionTotal(row: Row) {
        return row.taxDeferredContribution + row.employerContribution;
    }
}