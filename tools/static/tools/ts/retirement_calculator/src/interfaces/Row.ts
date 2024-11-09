// this.ts
import FormData from '../interfaces/FormData';
import {
    ContributionStrategy,
    EmployerContributionStrategy,
    ExpensesGrowthStrategy,
    GrowthStrategy,
    IncomeTaxStrategy,
    InflationGrowthStrategy,
    InvestmentGrowthStrategy,
    IraContributionStrategy,
    RetirementStrategy,
    TaxableContributionStrategy
} from "../types";
import {
    assertDefined,
    calculateTaxDeferredContributionLimit,
    calculateTaxDeferredElectiveContributionCatchUpLimit,
    calculateTaxDeferredElectiveContributionLimit
} from "../utils";
import {TAX_DEFERRED_CATCH_UP_AGE, TAX_DEFERRED_LIMIT_INFLATION_RATE} from "../constants";

export class Row {
    age: number;
    year: number;
    lifeExpectancy: number;

    /* Retirement */
    retirementStrategy: RetirementStrategy;
    retirementWithdrawalRate: number;
    retirementIncomeGoal: number;
    retirementAge: number;
    retirementSavingsAmount: number;
    retirementIncomeProjected?: number;

    /* Cash and Disposable Income */
    cashStartOfYear: number;
    cashEndOfYear: number;
    incomeDisposable?: number;

    /* Income */
    incomePreTaxed: number;
    incomeTaxable?: number;
    incomeTaxed?: number;
    incomeGrowthStrategy: GrowthStrategy;
    incomeGrowthRate: number;
    incomeGrowthAmount?: number;

    /* Tax */
    incomeTaxAmount?: number;
    incomeTaxRate: number;
    incomeTaxStrategy: IncomeTaxStrategy;
    incomeTaxFilingStatus: string;
    incomeTaxNumberOfDependents: string;

    /* Expenses */
    expenses: number;
    expenseRate: number;
    expensesGrowthStrategy: ExpensesGrowthStrategy;

    /* Debt */
    debtStartOfYear: number;
    debtEndOfYear: number;
    debtInterestRate: number;
    debtPayment: number;
    debtPaymentTotal: number;

    /* Tax-Deferred Savings */
    taxDeferredSavingsStartOfYear: number;
    taxDeferredContributionFixedAmount: number;
    taxDeferredContributionStrategy: ContributionStrategy;
    taxDeferredContribution: number;
    taxDeferredContributionTotal?: number;
    taxDeferredGrowthAmount?: number;
    taxDeferredContributionPercentage: number;
    taxDeferredSavingsEndOfYear: number;
    taxDeferredGrowthRate: number;
    taxDeferredContributionLifetime: number;

    taxDeferredContributionLimitInflationRate: number;
    taxDeferredContributionElectiveCatchUpLimit: number;
    taxDeferredContributionElectiveLimit: number;
    taxDeferredContributionLimit: number;
    taxDeferredContributionElectiveLimitApplied: number;
    taxDeferredContributionLimitApplied: number;

    /* Employer Contributions */
    employerContributionStrategy: EmployerContributionStrategy;
    employerContribution: number;
    employerMatchPercentage: number;
    employerMatchPercentageLimit: number;
    employerContributionPercentage: number;
    employerContributionFixedAmount: number;
    employerSavingsStartOfYear: number;
    employerSavingsEndOfYear: number;
    employerGrowthAmount?: number;
    employerContributionLifetime: number;

    /* IRA Savings */
    iraTaxableSavingsStartOfYear: number;
    iraTaxableSavingsEndOfYear: number;
    iraTaxableContribution: number;
    iraTaxableContributionFixedAmount: number;
    iraTaxableContributionStrategy: IraContributionStrategy;
    iraTaxableContributionPercentage: number;
    iraTaxableContributionLifetime: number;
    iraTaxableGrowthAmount?: number;

