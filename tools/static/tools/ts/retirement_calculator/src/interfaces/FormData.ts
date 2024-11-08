import {
  ContributionStrategy, EmployerContributionStrategy,
  ExpensesGrowthStrategy,
  GrowthStrategy,
  IncomeTaxStrategy, InflationGrowthStrategy, IraContributionStrategy,
  RetirementStrategy, TaxableContributionStrategy, InvestmentGrowthStrategy, IraType,
} from "../types";

export default interface FormData {
  /* Profile */
  age: number;
  year: number;
  lifeExpectancy: number;

  /* Extra Settings */
  allowNegativeBalance: boolean;
  investmentGrowthStrategy: InvestmentGrowthStrategy

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
  taxDeferredContributionPercentage: number;
  taxDeferredGrowthRate: number;

  taxDeferredContributionElectiveLimit?: number;
  taxDeferredContributionElectiveLimitApplied?: number;
  taxDeferredContributionCatchUpLimit?: number;
  taxDeferredContributionTotalElectiveLimit?: number;
  taxDeferredContributionElectiveTotalLimitApplied?: number;
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

  iraTaxDeferredSavingsStartOfYear: number;
  iraTaxDeferredSavingsEndOfYear: number;
  iraTaxDeferredContribution: number;
  iraTaxDeferredContributionFixedAmount: number;
  iraTaxDeferredContributionStrategy: IraContributionStrategy;
  iraTaxDeferredContributionPercentage: number;

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
  taxableContributionPercentage: number;
  taxableGrowthRate: number;

  /* Inflation */
  inflationRate: number;
  inflationGrowthStrategy: InflationGrowthStrategy;
}
