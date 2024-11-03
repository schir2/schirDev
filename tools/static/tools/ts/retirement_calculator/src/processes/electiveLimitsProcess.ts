import {Row} from "../interfaces/Row";
import {Process} from "../interfaces/Process";

export default class ElectiveLimitsProcess implements Process {
    adjustCatchUpLimit(row: Row) {
        row.taxDeferredContributionCatchUpLimit = 7500
        return row;
    }

    adjustElectiveLimit(row: Row) {
        if (row.taxDeferredContributionElectiveLimit === undefined) {
            row.taxDeferredContributionElectiveLimit = 22500
        } else {
            row.taxDeferredContributionElectiveLimit = row.taxDeferredContributionElectiveLimit * (1 + row.taxDeferredContributionElectiveLimitInflationRate / 100);
        }
        return row
    }

    adjustElectiveTotalLimit(row: Row) {
        if (row.taxDeferredContributionTotalElectiveLimit === undefined) {
            row.taxDeferredContributionTotalElectiveLimit = 66000
        } else {

            row.taxDeferredContributionTotalElectiveLimit = row.taxDeferredContributionTotalElectiveLimit * (1 + row.taxDeferredContributionElectiveLimitInflationRate / 100);
        }
        return row
    }

    calculateAgeAdjustedLimit(row: Row) {
        row.taxDeferredContributionElectiveLimitApplied = row.age < 50 ? row.taxDeferredContributionElectiveLimit : row.taxDeferredContributionElectiveLimit + row.taxDeferredContributionCatchUpLimit
        console.log(row.taxDeferredContributionElectiveLimitApplied)
        return row
    }

    calculateAgeAdjustedTotalLimit(row: Row) {
        row.taxDeferredContributionElectiveTotalLimitApplied = row.age < 50 ? row.taxDeferredContributionTotalElectiveLimit : row.taxDeferredContributionTotalElectiveLimit + row.taxDeferredContributionCatchUpLimit
        return row
    }

    initialize(row: Row) {
        row.taxDeferredContributionCatchUpLimit = row.taxDeferredContributionCatchUpLimit ?? 7500;
        row.taxDeferredContributionElectiveLimit = row.taxDeferredContributionElectiveLimit ?? 22500;
        row.taxDeferredContributionTotalElectiveLimit = row.taxDeferredContributionTotalElectiveLimit ?? 66000;
        return row;
    }

    process(row: Row) {
        row = this.adjustCatchUpLimit(row)
        row = this.adjustElectiveLimit(row)
        row = this.adjustElectiveTotalLimit(row)
        row = this.calculateAgeAdjustedLimit(row)
        row = this.calculateAgeAdjustedTotalLimit(row)
        return row
    }
}