    iraTaxDeferredSavingsStartOfYear: number;
    iraTaxDeferredSavingsEndOfYear: number;
    iraTaxDeferredContribution: number;
    iraTaxDeferredContributionFixedAmount: number;
    iraTaxDeferredContributionStrategy: IraContributionStrategy;
    iraTaxDeferredContributionPercentage: number;
    iraTaxDeferredContributionLifetime: number;
    iraTaxDeferredGrowthAmount?: number;

    iraGrowthRate: number;
    iraContributionLimit?: number;
    iraContributionCatchUpLimit?: number;


    /* Taxable Savings */
    taxableSavingsStartOfYear: number;
    taxableSavingsEndOfYear: number;
    taxableContributionFixedAmount: number;
    taxableContribution: number;
    taxableContributionStrategy: TaxableContributionStrategy;
    taxableContributionLifetime: number;
    taxableContributionPercentage: number;
    taxableGrowthRate: number;
    taxableGrowthAmount?: number;

    /* Inflation */
    inflationRate: number;
    inflationGrowthStrategy: InflationGrowthStrategy;
    investmentGrowthStrategy: InvestmentGrowthStrategy;

    /* Calculated Fields */
    savingsStartOfYear: number;
    savingsEndOfYear: number;
    taxableSpending: number;
    taxDeferredSpending: number;

    constructor(formData: FormData) {
        // Initialize properties using form data
        this.age = formData.age;
        this.year = formData.year;
        this.lifeExpectancy = formData.lifeExpectancy;
        this.retirementStrategy = formData.retirementStrategy;
        this.retirementWithdrawalRate = formData.retirementWithdrawalRate;
        this.retirementIncomeGoal = formData.retirementIncomeGoal;
        this.retirementAge = formData.retirementAge;
        this.retirementSavingsAmount = formData.retirementSavingsAmount;

        this.cashStartOfYear = 0;
        this.cashEndOfYear = formData.cash;

        this.incomePreTaxed = formData.incomePreTaxed;
        this.incomeGrowthStrategy = formData.incomeGrowthStrategy;
        this.incomeGrowthRate = formData.incomeGrowthRate;
        this.incomeTaxRate = formData.incomeTaxRate;
        this.incomeTaxStrategy = formData.incomeTaxStrategy;
        this.incomeTaxFilingStatus = formData.incomeTaxFilingStatus;
        this.incomeTaxNumberOfDependents = formData.incomeTaxNumberOfDependents;

        this.expenses = formData.expenses;
        this.expenseRate = formData.expenseRate;
        this.expensesGrowthStrategy = formData.expensesGrowthStrategy;

        this.debtStartOfYear = 0;
        this.debtEndOfYear = formData.debt;
        this.debtInterestRate = formData.debtInterestRate;
        this.debtPayment = formData.debtPayment;
        this.debtPaymentTotal = 0;

        this.taxDeferredSavingsStartOfYear = 0;
        this.taxDeferredSavingsEndOfYear = formData.taxDeferredSavings;
        this.taxDeferredContributionFixedAmount = formData.taxDeferredContributionFixedAmount;
        this.taxDeferredContributionStrategy = formData.taxDeferredContributionStrategy;
        this.taxDeferredContributionPercentage = formData.taxDeferredContributionPercentage;
        this.taxDeferredGrowthRate = formData.taxDeferredGrowthRate;
        this.taxDeferredContribution = 0
        this.taxDeferredContributionLifetime = 0;

        this.taxDeferredContributionLimitInflationRate = TAX_DEFERRED_LIMIT_INFLATION_RATE;
        this.taxDeferredContributionElectiveCatchUpLimit = calculateTaxDeferredElectiveContributionCatchUpLimit(this.year);
        this.taxDeferredContributionElectiveLimit = calculateTaxDeferredElectiveContributionLimit(this.year)
        this.taxDeferredContributionLimit = calculateTaxDeferredContributionLimit(this.year);
        this.taxDeferredContributionElectiveLimitApplied = this.calculateTaxDeferredContributionElectiveLimitApplied();
        this.taxDeferredContributionLimitApplied = this.calculateTaxDeferredContributionLimitApplied();

        this.employerContributionStrategy = formData.employerContributionStrategy;
        this.employerMatchPercentage = formData.employerMatchPercentage;
        this.employerMatchPercentageLimit = formData.employerMatchPercentageLimit;
        this.employerContributionPercentage = formData.employerContributionPercentage;
        this.employerContributionFixedAmount = formData.employerContributionFixedAmount;
        this.employerSavingsStartOfYear = 0;
        this.employerSavingsEndOfYear = 0;
        this.employerContribution = 0;
        this.employerContributionLifetime = 0;

        this.iraTaxableSavingsStartOfYear = 0;
        this.iraTaxableSavingsEndOfYear = formData.iraTaxableSavings;
        this.iraTaxableContributionFixedAmount = formData.iraTaxableContributionFixedAmount;
        this.iraTaxableContributionStrategy = formData.iraTaxableContributionStrategy;
        this.iraTaxableContribution = 0
        this.iraTaxableContributionPercentage = formData.iraTaxableContributionPercentage;
        this.iraTaxableContributionLifetime = 0;

        this.iraTaxDeferredSavingsStartOfYear = 0;
        this.iraTaxDeferredSavingsEndOfYear = formData.iraTaxDeferredSavings;
        this.iraTaxDeferredContributionFixedAmount = formData.iraTaxDeferredContributionFixedAmount;
        this.iraTaxDeferredContributionStrategy = formData.iraTaxDeferredContributionStrategy;
        this.iraTaxDeferredContribution = 0;
        this.iraTaxDeferredContributionPercentage = formData.iraTaxDeferredContributionPercentage;
        this.iraTaxDeferredContributionLifetime = 0;

        this.iraGrowthRate = formData.iraGrowthRate;

        this.taxableSavingsStartOfYear = 0;
        this.taxableSavingsEndOfYear = formData.taxableSavings;
        this.taxableContributionFixedAmount = formData.taxableContributionFixedAmount;
        this.taxableContributionStrategy = formData.taxableContributionStrategy;
        this.taxableContribution = 0
        this.taxableContributionLifetime = 0;
        this.taxableContributionPercentage = formData.taxableContributionPercentage;
        this.taxableGrowthRate = formData.taxableGrowthRate;
        this.taxableGrowthAmount = undefined;
        this.inflationRate = formData.inflationRate;
        this.inflationGrowthStrategy = formData.inflationGrowthStrategy;


        this.taxableSpending = 0;
        this.taxDeferredSpending = 0;
        this.investmentGrowthStrategy = 'start'
        this.savingsStartOfYear = 0
        this.savingsEndOfYear = this.taxableSavingsEndOfYear + this.taxDeferredSavingsEndOfYear + this.iraTaxableSavingsEndOfYear + this.iraTaxDeferredSavingsEndOfYear + this.employerSavingsEndOfYear

    }

