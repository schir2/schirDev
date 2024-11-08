import {Row} from "../interfaces/Row";
import {Pipeline} from "../interfaces/Pipeline";

export default class EndOfYearPipeline implements Pipeline {

    initialize(row: Row): Row {
        row.incomeTaxable = this.calculateIncomeTaxable(row)
        row.incomeTaxAmount = this.calculateIncomeTaxAmount(row)
        console.log(row.incomeTaxAmount)
        row.incomeTaxed = this.calculateIncomeTaxed(row)
        row.incomeDisposable = this.calculateIncomeDisposable(row)
        row.cashEndOfYear = this.calculateEndOfYearCash(row)
        row.retirementIncomeProjected = this.calculateRetirementIncomeProjected(row)
        return row
    }


    private calculateIncomeTaxed(row: Row) {
        return row.incomeTaxable - row.incomeTaxAmount;
    }

    process(row: Row): Row {
        row.incomeTaxable = this.calculateIncomeTaxable(row)
        row.incomeTaxAmount = this.calculateIncomeTaxAmount(row)
        row.incomeTaxed -= this.calculateIncomeTaxed(row)
        row.incomeDisposable = this.calculateIncomeDisposable(row)
        row.cashEndOfYear = this.calculateEndOfYearCash(row)
        row.retirementIncomeProjected = this.calculateRetirementIncomeProjected(row)
        row = this.calculateIncome(row)
        return row
    }

    private calculateIncome(row: Row): Row {
        switch (row.incomeGrowthStrategy) {
            case "fixed":
                return row
            case "percentage_increase":
                row.incomePreTaxed = row.incomePreTaxed * (1 + row.incomeGrowthRate / 100)
                return row
        }
    }

    calculateIncomeTaxable(row: Row): number {
        console.log(row.incomePreTaxed, row.taxDeferredSpending)
        return row.incomePreTaxed - row.taxDeferredSpending
    }


    private calculateIncomeTaxAmount(row: Row): number {
        switch (row.incomeTaxStrategy) {
            case 'bracket':
                return row.incomeTaxable * row.incomeTaxRate / 100
            case 'simple':
                return row.incomeTaxable * row.incomeTaxRate / 100
        }
    }

    private calculateIncomeDisposable(row: Row): number {
        return row.incomeTaxed - row.taxableSpending - row.expenses
    }

    private calculateEndOfYearCash(row: Row): number {
        return row.incomeDisposable
    }

    private calculateRetirementIncomeProjected(row: Row): number {
        return row.savingsEndOfYear * row.retirementWithdrawalRate / 100
    }
}