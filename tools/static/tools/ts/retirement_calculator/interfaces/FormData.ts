import {
  ContributionStrategy, EmployerContributionStrategy,
  ExpensesGrowthStrategy,
  GrowthStrategy,
  IncomeTaxStrategy, InflationGrowthStrategy, IraContributionStrategy, IraGrowthStrategy,
  RetirementStrategy, TaxableContributionStrategy, TaxableGrowthStrategy,
  TaxDeferredGrowthStrategy
} from "types";

export default interface FormData {
  /* Profile */
  age: number;
  year: number;
  lifeExpectancy: number;

  /* Retirement Strategies */
  retirementStrategy: RetirementStrategy;
  retirementWithdrawalRate: number;
  retirementIncomeGoal: number;
  retirementAge: number;
  retirementSavingsAmount: number;
  retirementIncomeProjected: number;

  /* Initial Values */
  cash: number;

  /* Income */
  incomePreTaxed: number;
  incomeTaxable: number;
  incomeTaxed: number;
  incomeDisposable: number;
  incomeGrowthStrategy: GrowthStrategy;
  incomeGrowthRate: number;
  incomeGrowthAmount: number;

  /* Income Tax */
  incomeTaxAmount: number;
  incomeTaxRate: number;
  incomeTaxStrategy: IncomeTaxStrategy;
  incomeTaxFilingStatus: string;
  incomeTaxNumberOfDependents: string;

  /* Expenses */
  expenses: number;
  expenseRate: number;
  expensesGrowthStrategy: ExpensesGrowthStrategy;

  /* Debt & Mortgage */
  debt: number;
  debtInterestRate: number;
  debtPayment: number;
  debtPaymentTotal: number;

  /* Goals */
  targetAnnualRetirementSpendingPreTaxed: number;
  targetEndOfLifeSavingsPreTaxed: number;

  /* Tax Deferred Savings */
  taxDeferredSavingsStartOfYear: number;
  taxDeferredContributionFixedAmount: number;
  taxDeferredContributionStrategy: ContributionStrategy;
  taxDeferredSavingsEndOfYear: number;
  taxDeferredContribution: number;
  taxDeferredContributionTotal: number;
  taxDeferredGrowthStrategy: TaxDeferredGrowthStrategy;
  taxDeferredContributionPercentage: number;
  taxDeferredGrowthRate: number;

  taxDeferredContributionElectiveLimit?: number;
  taxDeferredContributionElectiveLimitApplied?: number;
  taxDeferredContributionCatchUpLimit?: number;
  taxDeferredContributionTotalElectiveLimit?: number;
  taxDeferredContributionTotalElectiveLimitApplied?: number;
  taxDeferredContributionElectiveLimitInflationRate: number;

  /* Employer Contributions */
  employerContributionStrategy: EmployerContributionStrategy;
  employerContribution: number;
  employerMatchPercentage: number;
  employerMatchPercentageLimit: number;
  employerContributionPercentage: number;
  employerContributionFixedAmount: number;

  /* IRA Savings */
  iraSavingsInitial: number;
  iraContributionFixedAmount: number;
  iraContribution: number;
  iraContributionStrategy: IraContributionStrategy;
  iraSavingsStartOfYear: number;
  iraSavingsEndOfYear: number;
  iraContributionTotal: number;
  iraGrowthStrategy: IraGrowthStrategy;
  iraContributionPercentage: number;
  iraGrowthRate: number;
  iraContributionLimit: number;
  iraContributionCatchUpLimit: number;

  /* Taxable Savings */
  taxableContributionFixedAmount: number;
  taxableContribution: number;
  taxableContributionStrategy: TaxableContributionStrategy;
  taxableSavingsStartOfYear: number;
  taxableSavingsEndOfYear: number;
  taxableContributionLifetime: number;
  taxableGrowthStrategy: TaxableGrowthStrategy;
  taxableContributionPercentage: number;
  taxableGrowthRate: number;

  /* Inflation */
  inflationRate: number;
  inflationGrowthStrategy: InflationGrowthStrategy;
}