    calculateTaxableContribution(): number {
        switch (this.taxableContributionStrategy) {
            case 'fixed':
                return this.taxableContributionFixedAmount
            case 'percent_of_income':
                return this.incomePreTaxed * (this.taxableContributionPercentage / 100)

        }
    }

    calculateIraTaxableContribution(): number {
        switch (this.iraTaxableContributionStrategy) {
            case 'fixed':
                return this.iraTaxableContributionFixedAmount
            case 'percent_of_income':
                return this.incomePreTaxed * (this.iraTaxableContributionPercentage / 100)
            case 'max':
                assertDefined(this.iraContributionLimit, 'iraContributionLimit')
                assertDefined(this.iraContributionCatchUpLimit, 'iraContributionCatchUpLimit')
                return Number(this.age) >= 50 ? this.iraContributionCatchUpLimit : this.iraContributionLimit
        }

    }

    calculateIraDeferredContribution(): number {
        assertDefined(this.iraContributionCatchUpLimit, 'iraContributionCatchUpLimit')
        assertDefined(this.iraContributionLimit, 'iraContributionLimit')
        switch (this.iraTaxDeferredContributionStrategy) {
            case 'fixed':
                return this.iraTaxDeferredContributionFixedAmount
            case 'percent_of_income':
                return this.incomePreTaxed * (this.iraTaxDeferredContributionPercentage / 100)
            case 'max':
                return Number(this.age) >= 50 ? this.iraContributionCatchUpLimit : this.iraContributionLimit
        }

    }

