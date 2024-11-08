import {
    ContributionStrategy,
    EmployerContributionStrategy,
    ExpensesGrowthStrategy,
    GrowthStrategy,
    IncomeTaxStrategy,
    InflationGrowthStrategy,
    InvestmentGrowthStrategy,
    IraContributionStrategy,
    IraType,
    RetirementStrategy,
    TaxableContributionStrategy,
} from '../types'

export interface Row {
    /* Profile */
    investmentGrowthStrategy: InvestmentGrowthStrategy;
    employerGrowthAmount: number;
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
    cashStartOfYear: number;
    cashEndOfYear: number;
    incomeDisposable: number;

    /* Income */
    incomePreTaxed: number;
    incomeTaxable: number;
    incomeTaxed: number;
    incomeGrowthStrategy: GrowthStrategy;
    incomeGrowthRate: number;
    incomeGrowthAmount: number;
    agi: number;

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
    employerSavingsStartOfYear: number;
    employerSavingsEndOfYear: number;

  /* IRA Savings */
  iraTaxableSavingsStartOfYear: number;
  iraTaxableSavingsEndOfYear: number;
  iraTaxableContribution: number;
  iraTaxableContributionFixedAmount: number;
  iraTaxableContributionStrategy: IraContributionStrategy;
  iraTaxableContributionPercentage: number;
  iraTaxableContributionLifetime: number;
  iraTaxableGrowthAmount: number;

  iraTaxDeferredSavingsStartOfYear: number;
  iraTaxDeferredSavingsEndOfYear: number;
  iraTaxDeferredContribution: number;
  iraTaxDeferredContributionFixedAmount: number;
  iraTaxDeferredContributionStrategy: IraContributionStrategy;
  iraTaxDeferredContributionPercentage: number;
  iraTaxDeferredContributionLifetime: number;
  iraTaxDeferredGrowthAmount: number;

  iraGrowthRate: number;
  iraContributionLimit: number;
  iraContributionCatchUpLimit: number;


    /* Taxable Savings */
    taxableSavingsStartOfYear: number;
    taxableSavingsEndOfYear: number;
    taxableContributionFixedAmount: number;
    taxableContribution: number;
    taxableContributionStrategy: TaxableContributionStrategy;
    taxableContributionLifetime: number;
    taxableContributionPercentage: number;
    taxableGrowthRate: number;
    taxableGrowthAmount: number;

    /* Inflation */
    inflationRate: number;
    inflationGrowthStrategy: InflationGrowthStrategy;

    /* Calculated Fields */
    savingsStartOfYear: number;
    savingsEndOfYear: number;
    taxableSpending: number;
    taxDeferredSpending: number;
}
