import {
    ContributionStrategy,
    EmployerContributionStrategy,
    ExpensesGrowthStrategy,
    GrowthStrategy,
    IncomeTaxStrategy,
    InflationGrowthStrategy,
    IraContributionStrategy,
    IraGrowthStrategy,
    RetirementStrategy,
    TaxableContributionStrategy,
    TaxableGrowthStrategy,
    TaxDeferredGrowthStrategy
} from '../types'

export interface Row {
    /* Profile */
    employerContributionLifetime: number;
    age: number;
    year: number;
    lifeExpectancy: number;

    /* Retirement */
    retirementStrategy: RetirementStrategy;
    retirementWithdrawalRate: number;
    retirementIncomeGoal: number;
    retirementAge: number;
    retirementSavingsAmount: number;
    retirementIncomeProjected: number;

    /* Cash and Disposable Income */
    cash: number;
    incomeDisposable: number;

    /* Income */
    incomePreTaxed: number;
    incomeTaxable: number;
    incomeTaxed: number;
    incomeGrowthStrategy: GrowthStrategy;
    incomeGrowthRate: number;
    incomeGrowthAmount: number;

    /* Tax */
    incomeTaxAmount: number;
    incomeTaxRate: number;
    incomeTaxStrategy: IncomeTaxStrategy;
    incomeTaxFilingStatus: string;
    incomeTaxNumberOfDependents: string;

    /* Expenses */
    expenses: number;
    expenseRate: number;
    expensesGrowthStrategy: ExpensesGrowthStrategy;

    /* Debt */
    debt: number;
    debtInterestRate: number;
    debtPayment: number;
    debtPaymentTotal: number;

    /* Retirement Goals */
    targetAnnualRetirementSpendingPreTaxed: number;
    targetEndOfLifeSavingsPreTaxed: number;

    /* Tax-Deferred Savings */
    taxDeferredSavingsStartOfYear: number;
    taxDeferredContributionFixedAmount: number;
    taxDeferredContributionStrategy: ContributionStrategy;
    taxDeferredContribution: number;
    taxDeferredContributionTotal: number;
    taxDeferredGrowthStrategy: TaxDeferredGrowthStrategy;
    taxDeferredGrowthAmount: number;
    taxDeferredContributionPercentage: number;
    taxDeferredSavingsEndOfYear: number;
    taxDeferredGrowthRate: number;
    taxDeferredContributionLifetime: number;

    taxDeferredContributionCatchUpLimit: number;
    taxDeferredContributionElectiveLimit: number;
    taxDeferredContributionElectiveLimitApplied: number;
    taxDeferredContributionTotalElectiveLimit: number;
    taxDeferredContributionElectiveTotalLimitApplied: number;
    taxDeferredContributionElectiveLimitInflationRate: number;

    /* Employer Contributions */
    employerContributionStrategy: EmployerContributionStrategy;
    employerContribution: number;
    employerMatchPercentage: number;
    employerMatchPercentageLimit: number;
    employerContributionPercentage: number;
    employerContributionFixedAmount: number;

    /* IRA */
    iraSavingsStartOfYear: number;
    iraSavingsEndOfYear: number;
    iraContribution: number;
    iraContributionFixedAmount: number;
    iraContributionStrategy: IraContributionStrategy;
    iraContributionLifetime: number;
    iraGrowthStrategy: IraGrowthStrategy;
    iraContributionPercentage: number;
    iraGrowthRate: number;
    iraGrowthAmount: number;
    iraContributionLimit: number;
    iraContributionCatchUpLimit: number;

    /* Taxable Savings */
    taxableSavingsStartOfYear: number;
    taxableSavingsEndOfYear: number;
    taxableContributionFixedAmount: number;
    taxableContribution: number;
    taxableContributionStrategy: TaxableContributionStrategy;
    taxableContributionLifetime: number;
    taxableGrowthStrategy: TaxableGrowthStrategy;
    taxableContributionPercentage: number;
    taxableGrowthRate: number;
    taxableGrowthAmount: number;

    /* Inflation */
    inflationRate: number;
    inflationGrowthStrategy: InflationGrowthStrategy;

    /* Calculated Fields */
    savingsStartOfYear: number;
    savingsEndOfYear: number;
}
