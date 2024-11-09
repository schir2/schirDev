import {Row} from "../interfaces/Row";
import {Pipeline} from "../interfaces/Pipeline";

export default class EndOfYearPipeline implements Pipeline {

    process(row: Row): Row {
        row.incomeTaxable = row.calculateIncomeTaxable()
        row.incomeTaxAmount = row.calculateIncomeTaxAmount()
        row.incomeTaxed = row.calculateIncomeTaxed()
        row.incomeDisposable = row.calculateIncomeDisposable()
        row.cashEndOfYear = row.calculateEndOfYearCash()
        row.retirementIncomeProjected = row.calculateRetirementIncomeProjected()
        return row
    }
}