    calculateEmployerContribution(): number {
        assertDefined(this.taxDeferredContributionLimitApplied, 'taxDeferredContributionElectiveTotalLimitApplied')
        let employerContribution = 0
        const electiveContribution = this.calculateTaxDeferredContribution()

        switch (this.employerContributionStrategy) {
            case 'none':
                break
            case "percentage_of_contribution":
                const employerMatch = electiveContribution * (this.employerMatchPercentage / 100);
                const maxEmployerMatch = this.incomePreTaxed * this.employerMatchPercentageLimit / 100;
                employerContribution = Math.min(employerMatch, maxEmployerMatch)
                break
            case "fixed":
                employerContribution = this.employerContributionFixedAmount
                break
            case "percentage_of_compensation":
                employerContribution = this.incomePreTaxed * (this.employerContributionPercentage / 100)
                break
        }
        return Math.min(employerContribution, this.taxDeferredContributionLimitApplied - electiveContribution)

    }

    calculateTaxDeferredContribution(): number {
        assertDefined(this.taxDeferredContributionElectiveLimitApplied, 'taxDeferredContributionElectiveLimitApplied')
        let electiveContribution = 0
        switch (this.taxDeferredContributionStrategy) {
            case 'fixed':
                electiveContribution = this.taxDeferredContributionFixedAmount
                break
            case 'percent_of_income':
                electiveContribution = this.incomePreTaxed * (this.taxDeferredContributionPercentage / 100)
                break
            case 'until_company_match':
                electiveContribution = this.employerMatchPercentageLimit * this.incomePreTaxed / 100
                break
            case "max":
                electiveContribution = this.taxDeferredContributionElectiveLimitApplied
                break
        }
        return Math.min(electiveContribution, this.taxDeferredContributionElectiveLimitApplied)

    }

    calculateIraTaxDeferredSavingsEndOfYear() {
        assertDefined(this.iraTaxDeferredGrowthAmount, 'iraTaxDeferredGrowthAmount')
        return this.iraTaxDeferredSavingsStartOfYear + this.iraTaxDeferredContribution + this.iraTaxDeferredGrowthAmount;


    }

    calculateIraTaxDeferredGrowthAmount(): number {
        assertDefined(this.iraTaxDeferredContribution, 'iraTaxDeferredContribution')
        switch (this.investmentGrowthStrategy) {
            case 'start':
                return this.iraTaxDeferredSavingsStartOfYear * (this.iraGrowthRate / 100)
            case 'end':
                return (this.iraTaxDeferredSavingsStartOfYear + this.iraTaxDeferredContribution) * (this.iraGrowthRate / 100)
        }
    }

    calculateTaxableGrowthAmount(): number {
        switch (this.investmentGrowthStrategy) {
            case 'start':
                return this.taxableSavingsStartOfYear * (this.taxableGrowthRate / 100)
            case 'end':
                return (this.taxableSavingsStartOfYear + this.taxableContribution) * (this.taxableGrowthRate / 100)
        }
    }

    calculateTaxableSavingsEndOfYear(): number {
        assertDefined(this.taxableGrowthAmount, 'taxableGrowthAmount')
        return this.taxableSavingsStartOfYear + this.taxableContribution + this.taxableGrowthAmount;

    }

    calculateIraTaxableGrowthAmount(): number {
        switch (this.investmentGrowthStrategy) {
            case 'start':
                return this.iraTaxableSavingsStartOfYear * (this.iraGrowthRate / 100)
            case 'end':
                return (this.iraTaxableSavingsStartOfYear + this.iraTaxableContribution) * (this.iraGrowthRate / 100)
        }
    }

    calculateIraTaxableSavingsEndOfYear(): number {
        assertDefined(this.iraTaxableGrowthAmount, 'iraTaxableGrowthAmount')
        return this.iraTaxableSavingsStartOfYear + this.iraTaxableContribution + this.iraTaxableGrowthAmount;

    }

