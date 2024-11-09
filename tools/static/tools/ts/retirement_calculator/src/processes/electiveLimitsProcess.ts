import {Row} from "../interfaces/Row";
import {Process} from "../interfaces/Process";

export default class ElectiveLimitsProcess implements Process {
    adjustCatchUpLimit(row: Row) {
        row.taxDeferredContributionElectiveCatchUpLimit = 7500
        return row;
    }

    process(row: Row) {
        row.taxDeferredContributionLimit = row.calculateAdjustedTaxDeferredContributionLimit()
        row.taxDeferredContributionElectiveLimit = row.calculateAdjustedTaxDeferredContributionElectiveLimit()
        row.taxDeferredContributionElectiveCatchUpLimit = row.calculateAdjustedTaxDeferredContributionElectiveCatchUpLimit()
        row.taxDeferredContributionElectiveLimitApplied = row.calculateTaxDeferredContributionElectiveLimitApplied() ;
        row.taxDeferredContributionLimitApplied = row.calculateTaxDeferredContributionLimitApplied();
        return row
    }
}