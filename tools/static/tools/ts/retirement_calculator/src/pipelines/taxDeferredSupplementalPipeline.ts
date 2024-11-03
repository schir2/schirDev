import {Row} from "/interfaces/Row";
import {Pipeline} from "/interfaces/Pipeline";

export default class TaxDeferredSupplementalPipeline implements Pipeline {
    initialize(row: Row): Row {
        // TODO Implement this function
        return row
    }

    process(row: Row) {
        row.taxDeferredGrowthAmount = this.calculateGrowthAmount(row);
        row.taxDeferredContribution = Math.min(
            row.taxDeferredContributionElectiveLimitApplied,
            row.taxDeferredContributionTotal + row.taxDeferredContributionFixedAmount
        );
        row.taxDeferredSavingsEndOfYear = this.getTaxDeferredSavingsEndOfYear(row);
        return row;
    }

    calculateGrowthAmount(row: Row) {
        return row.taxDeferredSavingsStartOfYear * (row.taxDeferredGrowthRate / 100);
    }

    getTaxDeferredSavingsEndOfYear(row: Row) {
        return row.taxDeferredSavingsStartOfYear + row.taxDeferredContributionTotal + row.taxDeferredGrowthAmount;
    }
}