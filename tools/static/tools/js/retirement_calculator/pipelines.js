const pipelines = {
    CompanyMatchPipeline: {
        process(row) {
            row.taxDeferredContributionElectiveLimitApplied = this.getTaxDeferredContributionElectiveLimitApplied(row);
            row.employerContribution = this.getEmployerContribution(row);
            row.taxDeferredContribution = Math.min(row.taxDeferredContributionElectiveLimitApplied, row.employerContribution);
            row.taxDeferredContributionTotal = this.getTaxDeferredContributionTotal(row);
            return row;
        },
        getTaxDeferredContributionElectiveLimitApplied(row) {
            return row.age < 50
                ? row.taxDeferredContributionElectiveLimit
                : row.taxDeferredContributionElectiveLimit + row.taxDeferredContributionCatchUpLimit;
        },
        getEmployerContribution(row) {
            const employerMatch = row.taxDeferredContribution * (row.employerMatchPercentage / 100);
            const maxEmployerMatch = row.incomePreTaxed * row.employerMatchPercentageLimit / 100;
            return Math.min(employerMatch, maxEmployerMatch);
        },
        getTaxDeferredContributionTotal(row) {
            return row.taxDeferredContribution + row.employerContribution;
        }
    },

    AdditionalDeferredPipeline: {
        process(row) {
            row.taxDeferredGrowthAmount = this.calculateGrowthAmount(row);
            row.taxDeferredContribution = Math.min(
                row.taxDeferredContributionElectiveLimitApplied,
                row.taxDeferredContributionTotal + row.taxDeferredContributionFixedAmount
            );
            row.taxDeferredSavingsEndOfYear = this.getTaxDeferredSavingsEndOfYear(row);
            return row;
        },
        calculateGrowthAmount(row) {
            return row.taxDeferredSavingsStartOfYear * (row.taxDeferredGrowthRate / 100);
        },
        getTaxDeferredSavingsEndOfYear(row) {
            return row.taxDeferredSavingsStartOfYear + row.taxDeferredContributionTotal + row.taxDeferredGrowthAmount;
        }
    }
}