    calculateTaxDeferredGrowthAmount(): number {
        switch (this.investmentGrowthStrategy) {
            case 'start':
                return this.taxDeferredSavingsStartOfYear * (this.taxDeferredGrowthRate / 100)
            case 'end':
                return (this.taxDeferredSavingsStartOfYear + this.taxDeferredContribution) * (this.taxDeferredGrowthRate / 100)
        }
    }

    calculateTaxDeferredSavingsEndOfYear(): number {
        assertDefined(this.taxDeferredGrowthAmount, 'taxDeferredGrowthAmount')
        return this.taxDeferredSavingsStartOfYear + this.taxDeferredContribution + this.taxDeferredGrowthAmount;
    }

    calculateEmployerSavingsEndOfYear(): number {
        assertDefined(this.employerGrowthAmount, 'employerGrowthAmount')
        return this.employerSavingsStartOfYear + this.employerContribution + this.employerGrowthAmount
    }


    calculateEmployerGrowthAmount(): number {
        switch (this.investmentGrowthStrategy) {
            case 'start':
                return this.employerSavingsStartOfYear * (this.taxDeferredGrowthRate / 100)
            case 'end':
                return (this.employerSavingsStartOfYear + this.employerContribution) * (this.taxDeferredGrowthRate / 100)
        }
    }

    calculateIncomeTaxable(): number {
        return this.incomePreTaxed - this.taxDeferredSpending

    }

    calculateIncomeTaxAmount(): number {
        assertDefined(this.incomeTaxable, 'incomeTaxable')
        switch (this.incomeTaxStrategy) {
            case 'bracket':
                return this.incomeTaxable * this.incomeTaxRate / 100
            case 'simple':
                return this.incomeTaxable * this.incomeTaxRate / 100
        }
    }


    calculateIncomeTaxed(): number {
        assertDefined(this.incomeTaxable, 'incomeTaxable')
        assertDefined(this.incomeTaxAmount, 'incomeTaxAmount')
        return this.incomeTaxable - this.incomeTaxAmount;
    }


    calculateIncomeDisposable(): number {
        assertDefined(this.incomeTaxed, 'incomeTaxed')
        return this.incomeTaxed - this.taxableSpending - this.expenses
    }

    calculateCashEndOfYear(): number {
        assertDefined(this.incomeDisposable, 'incomeDisposable')
        return this.incomeDisposable
    }


    calculateRetirementIncomeProjected(): number {
        return this.savingsEndOfYear * this.retirementWithdrawalRate / 100
    }


    calculateIncome(): number {
        switch (this.incomeGrowthStrategy) {
            case "fixed":
                return this.incomePreTaxed
            case "percentage_increase":
                return this.incomePreTaxed * (1 + this.incomeGrowthRate / 100)
        }
    }

    calculateTaxDeferredContributionElectiveLimitApplied(): number {
        return this.age < TAX_DEFERRED_CATCH_UP_AGE ? this.taxDeferredContributionElectiveLimit : this.taxDeferredContributionElectiveLimit + this.taxDeferredContributionElectiveCatchUpLimit
    }

    calculateTaxDeferredContributionLimitApplied(): number {
        return this.age < TAX_DEFERRED_CATCH_UP_AGE ? this.taxDeferredContributionLimit : this.taxDeferredContributionLimit + this.taxDeferredContributionElectiveCatchUpLimit
    }

    calculateAdjustedTaxDeferredContributionLimit(): number {
        return this.taxDeferredContributionLimit * (1 + this.taxDeferredContributionLimitInflationRate / 100)
    }

    calculateAdjustedTaxDeferredContributionElectiveLimit(): number {
        return this.taxDeferredContributionElectiveLimit * (1 + this.taxDeferredContributionLimitInflationRate / 100)
    }

    calculateAdjustedTaxDeferredContributionElectiveCatchUpLimit(): number {
        return this.taxDeferredContributionElectiveCatchUpLimit * (1 + this.taxDeferredContributionLimitInflationRate / 100)
    }

}
