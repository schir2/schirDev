const process = {

    ElectiveLimitsProcess: {
        adjustCatchUpLimit(row) {
            row.taxDeferredContributionCatchUpLimit = 7500
            return row;
        },
        adjustElectiveLimit(row) {
            if (row.taxDeferredContributionElectiveLimit === undefined) {
                row.taxDeferredContributionElectiveLimit = 22500
            } else {
                row.taxDeferredContributionElectiveLimit = row.taxDeferredContributionElectiveLimit * (1 + row.taxDeferredContributionElectiveLimitInflationRate / 100);
            }
            return row
        },
        adjustElectiveTotalLimit(row) {
            if (row.taxDeferredContributionTotalElectiveLimit === undefined) {
                row.taxDeferredContributionTotalElectiveLimit = 66000
            } else {

                row.taxDeferredContributionTotalElectiveLimit = row.taxDeferredContributionTotalElectiveLimit * (1 + row.taxDeferredContributionElectiveLimitInflationRate / 100);
            }
            return row
        },
        calculateAgeAdjustedLimit(row) {
            row.taxDeferredContributionElectiveLimitApplied = row.age < 50 ? row.taxDeferredContributionElectiveLimit : row.taxDeferredContributionElectiveLimit + row.taxDeferredContributionCatchUpLimit
            console.log(row.taxDeferredContributionElectiveLimitApplied)
            return row
        },
        calculateAgeAdjustedTotalLimit(row) {
            row.taxDeferredContributionElectiveTotalLimitApplied = row.age < 50 ? row.taxDeferredContributionTotalElectiveLimit : row.taxDeferredContributionTotalElectiveLimit + row.taxDeferredContributionCatchUpLimit
            return row
        },
        process(row) {
            row = this.adjustCatchUpLimit(row)
            row = this.adjustElectiveLimit(row)
            row = this.adjustElectiveTotalLimit(row)
            row = this.calculateAgeAdjustedLimit(row)
            row = this.calculateAgeAdjustedTotalLimit(row)
            return row
        },
    }

}

const pipeline = {
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