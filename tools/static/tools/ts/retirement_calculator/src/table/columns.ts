import {Row} from "../interfaces/Row";

interface ColumnDefinition<K extends keyof Row> {
    id: K;
    value: K;
    label: string;
    format: string;
    section: string;
    show: boolean;
}

const tableColumns: ColumnDefinition<keyof Row>[] = [
    {id: 'age', value: 'age', label: 'age', format: 'number', section: 'personal', show: true},
    {id: 'year', value: 'year', label: 'year', format: 'number', section: 'personal', show: true},
    {id: 'lifeExpectancy', value: 'lifeExpectancy', label: 'lifeExpectancy', format: 'number', section: 'personal', show: true},
    {
        id: 'retirementStrategy',
        value: 'retirementStrategy',
        label: 'retirementStrategy',
        format: 'string',
        section: 'retirement',
        show: true
    },
    {
        id: 'retirementWithdrawalRate',
        value: 'retirementWithdrawalRate',
        label: 'retirementWithdrawalRate',
        format: 'number',
        section: 'retirement',
        show: true
    },
    {
        id: 'retirementIncomeGoal',
        value: 'retirementIncomeGoal',
        label: 'retirementIncomeGoal',
        format: 'currency',
        section: 'retirement',
        show: true
    },
    {id: 'retirementAge', value: 'retirementAge', label: 'retirementAge', format: 'currency', section: 'retirement', show: true},
    {
        id: 'retirementSavingsAmount',
        value: 'retirementSavingsAmount',
        label: 'retirementSavingsAmount',
        format: 'currency',
        section: 'retirement',
        show: true
    },
    {
        id: 'retirementIncomeProjected',
        value: 'retirementIncomeProjected',
        label: 'retirementIncomeProjected',
        format: 'currency',
        section: 'retirement',
        show: true
    },
    {id: 'cashStartOfYear', value: 'cashStartOfYear', label: 'cashStartOfYear', format: 'currency', section: 'savings', show: true},
    {id: 'cashEndOfYear', value: 'cashEndOfYear', label: 'cashEndOfYear', format: 'currency', section: 'savings', show: true},
    {id: 'incomeDisposable', value: 'incomeDisposable', label: 'incomeDisposable', format: 'currency', section: 'income', show: true},
    {id: 'incomePreTaxed', value: 'incomePreTaxed', label: 'incomePreTaxed', format: 'currency', section: 'income', show: true},
    {id: 'incomeTaxable', value: 'incomeTaxable', label: 'incomeTaxable', format: 'currency', section: 'income', show: true},
    {id: 'incomeTaxed', value: 'incomeTaxed', label: 'incomeTaxed', format: 'currency', section: 'income', show: true},
    {
        id: 'incomeGrowthStrategy',
        value: 'incomeGrowthStrategy',
        label: 'incomeGrowthStrategy',
        format: '',
        section: 'income',
        show: true
    },
    {id: 'incomeGrowthRate', value: 'incomeGrowthRate', label: 'incomeGrowthRate', format: 'percent', section: 'income', show: true},
    {id: 'incomeGrowthAmount', value: 'incomeGrowthAmount', label: 'incomeGrowthAmount', format: 'currency', section: 'income', show: true},
    {id: 'incomeTaxAmount', value: 'incomeTaxAmount', label: 'incomeTaxAmount', format: 'currency', section: 'income', show: true},
    {id: 'incomeTaxRate', value: 'incomeTaxRate', label: 'incomeTaxRate', format: '', section: 'income', show: true},
    {id: 'incomeTaxStrategy', value: 'incomeTaxStrategy', label: 'incomeTaxStrategy', format: '', section: 'income', show: true},
    {
        id: 'incomeTaxFilingStatus',
        value: 'incomeTaxFilingStatus',
        label: 'incomeTaxFilingStatus',
        format: '',
        section: 'income',
        show: true
    },
    {
        id: 'incomeTaxNumberOfDependents',
        value: 'incomeTaxNumberOfDependents',
        label: 'incomeTaxNumberOfDependents',
        format: 'number',
        section: 'income',
        show: true
    },
    {id: 'expenses', value: 'expenses', label: 'expenses', format: 'currency', section: 'income', show: true},
    {id: 'expenseRate', value: 'expenseRate', label: 'expenseRate', format: 'percent', section: 'income', show: true},
    {
        id: 'expensesGrowthStrategy',
        value: 'expensesGrowthStrategy',
        label: 'expensesGrowthStrategy',
        format: 'string',
        section: 'income',
        show: true
    },
    {id: 'debtStartOfYear', value: 'debtStartOfYear', label: 'debtStartOfYear', format: 'currency', section: 'debt', show: true},
    {id: 'debtEndOfYear', value: 'debtEndOfYear', label: 'debtEndOfYear', format: 'currency', section: 'debt', show: true},
    {id: 'debtInterestRate', value: 'debtInterestRate', label: 'debtInterestRate', format: 'percent', section: 'debt', show: true},
    {id: 'debtPayment', value: 'debtPayment', label: 'debtPayment', format: 'currency', section: 'debt', show: true},
    {id: 'debtPaymentTotal', value: 'debtPaymentTotal', label: 'debtPaymentTotal', format: 'currency', section: 'debt', show: true},
    {
        id: 'taxDeferredSavingsStartOfYear',
        value: 'taxDeferredSavingsStartOfYear',
        label: 'taxDeferredSavingsStartOfYear',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionFixedAmount',
        value: 'taxDeferredContributionFixedAmount',
        label: 'taxDeferredContributionFixedAmount',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionStrategy',
        value: 'taxDeferredContributionStrategy',
        label: 'taxDeferredContributionStrategy',
        format: '',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContribution',
        value: 'taxDeferredContribution',
        label: 'taxDeferredContribution',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionTotal',
        value: 'taxDeferredContributionTotal',
        label: 'taxDeferredContributionTotal',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredGrowthAmount',
        value: 'taxDeferredGrowthAmount',
        label: 'taxDeferredGrowthAmount',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionPercentage',
        value: 'taxDeferredContributionPercentage',
        label: 'taxDeferredContributionPercentage',
        format: 'percent',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredSavingsEndOfYear',
        value: 'taxDeferredSavingsEndOfYear',
        label: 'taxDeferredSavingsEndOfYear',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredGrowthRate',
        value: 'taxDeferredGrowthRate',
        label: 'taxDeferredGrowthRate',
        format: 'percent',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionLifetime',
        value: 'taxDeferredContributionLifetime',
        label: 'taxDeferredContributionLifetime',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionElectiveCatchUpLimit',
        value: 'taxDeferredContributionElectiveCatchUpLimit',
        label: 'taxDeferredContributionCatchUpLimit',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionElectiveLimit',
        value: 'taxDeferredContributionElectiveLimit',
        label: 'taxDeferredContributionElectiveLimit',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionElectiveLimitApplied',
        value: 'taxDeferredContributionElectiveLimitApplied',
        label: 'taxDeferredContributionElectiveLimitApplied',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionLimit',
        value: 'taxDeferredContributionLimit',
        label: 'taxDeferredContributionTotalElectiveLimit',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionLimitApplied',
        value: 'taxDeferredContributionLimitApplied',
        label: 'taxDeferredContributionElectiveTotalLimitApplied',
        format: 'currency',
        section: 'deferred',
        show: true
    },
    {
        id: 'taxDeferredContributionLimitInflationRate',
        value: 'taxDeferredContributionLimitInflationRate',
        label: 'taxDeferredContributionElectiveLimitInflationRate',
        format: 'percent',
        section: 'deferred',
        show: true
    },
    {
        id: 'employerContributionStrategy',
        value: 'employerContributionStrategy',
        label: 'employerContributionStrategy',
        format: '',
        section: 'employer',
        show: true
    },
    {
        id: 'employerContribution',
        value: 'employerContribution',
        label: 'employerContribution',
        format: 'currency',
        section: 'employer',
        show: true
    },
    {
        id: 'employerMatchPercentage',
        value: 'employerMatchPercentage',
        label: 'employerMatchPercentage',
        format: 'percent',
        section: 'employer',
        show: true
    },
    {
        id: 'employerMatchPercentageLimit',
        value: 'employerMatchPercentageLimit',
        label: 'employerMatchPercentageLimit',
        format: 'percent',
        section: 'employer',
        show: true
    },
    {
        id: 'employerContributionPercentage',
        value: 'employerContributionPercentage',
        label: 'employerContributionPercentage',
        format: 'percent',
        section: 'employer',
        show: true
    },
    {
        id: 'employerContributionFixedAmount',
        value: 'employerContributionFixedAmount',
        label: 'employerContributionFixedAmount',
        format: 'currency',
        section: 'employer',
        show: true
    },
    {
        id: 'employerSavingsStartOfYear',
        value: 'employerSavingsStartOfYear',
        label: 'employerSavingsStartOfYear',
        format: 'currency',
        section: 'employer',
        show: true
    },
    {
        id: 'employerSavingsEndOfYear',
        value: 'employerSavingsEndOfYear',
        label: 'employerSavingsEndOfYear',
        format: 'currency',
        section: 'employer',
        show: true
    },
    {
        id: 'employerContributionLifetime',
        value: 'employerContributionLifetime',
        label: 'employerContributionLifetime',
        format: 'currency',
        section: 'employer',
        show: true
    },
    {
        id: 'employerGrowthAmount',
        value: 'employerGrowthAmount',
        label: 'employerGrowthAmount',
        format: 'currency',
        section: 'employer',
        show: true
    },
    {
        id: 'iraTaxableSavingsStartOfYear',
        value: 'iraTaxableSavingsStartOfYear',
        label: 'iraTaxableSavingsStartOfYear',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxableSavingsEndOfYear',
        value: 'iraTaxableSavingsEndOfYear',
        label: 'iraTaxableSavingsEndOfYear',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxableContribution',
        value: 'iraTaxableContribution',
        label: 'iraTaxableContribution',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxableContributionFixedAmount',
        value: 'iraTaxableContributionFixedAmount',
        label: 'iraTaxableContributionFixedAmount',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxableContributionStrategy',
        value: 'iraTaxableContributionStrategy',
        label: 'iraTaxableContributionStrategy',
        format: '',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxableContributionPercentage',
        value: 'iraTaxableContributionPercentage',
        label: 'iraTaxableContributionPercentage',
        format: 'percent',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxableContributionLifetime',
        value: 'iraTaxableContributionLifetime',
        label: 'iraTaxableContributionLifetime',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxableGrowthAmount',
        value: 'iraTaxableGrowthAmount',
        label: 'iraTaxableGrowthAmount',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxDeferredSavingsStartOfYear',
        value: 'iraTaxDeferredSavingsStartOfYear',
        label: 'iraTaxDeferredSavingsStartOfYear',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxDeferredSavingsEndOfYear',
        value: 'iraTaxDeferredSavingsEndOfYear',
        label: 'iraTaxDeferredSavingsEndOfYear',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxDeferredContribution',
        value: 'iraTaxDeferredContribution',
        label: 'iraTaxDeferredContribution',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxDeferredContributionFixedAmount',
        value: 'iraTaxDeferredContributionFixedAmount',
        label: 'iraTaxDeferredContributionFixedAmount',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxDeferredContributionStrategy',
        value: 'iraTaxDeferredContributionStrategy',
        label: 'iraTaxDeferredContributionStrategy',
        format: 'string',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxDeferredContributionPercentage',
        value: 'iraTaxDeferredContributionPercentage',
        label: 'iraTaxDeferredContributionPercentage',
        format: 'percent',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxDeferredContributionLifetime',
        value: 'iraTaxDeferredContributionLifetime',
        label: 'iraTaxDeferredContributionLifetime',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraTaxDeferredGrowthAmount',
        value: 'iraTaxDeferredGrowthAmount',
        label: 'iraTaxDeferredGrowthAmount',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {id: 'iraGrowthRate', value: 'iraGrowthRate', label: 'iraGrowthRate', format: 'currency', section: 'ira', show: true},
    {
        id: 'iraContributionLimit',
        value: 'iraContributionLimit',
        label: 'iraContributionLimit',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'iraContributionCatchUpLimit',
        value: 'iraContributionCatchUpLimit',
        label: 'iraContributionCatchUpLimit',
        format: 'currency',
        section: 'ira',
        show: true
    },
    {
        id: 'taxableSavingsStartOfYear',
        value: 'taxableSavingsStartOfYear',
        label: 'taxableSavingsStartOfYear',
        format: 'currency',
        section: 'taxable',
        show: true
    },
    {
        id: 'taxableSavingsEndOfYear',
        value: 'taxableSavingsEndOfYear',
        label: 'taxableSavingsEndOfYear',
        format: 'currency',
        section: 'taxable',
        show: true
    },
    {
        id: 'taxableContributionFixedAmount',
        value: 'taxableContributionFixedAmount',
        label: 'taxableContributionFixedAmount',
        format: 'currency',
        section: 'taxable',
        show: true
    },
    {
        id: 'taxableContribution',
        value: 'taxableContribution',
        label: 'taxableContribution',
        format: 'currency',
        section: 'taxable',
        show: true
    },
    {
        id: 'taxableContributionStrategy',
        value: 'taxableContributionStrategy',
        label: 'taxableContributionStrategy',
        format: 'currency',
        section: 'taxable',
        show: true
    },
    {
        id: 'taxableContributionLifetime',
        value: 'taxableContributionLifetime',
        label: 'taxableContributionLifetime',
        format: 'currency',
        section: 'taxable',
        show: true
    },
    {
        id: 'taxableContributionPercentage',
        value: 'taxableContributionPercentage',
        label: 'taxableContributionPercentage',
        format: 'percent',
        section: 'taxable',
        show: true
    },
    {id: 'taxableGrowthRate', value: 'taxableGrowthRate', label: 'taxableGrowthRate', format: 'currency', section: 'taxable', show: true},
    {
        id: 'taxableGrowthAmount',
        value: 'taxableGrowthAmount',
        label: 'taxableGrowthAmount',
        format: 'currency',
        section: 'taxable',
        show: true
    },
    {id: 'inflationRate', value: 'inflationRate', label: 'inflationRate', format: 'currency', section: 'extra', show: true},
    {
        id: 'inflationGrowthStrategy',
        value: 'inflationGrowthStrategy',
        label: 'inflationGrowthStrategy',
        format: 'string',
        section: 'extra',
        show: true
    },
    {id: 'savingsStartOfYear', value: 'savingsStartOfYear', label: 'savingsStartOfYear', format: 'currency', section: 'extra', show: true},
    {id: 'savingsEndOfYear', value: 'savingsEndOfYear', label: 'savingsEndOfYear', format: 'currency', section: 'extra', show: true},
    {id: 'taxableSpending', value: 'taxableSpending', label: 'taxableSpending', format: 'currency', section: 'extra', show: true},
    {
        id: 'taxDeferredSpending',
        value: 'taxDeferredSpending',
        label: 'taxDeferredSpending',
        format: 'currency',
        section: 'extra',
        show: true
    },
    {
        id: 'investmentGrowthStrategy',
        value: 'investmentGrowthStrategy',
        label: 'investmentGrowthStrategy',
        format: 'string',
        section: 'extra',
        show: true
    },
]

export default tableColumns